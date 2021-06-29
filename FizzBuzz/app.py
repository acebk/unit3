from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def index():

    title = "This is my FizzBuzz Site"
    comment = "To activate FizzBuzz, add '/fizzbuzz/number' to the end of the url."
    comment2 = "To activate anagrams, add 'words/word' to the end of the url."
    return render_template('fizzbuzz.html', title=title, comment=comment, comment2=comment2)




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

@app.route("/words/<string:word>")
def words(word):

    words=[]
    f = open("static/words.txt")
    dictionary = f.read().splitlines()

    for w in dictionary:
        if sorted(word.upper()) == sorted(w): 
            words.append(w)

    return render_template('fizzbuzz.html', words=words, dictionary=dictionary)
