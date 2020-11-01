from flask import Blueprint, render_template, request, redirect, url_for
from .models import Item, Watchlist
from . import db


bp = Blueprint('items', __name__, url_prefix='/items')

@bp.route('/<id>')
def show(id):
    if (id != "All"):
        filteredItems = Item.query.filter_by(genre=id)
    else:
        filteredItems = Item.query.all()
        id += " Genres"
    return render_template('items_filtered.html', filteredItems=filteredItems, title=id)


#testing thing for watchlist.
# @bp.route('/<id>', methods = ['GET', 'POST'])
# def watchist(id):
#     wl_form = AddToWatchlistForm()
#     del_form = RemoveFromWatchlistForm()

#alreadyOnWatchlist = watchlist.query.filter_by(user_id = current_user.get_id())