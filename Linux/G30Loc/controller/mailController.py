from email.mime.application import MIMEApplication
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import *

from .._settings.mailSettings import *
from ..controller.pathClass import mediaFile


class ServerSMTP():
    def __init__(self):
        self.__server = SMTP(host=gmailHost['host'],
                             port=gmailHost['port'])

    def __conect(self):
        self.__server.starttls()

    def __disconect(self):
        self.__server.quit()

    def __login(self):
        self.__conect()
        self.__server.login(user=user,
                            password=password)

    def send(self, mail):
        self.__login()
        self.__server.sendmail(from_addr=fromEmail,
                               to_addrs=toEmail,
                               msg=mail.mail())
        self.__server.quit()


class Mail():
    def __init__(self):
        self.msg = MIMEMultipart()

    def setBody(self, body):
        """
        Set body mail
        :param body: Path where body mail is located
        :return: None (self.msg status updated)
        """
        self.msg.attach(MIMEText(body, 'plain'))


    def setMedia(self, mediaFile, name):
        """
        Set media in mail
        :param mediaFile: Path where media is located
        :param name: Namefile that appeares in the email
        :return: None (self.msg status updated)
        """
        mediaObject = getObject(mediaFile)
        payload = MIMEImage(mediaObject, pngFormat)
        payload.add_header('Content-Disposition', 'inline', filename=name)
        self.msg.attach(payload)

    def setFile(self, fichFile, formatObject, name):
        """
        Set some binary file in mail (pdf, txt, mp3, etc.)
        :param fichFile: Path where file is located
        :param formatObject: File extension
        :param name: Namefile that appeares in the email
        :return: None (self.msg status updated)
        """
        fichObject = getObject(fichFile)
        payload = MIMEApplication(fichObject, formatObject)
        payload.add_header('Content-Disposition', 'attachment', filename=name)

    def setParamsG30Loc(self):
        self.msg['From'] = fromEmail
        self.msg['To'] = toEmail
        self.msg['Subject'] = subject
        self.setBody(body)
        self.setMedia(mediaFile, name=media)

    def mail(self):
        self.setParamsG30Loc()
        return self.msg.as_string()
