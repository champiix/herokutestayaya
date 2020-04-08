from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "bro are you disrespecting my japanese culture bro i’m more japan than all of you because i watch anime and you don’t, i bet you don’t even know what Naruto is you degenerate. So before you message me acting like you know my culture maybe check yourself first"

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():  
    t = Thread(target=run)
    t.start()