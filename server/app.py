from flask import Flask
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from models import db
from config import Config
from controllers import blueprints

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
Migrate(app, db)
JWTManager(app)


for bp in blueprints:
    app.register_blueprint(bp)



if __name__ == '__main__':
    app.run(debug=True)
