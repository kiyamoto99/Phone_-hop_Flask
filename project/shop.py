from flask import Blueprint, render_template
from . import db
from flask_login import login_required, current_user
from .models import Product

shop = Blueprint('shop', __name__)


@shop.route('/shop')
def index():
    products = Product.query.all()
    return render_template('shop.html', products = products)

@shop.route('/product/<int:product_id>/')
def product(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template('product.html', product = product)

