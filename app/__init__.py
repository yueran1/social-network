from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from config import config




bootstrap = Bootstrap()
moment = Moment()
db = SQLAlchemy()

def create_app(config_name):
	app = Flask(__name__)
	app.config.from_object(config[config_name])
	config[config_name].init_app(app)
	
	bootstrap.init_app(app)
	moment.init_app(app)
	db.init_app(app)
	
	#attach error page at here
	from .main import main as main_blueprint
	app.register_blueprint(main_blueprint)
	
	from .auth import auth as atuth_blueprint
	app.register_blueprint(auth_blueprint, url_prefix='/auth')
	
	return app
