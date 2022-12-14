from datetime import datetime
from flask_wtf import FlaskForm
import re
from wtforms import StringField, SelectField, SelectMultipleField, DateTimeField, BooleanField, TextAreaField, RadioField
from wtforms.validators import ValidationError, DataRequired, AnyOf, URL, optional, length, Regexp

stateList = [
         ('AL', 'AL'),
         ('AK', 'AK'),
         ('AZ', 'AZ'),
         ('AR', 'AR'),
         ('CA', 'CA'),
         ('CO', 'CO'),
         ('CT', 'CT'),
         ('DE', 'DE'),
         ('DC', 'DC'),
         ('FL', 'FL'),
         ('GA', 'GA'),
         ('HI', 'HI'),
         ('ID', 'ID'),
         ('IL', 'IL'),
         ('IN', 'IN'),
         ('IA', 'IA'),
         ('KS', 'KS'),
         ('KY', 'KY'),
         ('LA', 'LA'),
         ('ME', 'ME'),
         ('MT', 'MT'),
         ('NE', 'NE'),
         ('NV', 'NV'),
         ('NH', 'NH'),
         ('NJ', 'NJ'),
         ('NM', 'NM'),
         ('NY', 'NY'),
         ('NC', 'NC'),
         ('ND', 'ND'),
         ('OH', 'OH'),
         ('OK', 'OK'),
         ('OR', 'OR'),
         ('MD', 'MD'),
         ('MA', 'MA'),
         ('MI', 'MI'),
         ('MN', 'MN'),
         ('MS', 'MS'),
         ('MO', 'MO'),
         ('PA', 'PA'),
         ('RI', 'RI'),
         ('SC', 'SC'),
         ('SD', 'SD'),
         ('TN', 'TN'),
         ('TX', 'TX'),
         ('UT', 'UT'),
         ('VT', 'VT'),
         ('VA', 'VA'),
         ('WA', 'WA'),
         ('WV', 'WV'),
         ('WI', 'WI'),
         ('WY', 'WY'),
     ]

genresList = [
         ('Alternative', 'Alternative'),
         ('Blues', 'Blues'),
         ('Classical', 'Classical'),
         ('Country', 'Country'),
         ('Electronic', 'Electronic'),
         ('Folk', 'Folk'),
         ('Funk', 'Funk'),
         ('Hip-Hop', 'Hip-Hop'),
         ('Heavy Metal', 'Heavy Metal'),
         ('Instrumental', 'Instrumental'),
         ('Jazz', 'Jazz'),
         ('Musical Theatre', 'Musical Theatre'),
         ('Pop', 'Pop'),
         ('Punk', 'Punk'),
         ('R&B', 'R&B'),
         ('Reggae', 'Reggae'),
         ('Rock n Roll', 'Rock n Roll'),
         ('Soul', 'Soul'),
         ('Other', 'Other'),
     ]

class ShowForm(FlaskForm):
    artist_id = StringField(
        'artist_id'
    )
    venue_id = StringField(
        'venue_id'
    )
    start_time = DateTimeField(
        'start_time',
        validators=[DataRequired()],
        default= datetime.today()
    )

class VenueForm(FlaskForm):
    name = StringField(
        'name', validators=[DataRequired()]
    )
    city = StringField(
        'city', validators=[DataRequired()]
    )
    state = SelectField(
        'state', validators=[DataRequired()],
        choices=stateList
    )
    address = StringField(
        'address', validators=[DataRequired()]
    )
    phone = StringField(
        'phone', validators = [DataRequired(), Regexp(r'^\d{3}-\d{3}-\d{4}$', message='phone is not in the correct format: ' + 'xxx-xxx-xxxx')]
    )
    image_link = StringField(
        'image_link'
    )
    genres = SelectMultipleField(
        # TODO implement enum restriction
        'genres', validators=[DataRequired()],
        choices=genresList
    )
    facebook_link = StringField(
        'facebook_link', validators=[URL()]
    )
    website_link = StringField(
        'website_link', validators=[URL()]
    )
    seeking_talent = RadioField(
        'seeking_talent', choices=[(True,'Yes'),(False,'No')], validators=[optional()]
    )
    seeking_description = TextAreaField(
        'seeking_description', validators=[optional(), length(max=250)]
    )

class ArtistForm(FlaskForm):
    name = StringField(
        'name', validators=[DataRequired()]
    )
    city = StringField(
        'city', validators=[DataRequired()]
    )
    state = SelectField(
        'state', validators=[DataRequired()],
        choices=stateList
    )
    phone = StringField(
        
        'phone', validators = [DataRequired(), Regexp(r'^\d{3}-\d{3}-\d{4}$', message='phone is not in the correct format: ' + 'xxx-xxx-xxxx')]
    )
    image_link = StringField(
        'image_link'
    )
    genres = SelectMultipleField(
        # TODO implement enum restriction
        'genres', validators=[DataRequired()],
        choices=genresList
    )
    facebook_link = StringField(
        # TODO implement enum restriction
        'facebook_link', validators=[URL()]
    )
    website_link = StringField(
        'website_link', validators=[URL()]
    )
    seeking_venue = RadioField(
        'seeking_venue', choices=[(True,'Yes'),(False,'No')], validators=[optional()]
    )
    seeking_description = TextAreaField(
        'seeking_description', validators=[optional(), length(max=250)]
    )


