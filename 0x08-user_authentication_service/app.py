#!/usr/bin/env python3
""" Basic Flask app """

from flask import Flask, jsonify, request, abort, make_response, redirect
from auth import Auth


AUTH = Auth()
app = Flask(__name__)


@app.route('/', methods=['GET'])
def welcome():
    """ returns a message when the route / is requested """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def users():
    """register a user
    """
    email = request.form.get('email')
    password = request.form.get('password')
    if email is None or password is None:
        return None

    try:
        AUTH.register_user(email, password)
        return jsonify({"email": "{}".format(email),
                        "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'])
def login():
    """log the user
    """

    email = request.form.get('email')
    password = request.form.get('password')
    if email is None or password is None:
        return None
    if AUTH.valid_login(email, password):
        SID = AUTH.create_session(email)
        if not SID:
            abort(401)
        resp = make_response(
            jsonify({"email": email, "message": "logged in"}), 200)
        resp.set_cookie("session_id", SID)
        return resp
    else:
        abort(401)


@app.route('/sessions', methods=['DELETE'])
def logout():
    """[Log out]
    """
    sidCocks = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(sidCocks)
    if user is None:
        abort(403)
    else:
        AUTH.destroy_session(user.id)
        return redirect("/")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
