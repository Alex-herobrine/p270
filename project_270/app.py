# Download the helper library from https://www.twilio.com/docs/python/install
import os
from flask import Flask, request, jsonify, render_template, redirect, url_for
from twilio.rest import Client


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')



@app.route('/login')
def verify_otp():
    username = request.form['username']

    password = request.form['password']

    number = request.form['number']

    if username=='India', password=='08151947':

        AC8af15280d100a962aee20a95f541a905
        53af7dec8ec7704f721ffc9dac5c8653


        verification = client.verify \
            .services('Enter service sid from twilio') \
            .verifications \
            .create(to=enter mobile number variable here, channel='Enter mode of sending otp here')










if __name__ == "__main__":
    app.run()

