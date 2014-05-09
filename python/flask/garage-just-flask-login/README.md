My complaint about the <a href="http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-v-user-logins">Flask Mega Tutorial Part V: User Logins</a> is that it conflates authentication (IE using OpenId with Google, Yahoo...etc) and authorization (IE having data that is owned by a particular user, and restricting
access to that data.)

In this toy app, the user logs in by typing their email address.   They then only have access to their own data.  You can easily log in another user by typing in another email address.

It uses flask-login to manage the session cookie.


<img src="http://www.samhalperin.com/img/projects/teaching-examples/garage-just-flask-login/login-screenshot.png" width=300 style="border:solid black 1px"></img>
<img src="http://www.samhalperin.com/img/projects/teaching-examples/garage-just-flask-login/garage-screenshot.png" width=300></img>

## Some notes should you want to try to get this running

+ the requirements.txt for building the virtual environment is one folder up from this readme.

+ I use <a href="https://github.com/kennethreitz/autoenv">autoenv</a> to manage the apps environment variables (like the database
path and the secret key.) 

+ .env pulls in a file called 'secrets' by sourcing it.  This file is .gitignored, so is therefore not included.  Copy example-secrets to secrets, and change the password.

+ I have this set up for the postgres app on a mac.  You should modify the database
url in .env, and create the database in postgres.


