from flask import Flask, render_template, request
import json
import os.path
from scripts import emailer
from datetime import datetime, timedelta
import parsedatetime.parsedatetime as pdt
from parsedatetime import Constants as pdc 

SCHEDULE_FILE = "schedule.json"

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/addevent", methods=["GET", "POST"])
def addevent():
    if request.method == "GET":
        return render_template("addevent.html")
    else:

        # Write data
        event = dict()
        event["name"] = request.form["name"]
        event["location"] = request.form["location"]
        event["datetime"] = request.form["date"] + " " + request.form["time"]
        event["email"] = request.form["email"]
        event["message"] = request.form["message"]
        event["remindme"] = request.form["remindme"]
        
        data = []
        if os.path.isfile(SCHEDULE_FILE):
            with open(SCHEDULE_FILE, "r") as schedule:
                data = json.load(schedule)

        data += [event]

        with open(SCHEDULE_FILE, "w") as schedule:
            json.dump(data, schedule)
            
        return render_template("message.html", title="Event Submitted",
                               header="Event Submitted!",
                               message=(request.form["name"] +
                                        " has been submitted!"))

@app.route("/email", methods=["GET", "POST"])
def email():
    with open(SCHEDULE_FILE, "r") as schedule:
        emailer.send(json.load(schedule)) # that was painless
    return render_template("message.html", title="Email Sent",
                           header="Reminder sent!",
                           message="We just sent a reminder for the last event you have.")

@app.route("/list")
def list():
    with open(SCHEDULE_FILE, "r") as schedule:
        data = json.load(schedule)

    result = "<ul>"

    for event in data:
        result += "<li><b>{}</b>: {} at {}</li>".format(event["name"],
                                                        event["message"],
                                                        event["location"])

    result += "</ul>"
    return render_template("message.html", title="Events List",
                           header="List of Events",
                           message=result)

@app.route("/calendar")
def calendar():
    with open(SCHEDULE_FILE, "r") as schedule:
        data = json.load(schedule)

    result = "<table><tr>"

    def iter_hours(start, end, delta):
        while start < end:
            yield start
            start += delta

    # HEADERS
    now = roundTime(datetime.now(), 60*60)
    later = now + timedelta(days=1)
    for date in iter_hours(now, later, timedelta(hours=1)):
        result += "<td>" + date.strftime("%I:%M %p") + "</td>"
    result += "</tr>"

    # EVENTS
    def event_to_datetime(event):
        return datetime(*pdt.Calendar(pdt.Constants()).parse(event["datetime"]))
    for day_of_week in range(7):
        events_today = [x for x in data if event_to_datetime(x).weekday() == day_of_week]
        result += "<tr>"
        for date in iter_hours(roundTime(datetime.now(), 60*60),
                               roundTime(datetime.now(), 60*60) + timedelta(days=1),
                               timedelta(hours=1)):
            result += "<td>alsdfasdfasd</td>"
        result += "</tr>"
            

    result += "</table>"
    return render_template("message.html", title="Calendar",
                           header="Calendar",
                           message=result)

def roundTime(dt=None, roundTo=60):
   """Round a datetime object to any time laps in seconds
   dt : datetime.datetime object, default now.
   roundTo : Closest number of seconds to round to, default 1 minute.
   Author: Thierry Husson 2012 - Use it as you want but don't blame me.
   From http://stackoverflow.com/a/10854034/1757964
   """
   if dt == None : dt = datetime.datetime.now()
   seconds = (dt - dt.min).seconds
   # // is a floor division, not a comment on following line:
   rounding = (seconds+roundTo/2) // roundTo * roundTo
   return dt + timedelta(0,rounding-seconds,-dt.microsecond)

if __name__ == "__main__":
    app.debug = True
    app.run()
