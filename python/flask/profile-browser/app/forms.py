from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, SelectField
from wtforms.validators import Required

class LoginForm(Form):
    oid_provider = SelectField(u'OpenId Provider', choices=[
        ('google', 'Google'), 
        ('yahoo', 'Yahoo'), 
        ('aol', 'AOL'), 
        ('flickr', 'Flickr'), 
        ('myOpenId', 'My Open Id')])
    remember_me = BooleanField('remember_me', default = False)
    
