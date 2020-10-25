# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, redirect, url_for
import requests

blueprint = Blueprint('home', __name__)


@blueprint.route('/results', methods=['POST'])
def results():
    veggies = request.form['a']
    fruits = request.form['collapseTwo']
    chicken = request.form['collapseThree']
    beef = request.form['collapseFour']
    milk = request.form['collapseFive']
    cheese = request.form['collapseSix']
    bagels = request.form['collapseSeven']
    bread = request.form['collapseEight']

    vegTotal = veggies * .67
    fruitTotal = fruits * .71
    chickenTotal = chicken * 1.54
    beefTotal = beef * 4.08
    milkTotal = milk * 3.45
    cheeseTotal = cheese * 4.27
    breadTotal = bread * 2.08

    total = vegTotal + fruitTotal + chickenTotal + beefTotal + milkTotal + cheeseTotal + breadTotal

    # if not 'access_token' in session:
    #     flash('Please sign in with your GitHub account.', 'danger')
    #     return redirect(url_for('github.fetching'))
    #
    # github = GitHub(access_token=session['access_token'])
    # github.delete('/user/starred/' + repo)

    return redirect(url_for('tutorial.fetching'))


@blueprint.route('/')
def index():
    # Search GitHub's repositories for requests
    response = requests.get(
        'https://api.github.com/search/repositories',
        params={'q': 'requests+language:python'},
    )

    # Inspect some attributes of the `requests` repository
    json_response = response.json()
    repository = json_response['items'][0]

    return render_template('home/index.html', helpfuldata=repository["description"])


@blueprint.route('/result')
def result():
    return render_template('home/result.html')


@blueprint.route('/result')
def total():
    if request.method == 'POST':
        answer = request.form
    return render_template("home/result.html", total=answer)



