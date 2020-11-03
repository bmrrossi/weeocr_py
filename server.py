from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_weeocr():
    return "Hello, WeeOCR user!!!"