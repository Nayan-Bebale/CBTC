from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)


# Function to determine the game result
def game_win(com, you):
    if com == you:
        return None
    elif com == 'r':
        if you == 's':
            return False
        elif you == 'p':
            return True
    elif com == 'p':
        if you == 'r':
            return False
        elif you == 's':
            return True
    elif com == 's':
        if you == 'p':
            return False
        elif you == 'r':
            return True

@app.route('/')
def index():
    result = request.args.get('result')
    com_choice = request.args.get('com_choice')
    your_choice = request.args.get('your_choice')
    return render_template('index.html', result=result, com_choice=com_choice, your_choice=your_choice)

@app.route('/play/<choice>', methods=['GET', 'POST'])
def play(choice):
    choices = {'r': 'rock', 'p': 'paper', 's': 'scissor'}
    com = random.choice(list(choices.keys()))
    you = choice

    com_choice = choices[com]
    your_choice = choices[you]

    game_result = game_win(com, you)

    if game_result is None:
        result = "It's a tie!"
    elif game_result:
        result = "You win!"
    else:
        result = "You lose!"

    return redirect(url_for('index', result=result, com_choice=com_choice, your_choice=your_choice) + '#rock')



if __name__ == '__main__':
    app.run(debug=True)
