from ..controller.propertiesClass import *
from ..controller.pathClass import bodyMailText

## SMTP Server
gmailHost = {'host': 'smtp.gmail.com',
             'port': 587}
## Settings
properties = Properties()
def getObject(path, mode = 'rb'):
    return open(path, mode).read()

## Loggin Server
user = properties.email()
password = properties.password()

## Mail Settings
fromEmail = user
toEmail = user
subject = 'g30Loc - Ubicacion'
body = getObject(bodyMailText,'r')

