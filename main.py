from flask import Flask, render_template, request
import json

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
        
        data = []
        with open("schedule.json", "r+") as schedule:
            data = json.load(schedule)

        data += [event]

        with open("schedule.json", "w") as schedule:
            json.dump(data, schedule)
            
        return render_template("submitevent.html", name=request.form["name"])

if __name__ == "__main__":
    app.debug = True
    app.run()
