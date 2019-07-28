#!/usr/bin/env python3
import requests
import subprocess as sbp
import shlex as sh
import time
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
import smtplib
import yaml

path ="./g30Loc.yml"
cfg = yaml.safe_load(open(path))

def captura():
    cap = cv2.VideoCapture(0)
    name = "captura-pantalla"
    leido, frame = cap.read()
    if leido:
        cv2.imwrite("{nombre}.png".format(nombre=name), frame)
    cap.release()
    return name

def enviar(aviso):
    msg = MIMEMultipart()
    #parametros
    password = cfg['pass']
    msg['From'] = cfg['email'] #aqui cambiar el email de origen
    msg['To'] = cfg['email']
    msg['Subject'] = 'G30Loc - Ubicacion'

    # Añade el mensaje al cuerpo del correo
    msg.attach(MIMEText(aviso,'plain'))

    # Adjunta la captura
    nombre = captura()
    capture = MIMEImage(open("./{}.png".format(nombre),"rb").read(),'png')
    capture.add_header('Content-Disposition', 'inline', filename=nombre)
    msg.attach(capture)
    sbp.call("rm {}.png".format(nombre), shell=True)

    #Adjunta macAddress
    txt = MIMEApplication(open(".macAddress.txt", "r", encoding="ISO-8859-1").read(),'txt')
    txt.add_header('Content-Disposition', 'attachment', filename="macAddress.txt")
    msg.attach(txt)
    sbp.call('del .macAddress.txt', shell=True)

    # Crea conexión
    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.starttls()
    server.login(msg['From'], password) # Logueo
    server.sendmail(msg['From'], msg['To'], msg.as_string()) # Enviar
    server.quit() # Cerrar conexión

def macAdd():
    sbp.call("netsh wlan show networks mode=bssid > .macAddress.txt", shell=True)

    fich = open(".macAddress.txt", "r", encoding="ISO-8859-1")
    lines = fich.readlines()
    fich.close()

    macAddress = [x.split(": ")[1].strip() for x in lines if 'BSSID ' in x]
    signalStrength = [int(x[x.find("vel=")+4:].strip().split()[0]) for x in lines if 'Signal level' in x ]
    dataMAC = [{"macAddress": macAddress[i], "signalStrength":-60,"signalToNoiseRatio":0} for i in range(len(macAddress))]
    return dataMAC

def main():
    datos = {
        "considerIP":"false",
        "wifiAccessPoints": macAdd()
    }
    url = str(cfg['url'])+str(cfg['key'])
    response = requests.post(url, json=datos)
    x, y, z = (response.json()['location']['lat']), (response.json()['location']['lng']), (response.json()['accuracy'])
    aviso = str(time.strftime("%x %X"))
    aviso += "\n\nEnlace\n===========\n"
    aviso += cfg['ubicacion'].format(a=x,b=y)
    aviso += "\n\nCoordenadas\n===========\n"
    aviso += "Latitud: {}\nLongitud: {}\nRadio: {}m".format(x,y,z)
    enviar(aviso)

if __name__ == "__main__":
    main()
