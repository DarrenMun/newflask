<<<<<<< HEAD
# from flask_sqlalchemy import SQLAlchemy
=======
from flask_sqlalchemy import SQLAlchemy
>>>>>>> 5b3d37d81e2f843309a86fefc8d50e1a72b24128
# from flaskbasic.wsgi import *
from src.flaskbasic.functions import Functions
import pytest

fun = Functions

def test_student_name():
    assert fun.readName('Lwando',1) == 'Lwando'
    assert fun.readName('Zukisa',2) == 'Zukisa'
    assert fun.readName('ludwe',3) == 'ludwe'

<<<<<<< HEAD
def test_all_results():
    assert fun.readResults(1, 'Lwando',10,60,10) == (1, 'Lwando', 10, 60, 10)
=======
def delete(student_id):
            student_results = Student.query.get_or_404(student_id)
            db.session.delete(student_results)
            db.session.commit() 

def test_all_results():
    assert fun.readResults(1,'Lwando',10, 60, 10 ) == (1, 'Lwando', 10, 60, 10) 
    assert fun.readResults(2,'Zukisa',10, 60, 5) == (2,'Zukisa',10, 60, 5)
    assert fun.readResults(3,'ludwe',32, 12, 22) == (3,'ludwe',32, 12, 22)




# def test_all_results():
#     assert fun.readResults(1, 'Lwando',10,60,10) == (1, 'Lwando', 10, 60, 10)
#     assert fun.readResults(2, 'Zukisa',10,60,5) == (2, 'Zukisa',10,60,5)
    # assert fun.readResults(1, 'Zikia',10,60,10) == (1, 'Lwando', 10, 60, 10)
>>>>>>> 5b3d37d81e2f843309a86fefc8d50e1a72b24128

    
    
	

		