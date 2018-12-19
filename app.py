from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>server가 html도 보내주나???</h1>"
    
@app.route("/html_tag")
def html_tag():
    return """
    <h1>one!!</h1>
    <h2>two!!</h2>
    """
    
@app.route("/html_file")
def html_file():
    return render_template("html_file.html")
    
    
@app.route("/welcome/<string:name>")
def welcome(name):
    return render_template("welcome.html",people=name)
    
@app.route("/cube/<int:num>")
def cube(num):
    triple = num**3
    return render_template("cube.html",triple=triple,num=num)
    
@app.route('/lunch')
def lunch():
    menu = ['삼겹살','떡볶이','치킨','곰탕']
    choice = random.choice(menu)
    return render_template("lunch.html",lunchmenu=choice)
    
@app.route('/lotto')
def lotto():
    numbers = range(1,46)
    lottonum = random.sample(numbers,6)
    sort_pick = sorted(lottonum)
    return render_template("lotto.html",sort_pick=sort_pick)
    
@app.route('/naver')
def naver():
    return render_template("naver.html")
    
@app.route('/google')
def google():
    return render_template("google.html")
   
    