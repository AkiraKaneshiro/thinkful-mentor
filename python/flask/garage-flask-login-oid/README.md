In this version of the app, I've added OID support so that the user
can login with Google and Yahoo.

## Some notes should you want to try to get this running

+ Copy example-env to .env and then use <a href="https://github.com/kennethreitz/autoenv">autoenv</a> to load it. Alternatively run 'source .env' each time you open a new terminal.

+ You will have to make sure the variables in .env are set up in heroku's dashboard as config variables when deploying.

