import requests
from ..controller.mailController import *
from ..controller.function import camshot, initMedia, closeMedia, getPosition
from .iwlist import *

class g30loc():
    def __init__(self):
        self.__properties = Properties()
        self.__interface = self.__properties.tred()
        self.__url = self.__properties.url()

    def getCamShot(self):
        camshot()

    def __send(self):
        posX, posY, posZ, ubiGoogleMap = self.apiGoogleMap()
        server = ServerSMTP()
        mail = Mail()
        mail.setBody(body.format(url=ubiGoogleMap,
                                 posX=posX, posY=posY, posZ=posZ))
        server.send(mail)

    def __dataApi(self):
        return iwList(self.__interface).dataApi()

    def apiGoogleMap(self):
        data = self.__dataApi()
        post = requests.post(url=self.__url, json=data).json()
        posX, posY, posZ = getPosition(post)
        ubiGoogleMap = self.__properties.ubi().format(posX=posX,posY=posY,posZ=posZ)
        return posX, posY, posZ, ubiGoogleMap

    def start(self):
        initMedia()
        self.getCamShot()
        self.__send()
        closeMedia()
