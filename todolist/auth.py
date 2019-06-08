import functools
from datetime import datetime
from flask import redirect, url_for, session
from flask_dance.contrib.google import google


def get_google_oauth_token():
    """Return the Google OAuth token dict for the current user from Session storage, if it exists there."""
    if 'google_oauth_token' in session:
        return session['google_oauth_token']
    return None


def get_token_expiration_dt(token):
    # This might only work for tokens from Google?
    return datetime.fromtimestamp(token['expires_at'] * 0.001)


def get_authenticated_user_id():
    # TODO
    return


def require_login(func):
    """Basic decorator that checks if user has logged in via Google Sign-in."""
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        if not google.authorized:
            return redirect(url_for("google.login"))
        return func(*args, **kwargs)
    return wrapper_decorator
