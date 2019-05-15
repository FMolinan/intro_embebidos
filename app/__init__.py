from flask import Flask, jsonify, render_template, request
import RPi.GPIO as io

app = Flask(__name__)

LED_CHANNEL = 7
io.setmode(io.BOARD)
io.setup(LED_CHANNEL, io.OUT)

@app.route("/")
def home():
    if request.method == 'POST':
        if io.input(LED_CHANNEL):
            io.ouput(LED_CHANNEL, False)
        else:
            io.output(LED_CHANNEL, True)
    elif request.method == 'GET':
        return render_template('home.html', project='Ejemplo GPIO')
