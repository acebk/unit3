from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def index():

    title = "This is my FizzBuzz Site"
    comment = "To activate FizzBuzz, add '/fizzbuzz/number' to the end of the url"

    return render_template('fizzbuzz.html', title=title, comment=comment)




@app.route("/fizzbuzz/<int:num>")
def fizzbuzz(num):

    list=[]

    for n in range(1,num+1):
        if n%3 ==0 and n%5 ==0:
            list.append("FizzBuzz")
        elif n%5==0:
            list.append("Buzz")
        elif n%3==0:
            list.append("Fizz")
        else:
            list.append(n)

    return render_template('fizzbuzz.html', list=list )
