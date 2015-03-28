from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/addevent", methods=["GET", "POST"])
def addevent_submit():
    if request.method == "GET":
        return render_template("addevent.html")
    else:
        return "Submitted event called '{}'.".format(request.form["name"])

if __name__ == "__main__":
    app.debug = True
    app.run()
