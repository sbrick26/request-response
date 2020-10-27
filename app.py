
# TODO: Follow the assignment instructions to complete the required routes!
# (And make sure to delete this TODO message when you're done!)

from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def homepage():
    """Shows a greeting to the user."""
    return 'Are you there, world? It\'s me, Ducky!'

@app.route('/penguins')
def penguinpage():
    return "Penguins are cute!"

@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    return f'Wow, {users_animal} is my favorite animal, too!'

@app.route('/dessert/<users_dessert>')
def favorite_dessert(users_dessert):
    return f'How did you know I liked {users_dessert}?'

@app.route('/madlibs/<adjective>/<noun>')
def madlibs(adjective, noun):
    return f'The {noun} is very {adjective} when the {noun} is coding.'

@app.route('/multiply/<number1>/<number2>')
def multiply(number1, number2):
    if number1.isdigit() and number2.isdigit():
        num1 = int(number1)
        num2 = int(number2)
        ans = num1*num2
        return f'{num1} times {num2} is {ans}.'
    return 'Invalid inputs. Please try again by entering 2 numbers!'

# STRECH TIME


@app.route('/sayntimes/<word>/<n>')
def sayntimes(word, n):
    if n.isdigit() == False: 
        return "Invalid input. Please try again by entering a word and a number!"
    times = int(n)
    string = ""
    for i in range(times):
        string += word + ' '
    return string

@app.route('/reverse/<word>')
def reverse(word):
    string = ""
    for i in reversed(range(len(word))):
        string += word[i]
    return string

@app.route('/strangecaps/<word>')
def strangecaps(word):
    string = ''
    for i in range(len(word)):
        if i%2 == 0:
            string += word[i].lower()
        else:
            string += word[i].upper()
    return string

@app.route('/dicegame')
def dicegame():
    randomDice = random.randint(1,6)
    if randomDice == 6:
        return f'You rolled {randomDice}. You won!'
    return f'You rolled {randomDice}. You lost!'

if __name__ == '__main__':
    app.run(debug=True)

