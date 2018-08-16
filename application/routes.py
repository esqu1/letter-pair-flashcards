from application import app
from flask import render_template, request, abort
import requests
import os


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/cubing/bld/gen_token')
def gen_token():
    secret_string = request.args.get('state')
    code = request.args.get('code')
    if secret_string != os.environ.get('LETTERPAIRSECRETSTATE'):
        abort(404)

    r = requests.post(
        'https://api.quizlet.com',
        headers={
            'Authorization':
            'Basic %s' % os.environ.get('LETTERSPAIRSECRETENCODED')
        },
        data={
            'grant_type': 'authorization_code',
            'code': code
        })
    # create a new token, then redirect to new webpage (Below)


@app.route('/cubing/bld/createflashcards')
def flash_card_maker():
    return render_template('create.html')
