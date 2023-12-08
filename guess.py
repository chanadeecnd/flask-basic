import random

random_number = random.randint(0, 9)
print(random_number)


def guess_num(function):
    high_url = 'https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'
    low_url = 'https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'
    correct_url = 'https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'

    def wrapper(*args, **kwargs):
        number = function(*args, **kwargs)
        print(number)
        if number > random_number:
            color = "purple"
            text = f"<h1 style='color:{color};'>Too high, try again!</h1>"
            url = high_url
        elif number < random_number:
            color = "red"
            text = f"<h1 style='color:{color};'>Too low, try again!</h1>"
            url = low_url
        else:
            color = "green"
            text = f"<h1 style='color:{color};'>You found me!</h1>"
            url = correct_url
        print(f'text = {text}')
        return f'''
        {text}
        <img src={url} />
        '''
    return wrapper
