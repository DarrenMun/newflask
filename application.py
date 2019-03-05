from src.flaskbasic import application ,db
from src.flaskbasic.form import *

# runs the application

if __name__ == '__main__':                     
	application.run(debug=True)