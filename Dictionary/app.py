from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def index():
    f = open("static/words.txt")
    dictionary = f.read().splitlines()
    list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    title = "This is my dictionary Website"
    dict_length = len(dictionary)
    return render_template('dictionary.html', title=title, dict_length=dict_length, list=list)

@app.route("/<string:word>")
def words(word):

    title = "This is my dictionary Website"
    f = open("static/words.txt")
    dictionary = f.read().splitlines()

    list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    dict_list = []
    valid = 0

    for letter in list:
        dict_list.append(str(word)+letter)

    for index in dictionary:
        if word.upper() == index[:len(word)] and len(word) != len(index):
            valid += 1

    if valid == 1:
        tense = 'word'
        poss = "has"
        x = 'is'
    else:
        tense = 'words'
        poss= "have"
        x = "are"
    return render_template('dictionary.html', dict_list=dict_list, valid=valid,
     word=word, dictionary=dictionary, tense=tense, title=title, poss=poss, x=x)
