import os

import oauthlib
from flask import (
    Flask,
    render_template, request, redirect, url_for, session, current_app
)

from flask_dance.contrib.google import make_google_blueprint, google

# oauth
from oauthlib.oauth2.rfc6749.errors import InvalidClientIdError, TokenExpiredError
# os.environ
from dotenv import load_dotenv

from scripts import invoke_lambda

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
load_dotenv()


def _empty_session():
    """
    Deletes the Google token and clears the session
    """
    if "google" in current_app.blueprints and hasattr(
            current_app.blueprints["google"], "token"
    ):
        del current_app.blueprints["google"].token
    session.clear()


app = Flask(__name__)
app.config["SECRET_KEY"] = "qwertyasdfgh123#"

back_home = os.environ.get("BACK_HOME")
google_bp = make_google_blueprint(
    client_id=os.getenv("GOO_CLIENT"),
    client_secret=os.getenv("GOO_SHH"),
    scope=[
        "https://www.googleapis.com/auth/userinfo.email",
        "openid",
        "https://www.googleapis.com/auth/userinfo.profile",
    ],
    redirect_to="landing_page",
)

app.register_blueprint(google_bp, url_prefix="/login")


@app.errorhandler(oauthlib.oauth2.rfc6749.errors.TokenExpiredError)
@app.errorhandler(oauthlib.oauth2.rfc6749.errors.InvalidClientIdError)
def token_expired(_):
    _empty_session()
    return redirect(url_for("login"))


@app.route('/foo', methods=['GET', 'POST'])
def foo():
    value = request.form.get('lambda_selector')
    if value == "b1":
        invoke_lambda.run_lambda1()
    elif value == "b2":
        invoke_lambda.run_lambda2()
    elif value == "b3":
        invoke_lambda.run_lambda3()
    elif value == "b4":
        invoke_lambda.run_lambda4()
    elif value == "b5":
        invoke_lambda.run_lambda5()
    elif value == "b6":
        invoke_lambda.run_lambda6()
    elif value == "b7":
        invoke_lambda.run_lambda7()
    elif value == "b8":
        invoke_lambda.run_lambda8()
    elif value == "b9":
        invoke_lambda.run_lambda9()
    else:
        pass

    print(str(value))  # just to see what was selected

    return render_template('index.html')


@app.route('/', methods=["GET", "POST"])
def landing_page():
    if not google.authorized:
        return redirect(url_for("google.login"))

    listStatus = [('cpp', 'C++'), ('py', 'Python'), ('text', 'Plain Text')]
    default = 'cpp'
    return render_template('index.html', listStatus=listStatus, default=default)


if __name__ == '__main__':
    app.run()
