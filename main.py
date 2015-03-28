from flask import Flask, render_template, request
import json
import os.path

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
    return render_template("message.html", title="Error",
                           header="Not implemented yet!",
                           message="Sorry, we haven't implemented email yet.")

if __name__ == "__main__":
    app.debug = True
    app.run()
