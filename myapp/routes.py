from myapp import myobj
from myapp import db
from myapp.forms import TopCities
from myapp.models import Cities
from flask import render_template, flash, redirect

@myobj.route("/")
def home():
	"""Return H1 header that says welcome!
	"""
	return render_template("main.html")

@myobj.route("/hi")
def hi():
	return "Hi!"

@myobj.route("/main")
def main():
	date = '2021-10-05'
	users = {'username' : 'carlos'}

	post = [ {'author': 'John', 'body': 'Beatiful day in Portland!'},\
		{ 'author': 'Susan', 'body': 'The dat is cloudy today!'}]

	return render_template('hello.html', users=users, datee=date, post=post)

@myobj.route("/home")
def home_top_cities():
	title = 'Top Cities'
	name = 'Justin'
	form = TopCities()
	if form.validate_on_submit():
		flash(f'City name: {form.city_name.data}, with city rank: {form.city_rank.data}')
		city_name = form.city_name.data
		city_rank = form.city_rank.data
		cities = Cities(city_name=city_name, city_rank=city_rank, is_visted = form.is_visted.data)
		db.session.add(cities)
		db.session.commit()
		return redirect('/home')
	top_cities = Cities.query.order_by(Cities.city_rank).all()
	return render_template('home.html', title=title, name=name, form=form, top_cities=top_cities)
