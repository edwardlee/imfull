# -*- coding: utf-8 -*-
from flask import Blueprint, render_template
import requests
blueprint = Blueprint('home', __name__)




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
