from manage import db,app

class Name(db.Model):
	__tablename__ = 'names'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), index=True, unique=True)


	def __repr__(self):
		return '<User %r>' % (self.nickname)