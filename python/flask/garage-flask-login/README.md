My complaint about the <a href="http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-v-user-logins">Flask Mega Tutorial Part V: User Logins</a> is that it conflates authentication (IE using OpenId with Google, Yahoo...etc) and authorization (IE having data that is owned by a particular user, and restricting
access to that data.)

In this toy app, the user logs in by typing their email address.   They then only have access to their own data.  You can easily log in another user by typing in another email address.

It uses flask-login to manage the session cookie.


<img src="http://www.samhalperin.com/img/projects/teaching-examples/garage-just-flask-login/login-screenshot.png" width=300 style="border:solid black 1px"></img>
<img src="http://www.samhalperin.com/img/projects/teaching-examples/garage-just-flask-login/garage-screenshot.png" width=300></img>

## Some notes should you want to try to get this running

+ Copy example-env to .env and then use <a href="https://github.com/kennethreitz/autoenv">autoenv</a> to load it. Alternatively run 'source .env' each time you open a new terminal.

+ You will have to make sure the variables in .env are set up in heroku's dashboard as config variables when deploying.

