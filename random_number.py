from flask import Flask
from guess import guess_num

app = Flask(__name__)


@app.route('/')
def home_page():
    gif_url = 'https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'
    return f'''
    <h1>Guess a number between 0 and 9</h1>
    <img src={gif_url}>
    '''


@app.route('/<int:number>')
@guess_num
def guess_number(number):
    return number


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
