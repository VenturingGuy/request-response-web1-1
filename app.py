from flask import Flask

import random

app = Flask(__name__)

@app.route('/')

def homepage():
    """Shows a greeting to the user."""
    return 'Are you there, world? It\'s me, Ducky!'

@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    """Display a message to the user that changes based on their favorite animal."""
    return f'Wow, {users_animal} is my favorite animal, too!'

@app.route('/dessert/<users_dessert>')
def favorite_dessert(users_dessert):
    """Display a message to the user that changes based on their favorite dessert."""
    return f'How did you know I liked {users_dessert}?'

@app.route('/madlibs/<adjective>/<noun>')
def madlib(adjective, noun):
    """Display a funny story using an adjective and a noun."""
    return f'I couldn\'t make it to class today because of a {adjective} {noun}, honest!'

@app.route('/multiply/<number1>/<number2>')
def multiply(number1, number2):
    """Multiplies and returns the output of the two input numbers."""
    if number1.isdigit() and number2.isdigit():
        return f'{number1} times {number2} is {int(number1) * int(number2)}.'
    else:
        return f'Invalid inputs. Please try again by entering 2 numbers!'

@app.route('/sayntimes/<word>/<n>')
def sayntimes(word, n):
    """Repeats a given word a given amount of times."""
    group_word = ""
    if (type(word) == str ) and (n.isdigit()):
        for i in range (int(n)):
            if i == (int(n)):
                group_word += word
            else:
                group_word += (word + " ")
    else:
        group_word = "Invalid input. Please try again by entering a word and a number!"
    return f'{group_word}'

@app.route('/dicegame')
def dicegame():
    """Rolls a random die, user gets 6 to win."""
    die_roll = random.randint(1, 6)
    message = f'You rolled a {die_roll}. '
    if (die_roll == 6):
        message += "You won!"
    else:
        message += "You lost!"
    return message

if __name__ == '__main__':
    app.run(debug=True)