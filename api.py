import flask
from chat import bot_response
from flask import Flask, render_template, request
import webbrowser
from datetime import datetime, time

now = datetime.now()

current_time = now.strftime("%H:%M")



app = Flask(__name__,template_folder="./")
app.static_folder = 'static'

@app.route("/dark")
def chat():
    return render_template("dark theme.html",time=current_time)

@app.route("/")
def home():
    
    return render_template("index.html",tym=current_time)

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    answer = str(bot_response(userText))
    return answer

if __name__ == "__main__":
    webbrowser.open('http://localhost:5000')
    app.run(host='localhost')
    