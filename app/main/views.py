from datetime import datetime
from flask import render_template, session, redirect, url_for, current_app
from flask import render_template, redirect, request, url_for, flash
from . import main
from .forms import NameForm, EditProfileForm
from .. import db
from ..models import User
from flask_login import login_user, login_required, logout_user, current_user

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
    
    
@main.route('/user/<username>')
def user(username):
	user = User.query.filter_by(username=username).first()
	if user is None:
		abort(404)
	return render_template('user.html', user=user)

@main.route('/edit-profile',methods=['GET','POST'])
@login_required
def edit_profile():
	form = EditProfileForm()
	if form.validate_on_submit():
		current_user.name= form.name.data
		current_user.location= form.location.data
		current_user.about_me = form.about_me.data
		db.session.add(current_user)
		flash('Your profile has been updated.')
		return redirect(url_for('.user',username=current_user.username))
	form.name.data=current_user.location
	form.location.data=current_user.location
	form.about_me.data= current_user.about_me
	return render_template('edit_profile.html', form=form)
	
