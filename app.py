import os
from flask import Flask, send_file, request, redirect, url_for, render_template
from twilio.rest import Client

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('home.html')

if __name__ == "__main__":
    app.run()



