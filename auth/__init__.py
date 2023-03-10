import os

from flask import Flask, render_template


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='top-secret',
        DATABASE=os.path.join(app.instance_path, 'local.db')
    )

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def index():
        return render_template('index.html')

    app.add_url_rule('/', endpoint='index')

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    return app
