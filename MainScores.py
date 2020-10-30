from flask import Flask

import Utils

app = Flask(__name__)


@app.route('/')
def score_server():
    try:
        score = open("Scores.txt", "r")
    except BaseException as e:
        return """<html>
        <head>
            <title>Scores Game</title>
        </head>
        <body>
        <body>
            <h1><div id="score" style="color:red">""" + Utils.BAD_RETURN_CODE + str(e) + """</div></h1>
        </body>
        </html>
        """
    return """
    <html>
        <head>
            <title>Scores Game</title>
        </head>
        <body>
        <h1>
        <p style="color:blue;">Your score is <div id="score">""" + str(score.readline()) + """</div></p>
        </h1>
        </body>
    </html>"""
