from myapp import myobj
from myapp import db
from myapp.forms import TopCities
from myapp.models import Cities
from flask import render_template, flash, redirect

@myobj.route("/", methods=['GET', 'POST'])
def home_top_cities():
	title = 'Top Cities'
	name = 'Justin'
	form = TopCities()
	if form.validate_on_submit():
		flash(f'City name: {form.city_name.data}, with city rank: {form.city_rank.data}')
		city_name = form.city_name.data
		city_rank = form.city_rank.data
		cities = Cities(city_name=city_name, city_rank=city_rank, is_visited = form.is_visited.data)
		db.session.add(cities)
		db.session.commit()
		return redirect('/')
	top_cities = Cities.query.order_by(Cities.city_rank).all()
	return render_template('home.html', title=title, name=name, form=form, top_cities=top_cities)
