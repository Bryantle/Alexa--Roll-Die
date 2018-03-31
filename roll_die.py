from flask import Flask, render_template
from flask_ask import Ask, question, session, statement
from random import randint
import logging

app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger('flask_ask').setLevel(logging.DEBUG)

@ask.launch
def launched():
    return question(render_template('start'))

@ask.intent('YesIntent')
def yes():
    number = randint(1,7)
    return statement(render_template('yes', number = number))

@ask.intent('NoIntent')
def no():
    return statement(render_template('no'))

@ask.session_ended
def ender():
    return statement(render_template('end'))

if __name__ == '__main__':
    app.run(debug = True)
