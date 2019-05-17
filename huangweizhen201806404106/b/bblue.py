from flask import Blueprint

b_bp = Blueprint('b_bp',__name__)
@b_bp.route('/b',methods =['POST'])
def b():
    return('hello world!')