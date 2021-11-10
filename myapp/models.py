from myapp import db

class Cities(db.Model):
	city_name = db.Column(db.String(64), index=True)
	city_rank = db.Column(db.Integer, index=True)
	id = db.Column(db.Integer, primary_key=True)
	is_visited = db.Column(db.Boolean)

	def __repr__(self):
		return f'{self.city_name}'

