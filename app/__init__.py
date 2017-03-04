from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_pagedown import PageDown
from config import config

login_manager= LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
pagedown=PageDown()



bootstrap = Bootstrap()
moment = Moment()
db = SQLAlchemy()

def create_app(config_name):
	app = Flask(__name__)
	app.config.from_object(config[config_name])
	config[config_name].init_app(app)
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= True
	
	bootstrap.init_app(app)
	moment.init_app(app)
	db.init_app(app)
	login_manager.init_app(app)
	
	pagedown.init_app(app)
	
	#attach error page at here
	from .main import main as main_blueprint
	app.register_blueprint(main_blueprint)
	
	from .auth import auth as auth_blueprint
	app.register_blueprint(auth_blueprint, url_prefix='/auth')
	

	return app
