from flask import Flask
from flask import jsonify

application = Flask(__name__)


@application.route("/")
def hello():
    """Return a friendly HTTP greeting."""
    print("I am inside hello world")
    return "Continuous Delivery Demo"

@application.route("/cube/<n>")
def cube(n):
    print(f"This was placed in the url: new-{n}")
    val = {f"{n} to the power of 3 =": int(n)**3}
    return jsonify(val)


if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()