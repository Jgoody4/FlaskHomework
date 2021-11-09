from myapp import db

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), index=True, unique=True)
	email = db.Column(db.String(128), index=True, unique=True)
	password_hash = db.Column(db.String(128))

	def __repr__(self):
		return f'<User {self.username}>'

	def check_password(self, password):
		return check_password_hash(self.password_hash, password)

	def set_password(self, password):
		self.password_hash = generate_password_hash(password)

class Cities(db.Model):
	city_name = db.Column(db.String(64), index=True)
	city_rank = db.Column(db.Integer, index=True)
	id = db.Column(db.Integer, primary_key=True)
	is_visited = db.Column(db.Boolean)

	def __repr__(self):
		return f'{self.city_name}'

