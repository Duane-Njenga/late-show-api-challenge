from flask import Flask
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from server.models import db
from server.config import Config


    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    Migrate(app, db)
    JWTManager(app)

    from server.controllers import auth_controller, guest_controller, episode_controller, appearance_controller
    app.register_blueprint(auth_controller.bp)
    app.register_blueprint(guest_controller.bp)
    app.register_blueprint(episode_controller.bp)
    app.register_blueprint(appearance_controller.bp)

    return app


if __name__ == '__main__':
    app.run(debug=True)
