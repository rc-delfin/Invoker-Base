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
open_gate = os.environ.get("OPEN_GATE")

app.register_blueprint(google_bp, url_prefix="/login")

lambdas = [{"b1": "Account expires"},
           {"b2": "OneCG fields"},
           {"b3": "Account Request"},
           {"b4": "OneCG 2 attribs"},
           {"b5": "Multiple CSVs for AD"},
           {"b6": "Country holidays"},
           {"b7": "Change in POSNO"},
           {"b8": "Funding Opportunities"},
           {"b9": "AB webprofiles updates"}]


@app.errorhandler(oauthlib.oauth2.rfc6749.errors.TokenExpiredError)
@app.errorhandler(oauthlib.oauth2.rfc6749.errors.InvalidClientIdError)
def token_expired(_):
    _empty_session()
    return redirect(url_for("login"))


@app.route('/foo', methods=['GET', 'POST'])
def foo():
    if not google.authorized:
        return redirect(url_for("landing_page"))

    value = request.form.get('lambda_selector')
    if value:
        invoke_lambda.run_lambda(value)

    print("Value: " + str(value))  # just to see what was selected
    return render_template('index.html', lambdas=lambdas)


@app.route('/', methods=["GET", "POST"])
def landing_page():
    if not google.authorized:
        return redirect(url_for("google.login"))

    resp = google.get("/oauth2/v2/userinfo")
    assert resp.ok, resp.text
    email = resp.json()["email"]

    print(email)  # debug code, can be removed
    print(open_gate)  # debug code, can be removed

    if email in open_gate:
        return render_template('index.html', lambdas=lambdas)

    return "<h1>Forbidden: Unauthorized Access</h1>", 403


if __name__ == '__main__':
    app.run()
