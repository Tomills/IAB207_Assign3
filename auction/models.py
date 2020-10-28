from datetime import datetime
from . import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True, unique=True, nullable=False)
    emailid = db.Column(db.String(100), index=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    contact_number = db.Column(db.Integer, nullable=False)
    address = db.Column(db.String(255), nullable=False)

    items = db.relationship('Item', backref='users')
    watchlists = db.relationship('Watchlist', backref='users')
    bids = db.relationship('Bid', backref='users')


class Item(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True, nullable=False)
    description = db.Column(db.String(200), nullable=False)
    artist = db.Column(db.String(100), index=True, nullable=False)
    genre = db.Column(db.String(80), index=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    designation = db.Column(db.String(80), nullable=False)
    image = db.Column(db.String(400), nullable=False)
    starting_value = db.Column(db.Integer, nullable=False)
    current_value = db.Column(db.Integer, nullable=False)
    bid_number = db.Column(db.Integer, nullable=True)
    status = db.Column(db.String(80), index=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    date_posted = db.Column(db.String, nullable=False)

    watchlists = db.relationship('Watchlist', backref='items')
    bids = db.relationship('Bid', backref='items')

    def __repr__(self):  # string print method
        return "<Name: {}>".format(self.name)


class Watchlist(db.Model):
    __tablename__ = 'watchlists'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'))
    date_added = db.Column(db.DateTime, default=datetime.now())

    def __repr__(self):  # string print method
        return "<Name: {}>".format(self.item_id)


class Bid(db.Model):
    __tablename__ = 'bids'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'))
    bid_amount = db.Column(db.Integer, nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.now())

    def __repr__(self):  # string print method
        return "<Bid: {}>".format(self.bid_amount)
