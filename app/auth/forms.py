"""

AUTOR: Juanjo

FECHA DE CREACIÓN: 24/01/2019

"""

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email, Length


class SignupForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired(), Length(max=64)], render_kw={"placeholder": "nombre"})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={"placeholder": "password"})
    email = StringField('Email', validators=[DataRequired(), Email()], render_kw={"placeholder": "e-mail"})
    submit = SubmitField('Registrar')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()], render_kw={"placeholder": "e-mail"})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={"placeholder": "password"})
    remember_me = BooleanField('Recuérdame')
    submit = SubmitField('Login')
