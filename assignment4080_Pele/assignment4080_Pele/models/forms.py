from datetime import datetime

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms import Form, BooleanField, PasswordField , HiddenField , DateTimeField , IntegerField , DecimalField , FloatField , RadioField
from wtforms import Form, SelectMultipleField , BooleanField
from wtforms import TextField, TextAreaField, SelectField
from wtforms import validators, ValidationError
from wtforms.fields.html5 import DateField

from wtforms.validators import DataRequired
from wtforms.validators import InputRequired




class ExpandForm(FlaskForm):
    submit1 = SubmitField('Expand')
    name="Expand" 
    value="Expand"

class CollapseForm(FlaskForm):
    submit2 = SubmitField('Collapse')
    name="Collapse" 
    value="Collapse"

class PokedexForm(FlaskForm):
    orderby = SelectField('Sort by:' , validators = [DataRequired] , choices=[('Dex', 'Pokedex number'), ('HP', 'Health Points') , ('Attack', 'Attack'),('Defense','Defense'), ('Sp. Attack', 'Special Attack'), ('Sp. Defense','Special Defense'),('Speed','Speed'),('Total','Total')])
    presentby = SelectField('Sort by:' , validators = [DataRequired] , choices=[('Dex', 'Pokedex number'), ('HP', 'Health Points') , ('Attack', 'Attack'),('Defense','Defense'), ('Sp. Attack', 'Special Attack'), ('Sp. Defense','Special Defense'),('Speed','Speed'),('Total','Total')])

    subnmit = SubmitField('הצג')