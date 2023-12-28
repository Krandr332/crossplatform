# app.py

from flask import Flask, render_template, request

import random

app = Flask(__name__)

def choose_option(options):
    option_index = random.randint(0, len(options) - 1)
    return options[option_index]

def generate_plot():
    plot_type = choose_option(["PROGRAM", "REPORT", "SPECIAL", "SERIES", "STORY"])
    character_type = choose_option(["SWINGING", "BRILLIANT", "SALTY", "HILARIOUS", "SENSITIVE", "DODDERING", "HENPECKED", "DEDICATED", "THOUGHTFUL", "HEAVY"])
    character = choose_option(['GIRL COWHAND', 'LITTLE BOY', 'SCIENTIST', 'LAWYER', 'TOWN MARSHALL', 'DENTIST', 'BUS DRIVER', 'JUNGLE MAN', 'SECRET AGENT', 'COLLIE'])
    success = choose_option(['A WHIZ', 'A FLOP', 'MEDIOCRE', 'A SUCCESS', 'A DISASTER'])
    activity = choose_option(['SOLVING CRIMES', 'ROPING COWS', 'COOKING HEALTH FOOD', 'PITCHING WOO', 'PROTECTING ECOLOGY', 'HELPING CHILDREN', 'TWO-FISTED DRINKING', 'FIGHTING FIRES', 'HERDING ELEPHANTS', 'WINNING RACES'])
    resolution = choose_option(['RECOVERS THE JEWELS', 'FOILS THE SPIES', 'DESTROYS THE CITY', 'FINDS LOVE', 'SAVES THE ANIMALS', 'CONFESSES', 'DISCOVERS THE SECRET', 'STOPS THE FLOOD', 'HELPS THE DOG', 'MAKES THE SACRIFICE'])

    return {
        'plot_type': plot_type,
        'character_type': character_type,
        'character': character,
        'success': success,
        'activity': activity,
        'resolution': resolution
    }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_plot', methods=['POST'])
def generate_plot_route():
    plot = generate_plot()
    return render_template('generate_plot.html', plot=plot)

if __name__ == '__main__':
    app.run(debug=True, port=8080)
