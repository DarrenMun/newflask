from flask import Flask,render_template, redirect, url_for,request, jsonify, abort,request
from flask_sqlalchemy import SQLAlchemy
from src.flaskbasic import *
from src.flaskbasic.form import StudentForm

# Schema of the project or table, it  is how the data is structured
class Student(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(50), nullable= False)
  physics = db.Column(db.Integer)
  maths = db.Column(db.Integer)
  chemistry = db.Column(db.Integer)

# Route that first renders the page when the page loads, get route that gets the data from the database,
# post route that sends data to the database

@application.route('/', methods=['GET','POST'])
def add_results():
    form = StudentForm()
    if form.validate_on_submit():
      student = Student(name=form.name.data, physics=form.physics.data, maths=form.maths.data,chemistry=form.chemistry.data,)
      db.session.add(student)
      db.session.commit()
      return redirect(url_for('add_results'))
    else:
      return render_template('home.html', form=form)


# get route that gets all the data from the database and renders a template with results

@application.route('/results', methods=['GET','POST'])
def get_results():
  data = Student.query.all()
  return render_template('results.html', data = data)

# PUT route updates the existing data in the database
@application.route('/results/<int:indexId>', methods=['PUT'])
def update_results(indexId):
  
  student = Student.query.filter_by(id = indexId).first()

  if not student:
    return jsonify({'message' : 'No Student found'})

  student.name = request.json['name']
  student.physics = request.json.get('physics', "")
  student.maths = request.json.get('maths', "")
  student.chemistry = request.json.get('chemistry', "") 
  db.session.commit()
  
  return jsonify({'student':'Pass'})

# Delete route deletes an existing data in the database 

@application.route('/results/<int:indexId>', methods=['DELETE'])
def delete_student(indexId):

  student = Student.query.filter_by(id = indexId).first()

  if not student:
    return jsonify({'message':'No user found'})

  db.session.delete(student)
  db.session.commit()

  return jsonify({'message':'Student found and Deleted'})


