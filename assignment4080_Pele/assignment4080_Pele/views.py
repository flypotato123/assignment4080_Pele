"""
Routes and views for the flask application.
"""
from datetime import datetime
from flask import render_template
from assignment4080_Pele import app
from flask import request

import pandas as pd

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

from assignment4080_Pele.models.forms import ExpandForm
from assignment4080_Pele.models.forms import CollapseForm
from assignment4080_Pele.models.forms import SinglePresidentForm
from assignment4080_Pele.models.forms import AllOfTheAboveForm

from wtforms.fields.html5 import DateField , DateTimeField

from os import path
import io

import matplotlib.pyplot as plt
from matplotlib.figure import Figure

from flask_bootstrap import Bootstrap
bootstrap = Bootstrap(app)
from datetime import datetime
from flask import render_template
from assignment4080_Pele import app
import pandas as pd
import os
from os import path

app.config['SECRET_KEY'] = 'The first argument to the field'

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Pele',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
@app.route('/gallery')
def gallery():
    """Renders the gallery page."""
    return render_template(
        'gallery.html',
        title='Pokemon Gallery',
        year=datetime.now().year,
        message='A gallery with some special Pokemon with special stats.'
    )
@app.route('/data')
def data():
    """Renders the contact page."""
    df = pd.read_csv(path.join(path.dirname(__file__), 'static\\data\\pokemon.csv'))
    

    return render_template(
         
        'data.html',
        title='Data',
        year=datetime.now().year,
        message='Dataset.',

    )
@app.route('/data/obama' , methods = ['GET' , 'POST'])
def obama():

    print("Obama")

    """Renders the about page."""
    form1 = ExpandForm()
    form2 = CollapseForm()
    # df = pd.read_csv(path.join(path.dirname(__file__), 'static\\data\\trump.csv'))
    df = pd.read_csv(path.join(path.dirname(__file__), 'static/data/pokemon.csv'))
    raw_data_table = ''
    
    if request.method == 'POST':
        if request.form['action'] == 'Expand' and form1.validate_on_submit():
            raw_data_table = df.to_html(classes = 'table table-hover')
        if request.form['action'] == 'Collapse' and form2.validate_on_submit():
            raw_data_table = ''

    

    return render_template(
        'obama.html',
        title='Obama',
        year=datetime.now().year,
        raw_data_table = raw_data_table,
        form1 = form1,
        form2 = form2
    )