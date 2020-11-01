from flask import (
    Blueprint, flash, render_template, request, url_for, redirect, session, g,
)
from werkzeug.security import generate_password_hash, check_password_hash
# from .models import User
from .forms import LoginForm, RegisterForm, SellForm, BidForm
from flask_login import login_user, login_required, logout_user, current_user
from . import db
from .models import User, Item, Bid, Watchlist
import os
from werkzeug.utils import secure_filename
import datetime
from datetime import datetime

# create a blueprint
bp = Blueprint('auth', __name__)
bp2 = Blueprint('item', __name__, url_prefix='/item')


#-- Watchlist Data 
@bp.route("/watchlist")
@login_required
def watchlist():
    user_id = current_user.get_id()
    watchlist = Watchlist.query.with_entities(Watchlist.id, Watchlist.date_added, Item.current_value, Item.bid_number, Item.status, Item.image).filter_by(user_id=user_id).join(Item).order_by(Watchlist.date_added)
    
    return render_template('watchlist.html', watchlist=watchlist)


# -- Populating the Watchlist
@bp.route("/watchlist/<id>/add")
@login_required
def watchlist_add(id):
    user_id = current_user.get_id()
    item_obj = id
    time = datetime.now()

    new_watchlist = Watchlist(user_id=user_id, item_id=item_obj, date_added=time)
    db.session.add(new_watchlist)
    db.session.commit()

    return redirect("/")


# -- Removing item from the Watchlist
@bp.route("/watchlist/<id>/del")
@login_required
def watchlist_del(id):
    watchlist_id = id

    rem_watchlist = Watchlist.query.filter_by(id=watchlist_id).first()
    db.session.delete(rem_watchlist)

    db.session.commit()

    return redirect("/watchlist")


# -- Removing item from the Watchlist from Index page
@bp.route("/indexwatchlist/<id>/del")
@login_required
def indexwatchlist_del(id):
    watchlist_id = id

    rem_watchlist = Watchlist.query.filter_by(id=watchlist_id).first()
    db.session.delete(rem_watchlist)

    db.session.commit()

    return redirect("/")

    


@bp.route("/item_details")
def item_details():
    return render_template('item_details.html')


@bp2.route("/<id>")
def show(id):
    form = BidForm()
    details = Item.query.filter_by(id=id).first()
    return render_template('created_item_details.html', details=details, form=form)


@bp.route("/error")
def error():
    return render_template('error_view.html')


# this is the hint for a login function


@bp.route('/login', methods=['GET', 'POST'])
def authenticate():  # view function
    print('In Login View function')
    login_form = LoginForm()
    error = None
    if(login_form.validate_on_submit() == True):
        user_name = login_form.user_name.data
        password = login_form.password.data
        u1 = User.query.filter_by(name=user_name).first()
        if u1 is None:
            error = 'Incorrect user name'
        # takes the hash and password
        elif not check_password_hash(u1.password_hash, password):
            error = 'Incorrect password'
        if error is None:
            login_user(u1)
            # this gives the url from where the login page was accessed
            # nextp = request.args.get('next')
            # print(nextp)
            # if next is None or not nextp.startswith('/'):
            return redirect(url_for('main.index'))
            # return redirect(nextp)
        else:
            flash(error)
    return render_template('user.html', form=login_form, heading='Login')


@bp.route('/register', methods=['GET', 'POST'])
def register():
    register = RegisterForm()
    # the validation of form submis is fine
    if (register.validate_on_submit() == True):
        # get username, password and email from the form
        uname = register.user_name.data
        pwd = register.password.data
        email = register.email_id.data
        contact = register.number.data
        address = register.location.data
        # check if a user exists
        u1 = User.query.filter_by(name=uname).first()
        if u1:
            flash('User name already exists, please login')
            return redirect(url_for('auth.register'))
        # don't store the password - create password hash
        pwd_hash = generate_password_hash(pwd)
        # create a new user model object
        new_user = User(name=uname, password_hash=pwd_hash,
                        emailid=email, contact_number=contact, address=address)
        db.session.add(new_user)
        db.session.commit()
        # commit to the database and redirect to HTML page
        return redirect(url_for('main.index'))
    # the else is called when there is a get message
    else:
        return render_template('user.html', form=register, heading='Register')


def check_upload_file(form):
    fp = form.item_image.data
    filename = fp.filename
    BASE_PATH = os.path.dirname(__file__)
    upload_path = os.path.join(BASE_PATH, 'static/images',
                               secure_filename(filename))
    db_upload_path = '/static/images/' + secure_filename(filename)
    fp.save(upload_path)
    return db_upload_path


@bp.route('/sell', methods=['GET', 'POST'])
@login_required
def sell():
    Sell_Form = SellForm()
    if (Sell_Form.validate_on_submit() == True):
        db_file_path = check_upload_file(Sell_Form)
        # get username, password and email from the form
        title = Sell_Form.item_name.data
        band = Sell_Form.item_artist.data
        symmary = Sell_Form.item_description.data
        group = Sell_Form.item_genre.data
        size = Sell_Form.item_type.data
        release = Sell_Form.item_year.data
        bid = Sell_Form.item_value.data
        num = 0
        picture = db_file_path
        auction = 'OPEN'
        lister = current_user.get_id()
        today = datetime.now()

        # create a new user model object
        new_item = Item(name=title, description=symmary, artist=band, genre=group, year=release,
                        designation=size, image=picture, starting_value=bid, current_value=bid, bid_number=num, status=auction, user_id=lister, date_posted=today)
        db.session.add(new_item)
        db.session.commit()

        # commit to the database and redirect to HTML page
        return redirect(url_for('main.index'))
    # the else is called when there is a get message
    else:
        return render_template('user.html', form=Sell_Form, heading='Sell')


@bp.route('/item/<id>/bid', methods=['GET', 'POST'])
@login_required
def bid(id):
    form = BidForm()
    print("running......")
    bidder = current_user.get_id()
    item_obj = id
    bid = form.value.data
    time = datetime.now()
    item_update = Item.query.get(id)

    if form.validate_on_submit():
        if bid > item_update.current_value:
            new_bid = Bid(user_id=bidder, item_id=item_obj,
                          bid_amount=bid, date_added=time)
            db.session.add(new_bid)

            count = item_update.bid_number
            item_update.current_value = bid
            item_update.bid_number = count + 1

            db.session.commit()
            print('Your comment has been added', 'success')
            return redirect(url_for('item.show', id=id))
        else:
            flash('bid must be higher than current value')
            return redirect(url_for('item.show', id=id))
    else:
        flash('bid must be higher than current value')
        return redirect(url_for('item.show', id=id))


@ bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))
