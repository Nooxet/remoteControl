
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
        'Series': {
            'MyFavs': {
                'Dexter': ['Dexter - S01E01 - Pilot.mp4', 'Dexter - S01E02 - During The Darkest Night.mkv', '3'],
                'BreakingBad': ['1', '2', '3'],
                'House': ['1', '2', '3']
            },
            'MyFavs2': {
                'Dexter': ['Dexter - S01E01 - Pilot.mp4', 'Dexter - S01E02 - During The Darkest Night.mkv', '3'],
                'BreakingBad': ['1', '2', '3'],
                'House': ['1', '2', '3']
            }
        }
    }
    return render_template('test.html', media=data)
