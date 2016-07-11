
from app import server
from flask import render_template

@server.route('/')
@server.route('/index')
def index():
    data = {
        'Movies': ['Pulp Fiction', 'Fight Club', 'Terminator'],
        'Series': ['Dexter', 'House MD', 'Breaking Bad', 'Friends']
    }
    return render_template('index.html', media=data)

@server.route('/test')
def test():
    data = {
        'Movies': {
            'The Best': ['Pulp Fiction', 'Fight Club', 'Terminator'],
        },
        'Series': {
            'My Favs': ['Dexter', 'House MD', 'Breaking Bad', 'Friends']
        }
    }
    return render_template('test.html', media=data)
