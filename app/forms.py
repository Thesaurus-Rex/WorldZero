from flask_wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired


# this is the login form
class LoginForm(Form):
    # This is someone's open ID
    openid = StringField('openid', validators=[DataRequired()])
    # this is weather or not they want to be remembered
    remember_me = BooleanField('remember_me', default=False)
