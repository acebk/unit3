from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():

    title = "The Exam"

    text = """It is a cold, snowy afternoon at the University of Chicago and you have a Finance exam worth 40% of your grade at 11:30 am.
                You wake up at 9am in a cold sweat and you realize you did not study for it at all."""

    choices = [
        ('business_as_usual',"Get ready for the day"),
        ('panic',"Rush out of the door and go to the library")
    ]

    template_context = dict(title=title, text=text, choices=choices)
    return render_template('adventure.html', **template_context)



@app.route("/panic")
def panic():
    title = "You rush to the library"

    text = """You rush to the library across campus that is closest to the testing location and go into your backpack to get your study materials, only to realize
              that you left your notes in your dorm room. You hang your head and accept defeat."""

    choices = []

    template_context = dict(title=title, text=text, choices=choices)

    return render_template('adventure.html', **template_context)

@app.route("/usual")
def business_as_usual():
    title = "You get ready for the day."

    text = """You spend 30 minutes getting ready for the day and walk to the nearest library
            before sitting down."""

    choices = [
            ('plan', "You plan out what topics to study."),
            ('study', "You start studying immediately in the interest of utilizing all of the time available to you.")
            ]

    template_context = dict(title=title, text=text, choices=choices)
    return render_template('adventure.html', **template_context)


@app.route("/plan")
def plan():
    title = "Plan it out."

    text = """You make a detailed plan of how to study and focus on covering the subjects you struggle
            with the most. You end up getting a 93% on the exam. Great job!"""

    choices = []

    template_context = dict(title=title, text=text, choices=choices)
    return render_template('adventure.html', **template_context)

@app.route("/study")
def study():
    title= "You start studying from the beginning of the test material."

    text = """You end up getting through most of the material and get a 75% on the exam. Cs get degrees you suppose."""

    choices = []

    template_context = dict(title=title, text=text, choices=choices)
    return render_template('adventure.html', **template_context)
