# Load environment variables from .env file (needed for gunicorn)
from dotenv import load_dotenv
load_dotenv()

import os
from flask import Flask, render_template
from todo import todo_bp, init_app as init_todo
from todo import db


SITE = {
    "WebsiteName": "TodoApp",
    "ControllerName": "UTC Sheffield Olympic Legacy Park",
    "ControllerAddress": "UTC Sheffield Olympic Legacy Park, 2 Old Hall Road"
    + ", Sheffield, S9 3TU",
    "ControllerURL": "https://www.utcsheffield.org.uk/olp/",
}

def create_app(config_overrides=None):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
        'DATABASE_URL',
        'sqlite:///todo.db'
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    if config_overrides:
        app.config.update(config_overrides)

    # Register blueprints
    app.register_blueprint(todo_bp)

    @app.context_processor
    def inject_dict_for_all_templates():
        return {"site": SITE}

    @app.route('/privacy')
    def privacy():
        return render_template('privacy.html')

    # Initialize todo module (db and tables)
    init_todo(app)

    return app


app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
