from flask import Flask

app = Flask(__name__)
port = 5000


def make_bold(function):
    def return_make(*args, **kwargs):
        result = function(*args, **kwargs)
        return f"<strong>{result}</strong>"
    return return_make


@app.route('/')
def hello_world():
    return "Hello World!"


@app.route('/username/<name>')
@make_bold
def greet(name):
    return f"Hello {name}"


@app.route('/add/<int:input1>/<int:input2>')
def add(input1, input2):
    result = input1 + input2
    return f"Result = {result}"


@app.route('/cat/<name>')
def cat(name):
    url = ('https://media3.giphy.com/media/3oriO0OEd9QIDdllqo/giphy.gif?cid'
           '=ecf05e47f988spy9w350b45i0w1czupq4ad3lu9scssybh0j&ep=v1_gifs_search&rid=giphy.gif&ct=g')
    return f'''<h1>Hello meow~ {name}</h1>
                <h4>{name}</h4>
                <img src={url} />
            '''


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=port)

# command: flask --app hello --debug run
