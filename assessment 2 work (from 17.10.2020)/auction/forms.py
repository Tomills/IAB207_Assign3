
from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileField, FileAllowed
from wtforms.fields import TextAreaField, SubmitField, StringField, PasswordField, IntegerField, SelectField, FileField
from wtforms.validators import InputRequired, Length, Email, EqualTo


# creates the login information
class LoginForm(FlaskForm):
    user_name = StringField("User Name", validators=[
                            InputRequired('Enter user name')])
    password = PasswordField("Password", validators=[
                             InputRequired('Enter user password')])
    submit = SubmitField("Login")

 # this is the registration form


class RegisterForm(FlaskForm):
    user_name = StringField("User Name", validators=[InputRequired()])
    email_id = StringField("Email Address", validators=[
        Email("Please enter a valid email")])
    location = StringField("Address", validators=[InputRequired
                                                  ("Please enter a valid address")])
    number = IntegerField("Contact Number", validators=[InputRequired
                                                        ("Please enter a valid number")])

    # add buyer/seller - check if it is a buyer or seller hint : Use RequiredIf field

    # linking two fields - password should be equal to data entered in confirm
    password = PasswordField("Password", validators=[InputRequired(),
                                                     EqualTo('confirm', message="Passwords should match")])
    confirm = PasswordField("Confirm Password")

    # submit button
    submit = SubmitField("Register")


class SellForm(FlaskForm):

    genre_options = ['Blues', 'Country', 'EDM', 'Hip Hop',
                     'Indie Rock', 'Jazz', 'Pop', 'Rock', 'Techno']

    type_options = ['7-inch', '8-inch', '12-inch']

    ALLOWED_FILE = {'png', 'jpg', 'JPG', 'PNG'}

    item_name = StringField("Record Title", validators=[
                            InputRequired("Please enter a title for the record")])
    item_artist = StringField("Record Artist", validators=[
                              InputRequired("Please enter an artist for the record")])
    item_description = StringField("Record Description", validators=[
                                   InputRequired("Please enter a description for the record")])
    item_genre = SelectField(
        'Record Genre', choices=genre_options, validators=[InputRequired()])
    item_type = SelectField(
        'Record Type', choices=type_options, validators=[InputRequired()])
    item_year = IntegerField("Record Year", validators=[InputRequired
                                                        ("Please enter a Year for the record")])
    item_value = IntegerField("Starting Value", validators=[
        InputRequired("Please enter a starting price for the record")])
    item_image = FileField('Record Image', validators=[
        FileRequired(message='Upload an Image of the record'),
        FileAllowed(ALLOWED_FILE, message='Only supports png, jpg, JPG, PNG')])

    submit = SubmitField("Sell")
