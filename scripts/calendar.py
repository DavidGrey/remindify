from flask import Flask, render_template, request 
import datetime
datetime.datetime.strptime('3/30/2015 6:15 PM', '%m/%d/%Y %I:%M %p').strftime('%A')

m = ''

#app = Flask (__name__)

#@app.route( "/" )

Sunday = m
Monday = m
Tuesady = m
Wednesady = m
Thursday = m
Friday = m
Saturday = m

def comp ():
    thing = [Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday]
    c = 0
    for c in range(thing):
        if datetime.datetime.strptime('datetime from your file', '%m/%d/%Y %I:%M %p').strftime('%A')  == str(thing[c]):
            thing[c]+= 
        return False
         
def index():
    if comp:
      return render_template( "Calender.html",
      Sunday= m,
      Monday= m,
      Tuesday= m,
      Wednesday= m,
      Thursday= m,
      Friday= m,
      Saturday= m)
