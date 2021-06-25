from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def index():

    title = "The Exam"

    text = """It is a cold, snowy afternoon at the University of Chicago and you have a Finance exam worth 40% of your grade at 11:30 am.
                You wake up at 9am in a cold sweat and you realize you did not study for it at all."""

    image = url_for('static', filename='index.jpg')

    choices = [
        ('business_as_usual',"Get ready for the day"),
        ('panic',"Rush out of the door and go to the library")
    ]

    template_context = dict(title=title, text=text, choices=choices, image=image)
    return render_template('adventure.html', **template_context)



@app.route("/panic")
def panic():
    title = "You rush to the library"

    text = """You rush to the library across campus that is closest to the testing location and go into your backpack to get your study materials, only to realize
              that you left your notes in your dorm room. You hang your head and accept defeat."""

    image = url_for('static', filename="panic.jpg")

    choices = []

    template_context = dict(title=title, text=text, choices=choices, image=image)

    return render_template('adventure.html', **template_context)

@app.route("/usual")
def business_as_usual():
    title = "You get ready for the day."

    text = """You spend 30 minutes getting ready for the day and walk to the nearest library
            before sitting down."""

    image = url_for('static', filename="business_as_usual.jpg")

    choices = [
            ('plan', "You plan out what topics to study."),
            ('study', "You start studying immediately")
            ]

    template_context = dict(title=title, text=text, choices=choices, image=image)
    return render_template('adventure.html', **template_context)


@app.route("/plan")
def plan():
    title = "Plan it out."

    text = """You make a detailed plan of how to study and focus on covering the subjects you struggle
            with the most. You end up getting a 93% on the exam. Great job!"""

    image = url_for('static', filename="plan.jpg")

    choices = []

    template_context = dict(title=title, text=text, choices=choices, image=image)
    return render_template('adventure.html', **template_context)

@app.route("/study")
def study():
    title= "You start studying from the beginning of the test material."

    text = """You end up getting through most of the material and get a 75% on the exam. Cs get degrees you suppose."""

    image = url_for('static', filename="study.jpg")

    choices = []

    template_context = dict(title=title, text=text, choices=choices, image=image)
    return render_template('adventure.html', **template_context)
