from flask import Flask
import random



app = Flask(__name__)

random_number = random.randint(0, 9)
print(random_number)


@app.route('/')
def home():
    return "<h1 style='text-align: center'>Guess a number between 0 and 9</h1>" \
        "<div style='text-align: center'>" \
           "<img src='https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExdm9qaDVtaTl1NXhtaHRvZXllMTFhaWQ5cnF1Y3VvZ3I1OTN3endvbSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/njtPBlbYnHAHK/giphy.gif' alt='Kitten' width: 200px style='display: flex, justify-content: center'>" \
               "</div>" \

@app.route("/<int:number>")
def guess_number(number):
    if number < random_number:
        return "<h1 style='text-align: center; color: red'>Too low, try again!</h1>" \
                "<div style='text-align: center'>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif' alt='Kitten' width: 200px style='display: flex, justify-content: center'>" \
                "</div>" 
    elif number > random_number:
        return "<h1 style='text-align: center; color: purple'>Too high, try again!</h1>" \
                "<div style='text-align: center'>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' alt='Kitten' width: 200px style='display: flex, justify-content: center'>" \
                "</div>" 
    else:
        return "<h1 style='text-align: center; color: green'>You found me!</h1>" \
                 "<div style='text-align: center'>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif' alt='Kitten' width: 200px style='display: flex, justify-content: center'>" \
                "</div>" \
        f"<h2 style='text-align: center'>The number was {random_number}</h2>" \

if __name__ == '__main__':
    app.run(debug=True, port=8080)