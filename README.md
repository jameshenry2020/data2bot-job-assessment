# data2bot-job-assessment
## create a virtualenv 

install the requirements
`pip install -r requirements.txt` 

## enter a secret_key 
### in the .env
SECRET_KET=yoursecretkey

### run your tests
`python manage.py test` or
`coverage run manage.py test && coverage report`

## run the application
`python manage.py runserver`

## access swagger documentation
[swagger docs](http://127.0.0.1:8000)

## postman collection for postman docs
open postman 
and import  **data2bot-assessment-api.postman_collection.json** file in the project directory
