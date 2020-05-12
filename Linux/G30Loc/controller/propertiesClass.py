from .._settings.settings import *
from ..controller.pathClass import propertiesFile
from ..controller.yamlClass import *


class Properties():
    def __init__(self, propertiesFile=propertiesFile):
        self.__prop = yamlClass(propertiesFile).parse()

    def __key(self):
        return self.__prop[key_]

    def __url(self):
        return self.__prop[url_]

    def __ubi(self):
        return self.__prop[ubi_]

    def __tred(self):
        return self.__prop[tred_]

    def email(self):
        return self.__prop[email_]

    def password(self):
        return self.__prop[pass_]
