from flask import Flask, jsonify, render_template, request
from config import Config
import RPi.GPIO as io

app = Flask(__name__)
app.config.from_object(Config)

LED_CHANNEL = 7
io.setmode(io.BOARD)
io.setup(LED_CHANNEL, io.OUT)

@app.route("/", methods=['GET','POST'])
def home():
    if request.method == 'POST':
        print("CLICK!")
        if io.input(LED_CHANNEL):
            io.output(LED_CHANNEL, False)
        else:
            io.output(LED_CHANNEL, True)
        return render_template('home.html', project='Ejemplo GPIO')
    elif request.method == 'GET':
        return render_template('home.html', project='Ejemplo GPIO')
