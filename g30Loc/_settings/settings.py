from datetime import datetime

dateTimeFormat = "%Y%m%d%H%M%S"
def formatFile(fileName, formatFile):
    return "{}.{}".format(fileName,formatFile)
def getDate():
    return datetime.strftime(datetime.today(),dateTimeFormat)

## Folders
settingsFolder = "_settings"
mediaFolder = "_media"

## Files
propertiesFileName = "properties"
ymlFormat = "yml"

mediaFileName = "screenshot{date}".format(date=getDate())
pngFormat = "png"

bodyMailFileName = "bodyMail"
txtFormat = "txt"

properties = formatFile(propertiesFileName,ymlFormat)
media = formatFile(mediaFileName,pngFormat)
bodyMail = formatFile(bodyMailFileName,txtFormat)

## properties fields
key_ = 'key'
url_ = 'url'
ubi_ = 'ubicacion'
tred_ = 'tarjeta-red'
email_ = 'email'
pass_ = 'pass'

## position
location = 'location'
latitude = 'lat'
longitude = 'lng'
accuracy = 'accuracy'
