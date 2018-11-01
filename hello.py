# import sys
# sys.path.append("../../myEnvironments/py3Env/lib/python3.7/site-packages")
from flask import Flask, render_template
import re
 
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html', phrase="hello", times=5)

@app.route("/coding")
def coding():
    return "<h1> Coding Dojo <h1>"

@app.route("/hello/<name>")
def hello(name):
    print(name)
    return "Hello, " + name

@app.route("/repeat/<num>/<name>")
def repeater(num,name):
    print(name * int(num))
    return name * int(num)  

@app.route("/play/")
def play():
    return render_template("boxes.html")

@app.route("/play/<num>")
def play_num(num):
    return render_template("boxes.html", num = int(num))

@app.route("/play/<num>/<color>")
def play_num_color(num, color):
    return render_template('boxes.html', num = int(num), color = color)

if __name__ =='__main__':
    app.run(debug=True)


# my cool regex code that I wont use... :)
# 
# play_pattern = re.compile(r'^([\w\-]+)')
        # play = play_pattern.finditer(play_num_color)

        # number_pattern = re.compile(r'\d')
        # number = number_pattern.finditer(play_num_color)

        # color_pattern  = re.compile(r'\b(\w+)\W*$')
        # color = color_pattern.finditer(play_num_color)

        # for k in color:
        #      color = (k.group(0))

        # for k in number:
        #     number = (k.group(0))
        #     print(number)
        
        # for k in play:
        #     play = (k.group(0))
        #     print(play)