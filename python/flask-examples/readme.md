#flask-examples

##goal 
write the simplest possible demo apps for flask, slqalchemy, etc..

##installation
1) create a venv using requirements.txt

2) uses autoenv.  If you don't then you will have 
to manually execute the code in each .env file.These are usually used to setup database URI's..etc

3) most modules have a run.py

4) some apps use postgres.  I use the postgres app on a mac.

##Manifest
**calculator**:  a simple 2 variable calculator

**calculator-ajax**: same as above but ajax

**messager-sqllight**:  post a message to the database

**messager-postgress**: postgresql version of above app

**my-garage**: a simple CRUD app, keep track of your sports cars.

**my-garage-wtf**: same app, but use WTF for forms

**profile-browser**: basic flask-login hello world

**profile-browser-droplist**: same app, but don't expose auth url to client.

**flask-sqlalchemy-quickstart**: a hello world for flask-sqlalchemy.  Most of the apps above don't use the flask-sqlalchemy plugin.