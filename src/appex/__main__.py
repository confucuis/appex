import flask

from appex import user


def main():
    app = flask.Flask(__name__)

    app.register_blueprint(user.bp)

    app.run(host="0.0.0.0", port=8885)


if __name__ == "__main__":
    main()
