from src.flaskbasic import db, application

# app schema, database table
class Student(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(50), nullable= False)
  physics = db.Column(db.Integer)
  maths = db.Column(db.Integer)
  chemistry = db.Column(db.Integer)

  def __repr__(self):
    return f"Student('{self.id}', '{self.name}',{self.physics}',{self.maths}',{self.chemistry}')"