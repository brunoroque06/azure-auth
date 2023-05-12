import jwt
from flask import Flask, abort, request

app = Flask(__name__)


@app.route("/")
def hello_world():
    if "Authorization" not in request.headers:
        abort(403)
    token = request.headers["Authorization"].split()[1]
    alg = jwt.get_unverified_header(token)["alg"]
    decoded = jwt.decode(token, algorithms=[alg], options={"verify_signature": False})
    return f"Hello {decoded['name']}. I know your email: {decoded['email']}."
