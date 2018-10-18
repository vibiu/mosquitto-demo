import random
import string

from flask import request, current_app

from route.base import account_bp
from model.account import Account
from model import db
from util.response import success, error
from util.pwlib import make_hash


@account_bp.route('', methods=['GET'])
def get_account():
    page = int(request.args.get('page', 1))
    limit = int(request.args.get('limit', 10))
    query = Account.query.paginate(page=page, per_page=limit)
    items, total = query.items, query.total
    data = [
        {
            'username': account.username,
            'super': account.super,
        } for account in items]
    return success(data, total=total)


@account_bp.route('', methods=['POST'])
def post_account():
    """post account

    request: {
        "username": "unam"
        "password": "password"
    }
    """
    json_data = request.get_json()
    username_length = current_app.config['USERNAME_LENGTH']
    password_length = current_app.config['PASSWORD_LENGTH']
    if not json_data or not isinstance(json_data, dict):
        return error(400, 'Json parse error.')
    password = str(json_data.get('password'))
    pwhash = make_hash(password)
    if not password or not valid_password(password, password_length):
        return error(400, 'Password invalid.')
    username = str(json_data.get('username'))
    if username:
        if not valid_password(username, username_length):
            return error(400, 'Username invalid.')
        account = Account.query.filter(Account.username == username).first()
        if account:
            return error(403, 'Account alredy exists.')
        else:
            account = Account(username=username, password=pwhash, super=0)
            db.session.add(account)
            db.session.commit()
    else:
        while 1:
            username = random_username(username_length)
            account = Account.query.filter(
                Account.username == username).first()
            if not account:
                account = Account(username=username, password=pwhash, super=0)
                db.session.add(account)
                db.session.commit()
                break
    data = {
        'username': account.username,
        'super': account.super
    }
    return success(data)


@account_bp.route('/<string:username>', methods=['GET'])
def get_account_name(username):
    username_length = current_app.config['USERNAME_LENGTH']
    if not username or not valid_username(username, username_length):
        return error(400, 'Username invalid.')
    account = Account.query.filter(Account.username == username).first()
    if not account:
        return error(404, 'Account not found.')
    data = {
        'username': account.username,
        'super': account.super
    }
    return success(data)


@account_bp.route('/<string:username>', methods=['DELETE'])
def delete_account_name(username):
    username_length = current_app.config['USERNAME_LENGTH']
    if not username or not valid_username(username, username_length):
        return error(400, 'Username invalid.')
    account = Account.query.filter(Account.username == username).first()
    if not account:
        return error(404, 'Account not found.')
    db.session.delete(account)
    db.session.commit()
    data = {
        'username': account.username,
        'super': account.super
    }
    return success(data)


def random_username(length=4):
    return ''.join(random.choice(string.ascii_letters) for i in range(length))


def valid_username(username, length):
    if len(username) != length:
        return False
    return all([s in string.ascii_letters for s in username])


def valid_password(password, length):
    if len(password) < length:
        return False
    return True
