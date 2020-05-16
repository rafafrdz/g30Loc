import yaml

from .pathClass import customPath
from .._settings.settings import formatFile, ymlFormat


class yamlClass():
    def __init__(self, fileName, *path):
        self.__fileName = formatFile(fileName, ymlFormat)
        self.__path = path
        self.__fich = open(customPath(fileName, *path))

    def parse(self):
        return yaml.safe_load(self.__fich)
