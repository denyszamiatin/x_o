import pickle
import os

from flask import Flask, render_template, request


import field as field_
import bot as bot_

app = Flask(__name__)


@app.route('/', methods=['GET', "POST"])
def index():
    message = ''
    try:
        with open("game.pickle", 'rb') as f:
            field = pickle.load(f)
    except FileNotFoundError:
        field = field_.Field()
    bot = bot_.Bot('O')
    if request.method == 'POST':
        x = int(request.form['x'])
        y = int(request.form['y'])
        try:
            field[x, y] = "X"
        except:
            message = 'Cell is occupied'
        if field.is_win('X'):
            os.remove("game.pickle")
            return "You won!"
        if field.is_draw():
            os.remove("game.pickle")
            return "Draw game"
        field[bot.move(field)] = 'O'
        if field.is_win("O"):
            os.remove("game.pickle")
            return "I won!"
        with open('game.pickle', 'wb') as f:
            pickle.dump(field, f)
    return render_template("index.html", field=field, message=message)



if __name__ == '__main__':
    app.run(debug=True)