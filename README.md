# Python REST API with PostgreSQL
This API manage user tasks
Users can Add, Remove, List and Edit daily tasks

## Pre requisites:
- PostgreSQL
- Python: version 3.9 
- Pip
- Python Virtual environment (venv)

## Steps for run application:
- Copy database script: [db_task.sql](database/db_task.sql)
- Install virtual environment: pip install virtualenv
- Create virtualenvironment: virtualenv venv
- Activate virtual environment: venv/Scripts/activate
- Install all dependencies in [requirements.txt](requirements.txt): pip install -r requirements.txt
- Configure database on: [config.py](config.py)
- Run application: flask run or python app.py
- Access the application with URL: http://localhost:5000
- Users for tests: admin01, admin02, user1, user2, ...
- Passwords for all users: 12345678
- Use Postman for test your API