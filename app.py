from flask import Flask, render_template, jsonify

app = Flask(__name__)

music_data = {
    'Happy & Uplifting': {
        'Pop': ['Bruno Mars', 'Dua Lipa'],
        'Electronic': ['Zedd', 'David Guetta']
    },
    'Sad & Melancholic': {
        'Ballad': ['Bille Eilish', 'John Legend'],
        'Lo-fi': ['Mac DeMarco', 'Yot Club']
        
    },
    'Motivated & Empowering': {
        'Hip Hop': ['Kendrick Lamar', 'MF Doom'],
        'Rock': ['Queen', 'AC/DC']
        
    },
    'Relaxed & Chill': {
        'Ambient': ['Brian Eno', 'Max Richter'],
        'Jazz': ['Chet Baker', 'Nina Simone']
        
    },
    'Romantic': {
        'Soul': ['Wilie Dixon', 'John Lee Hooker'],
        'Jazz': ['Lou Donaldson', 'Bill Evans Trio']
        }
}

@app.route('/')
def index():
    return render_template('index.html', music_data=music_data)

if __name__ == '__main__':
    app.run(debug=True)
