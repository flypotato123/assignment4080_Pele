"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from assignment4080_Pele import app
from assignment4080_Pele.models.LocalDatabaseRoutines import create_LocalDatabaseServiceRoutines

import base64from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvasfrom matplotlib.figure import Figure


from datetime import datetime
from flask import render_template, redirect, request
from assignment4080_Pele.models.Forms import PokedexForm

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd



import json 
import requests

import io
import base64

from os import path

from flask   import Flask, render_template, flash, request
from wtforms import Form, BooleanField, StringField, PasswordField, validators
from wtforms import TextField, TextAreaField, SubmitField, SelectField, DateField
from wtforms import ValidationError

from assignment4080_Pele.models.Forms import ExpandForm
from assignment4080_Pele.models.Forms import CollapseForm

from assignment4080_Pele.models.QueryFormStructure import QueryFormStructure 
from assignment4080_Pele.models.QueryFormStructure import LoginFormStructure 
from assignment4080_Pele.models.QueryFormStructure import UserRegistrationFormStructure 

###from DemoFormProject.Models.LocalDatabaseRoutines import IsUserExist, IsLoginGood, AddNewUser 

app.config['SECRET_KEY'] = 'The first argument to the field'

from flask_bootstrap import Bootstrapbootstrap = Bootstrap(app)


db_Functions = create_LocalDatabaseServiceRoutines() 

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


@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year
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
@app.route('/data/stats' , methods = ['GET' , 'POST'])
def stats():

    print("stats")

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
        'stats.html',
        title='stats',
        year=datetime.now().year,
        raw_data_table = raw_data_table,
        form1 = form1,
        form2 = form2
    )
@app.route('/data/types' , methods = ['GET' , 'POST'])
def types():

    print("types")

    """Renders the about page."""
    form1 = ExpandForm()
    form2 = CollapseForm()
    # df = pd.read_csv(path.join(path.dirname(__file__), 'static\\data\\trump.csv'))
    df = pd.read_csv(path.join(path.dirname(__file__), 'static/data/Perfected.csv'))
    raw_data_table = ''
    
    if request.method == 'POST':
        if request.form['action'] == 'Expand' and form1.validate_on_submit():
            raw_data_table = df.to_html(classes = 'table table-hover')
        if request.form['action'] == 'Collapse' and form2.validate_on_submit():
            raw_data_table = ''

    

    return render_template(
        'types.html',
        title='types',
        year=datetime.now().year,
        raw_data_table = raw_data_table,
        form1 = form1,
        form2 = form2
    )
# -------------------------------------------------------
# Register new user page
# -------------------------------------------------------
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = UserRegistrationFormStructure(request.form)

    if (request.method == 'POST' and form.validate()):
        if (not db_Functions.IsUserExist(form.username.data)):
            db_Functions.AddNewUser(form)
            db_table = ""

            flash('Thanks for registering new user - '+ form.FirstName.data + " " + form.LastName.data )
            # Here you should put what to do (or were to go) if registration was good
        else:
            flash('Error: User with this Username already exist ! - '+ form.username.data)
            form = UserRegistrationFormStructure(request.form)

    return render_template(
        'register.html', 
        form=form, 
        title='Register New User',
        year=datetime.now().year,
        repository_name='Pandas',
        )
# -------------------------------------------------------
# Login page
# This page is the filter before the data analysis
# -------------------------------------------------------
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginFormStructure(request.form)

    if (request.method == 'POST' and form.validate()):
        if (db_Functions.IsLoginGood(form.username.data, form.password.data)):
            flash('Login approved!')
            return redirect('query')
        else:
            flash('Error in - Username and/or password')
   
    return render_template(
        'login.html', 
        form=form, 
        title='Login to data analysis',
        year=datetime.now().year,
        repository_name='Pandas',
        )

@app.route('/query' , methods = ['GET' , 'POST'])
def query():

    print("Query")

    form1 = PokedexForm()
    chart = ""
    orderby="Attack"
    presentby="Defense"
    chart='static/images/chart.png'

    df = pd.read_csv(path.join(path.dirname(__file__), 'static/data/pokemon.csv'))

    if request.method == 'POST':
        orderby = form1.orderby.data
        presentby = form1.presentby.data

        df=df.set_index('Pokemon')

        fig = plt.figure()        ax = fig.add_subplot(111)

        df.plot.scatter(x=orderby,y=presentby, marker='.', ax=ax)
        chart = plot_to_img(fig)
            
    return render_template(
        'query.html',
        chart=chart,
        form1 = form1,
        vari1=orderby,
        vari2=presentby
    )


def plot_to_img(fig):    pngImage = io.BytesIO()    FigureCanvas(fig).print_png(pngImage)    pngImageB64String = "data:image/png;base64,"    pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')    return pngImageB64String




