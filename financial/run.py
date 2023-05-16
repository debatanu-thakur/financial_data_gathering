# pylint: disable=invalid-name
from flask import Flask
from flask_migrate import Migrate

from app.config import ProdConfig, DevConfig
from app.routes import financial, statistics
from app.models import db

def create_app():

    app = Flask(__name__)
    

    app.logger.info("Service starting")  # pylint: disable=no-member

    config = "development"

    if config == "production":
        app.config.from_object(ProdConfig())
    elif config == "development":
        app.config.from_object(DevConfig())
    else:
        app.logger.info("FLASK_ENV is NUL!!!") # pylint: disable=no-member

    app.register_blueprint(financial, url_prefix='/v1/financials')
    app.register_blueprint(statistics, url_prefix='/v1/statistics')
    db.init_app(app)
    Migrate(app, db, render_as_batch=True)
    return app


if __name__ == '__main__':
    flask_app = create_app()
    flask_app.run(debug=True, port=8000, host='0.0.0.0')
    
