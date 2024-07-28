from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class QueryForm(FlaskForm):
    query = StringField('Ask me a question:', validators=[DataRequired()])
    submit = SubmitField('Send')
