from datetime import datetime
from flask import render_template, session, redirect, url_for
from . import main
from .forms import NameForm
from .. import db
from ..models import User

@main.route('/', methods=['GET','POST'])
def index():
   
    name= None
    form= NameForm()
    #When user navigate the app for 1st time, there is no name
    #After user submits a name, this name can be displayed on website
    if form.validate_on_submit():
    	user = User.query.filter_by(username=form.name.data).first()
    	if user is None:
    	
			user= User(username= form.name.data)
			db.session.add(user)
			session['known']= False
    	else:
    		session['known']= True

    	session['name']= form.name.data
    	
    	form.name.data= ''
    	#The only vaiable in url_for is enpoint, by default, endpoint's name is view 			#function's name
    	return redirect(url_for('.index'))
    #Use GET instead of POST to avoid repeatly submit request
    return render_template('index.html', form=form, name=session.get('name'), known=session.get('known', False), current_time = datetime.utcnow())

