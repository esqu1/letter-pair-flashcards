from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/cubing/bld/createflashcards')
def flash_card_maker():
    return render_template('create.html')


if __name__ == '__main__':
    app.run(debug=True)
