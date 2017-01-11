from werkzeug.security import generate_password_hash, check_password_hash
from . import db

class Permission:
    FOLLOW = 0x01
    COMMENT = 0x02
    WRITE_ARTICLES = 0x04
    MODERATE_COMMENTS = 0x08
    ADMINISTER = 0x80



class Role(db.Model):
	__tablename__ = 'roles'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), unique=True)
	
	
	#backref add a back reference in the other model in the relationship
	#'User' represents the object-oriented view of the relationship
	users= db.relationship('User', backref='role',lazy='dynamic')
	
	def __repr__(self):
		return '<Role %r>' % self.name
		



class User(db.Model):
	
	__tablename__='users'
	id = db.Column(db.Integer, primary_key=True)
	username= db.Column(db.String(64), unique=True, index=True)
	role_id= db.Column(db.Integer, db.ForeignKey('roles.id'))
	password_hash= db.Column(db.String(128))
	
	@property
	def password(self):
		raise AttributeError('password is not a readable attribute')
		
	@password.setter
	def password(self, password):
		self.password_hash = generate_password_hash(password)
		
	def verify_password(self, password):
		return check_password_hash(self.passowrd_hash, password)
