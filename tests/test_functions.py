from flask_sqlalchemy import SQLAlchemy
from src.flaskbasic.functions import functions
import pytest

fun = functions

def test_student_name():

    assert fun.readName('Lwando',1) == 'Lwando'

def test_all_results():
    assert fun.readResults(1, 'Lwando',10,60,10) == (1, 'Lwando', 10, 60, 10)

    assert fun.readName('Lwando',6) == 'Lwando'

def test_all_results():
    assert fun.readResults(6, 'Lwando',50,60,90) == (6, 'Lwando', 50, 60, 90)


    
    
	

		