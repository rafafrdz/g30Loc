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
def enviar(aviso):
    msg = MIMEMultipart()
    #parametros
    password = cfg['pass']
    msg['From'] = cfg['email'] #aqui cambiar el email de origen
    msg['To'] = cfg['email']
    msg['Subject'] = 'G30Loc - Ubicacion'

    # Añade el mensaje al cuerpo del correo
    msg.attach(MIMEText(aviso,'plain'))
    # Crea conexión
    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.starttls()
    server.login(msg['From'], password) # Logueo
    server.sendmail(msg['From'], msg['To'], msg.as_string()) # Enviar
    server.quit() # Cerrar conexión

def macAdd():
    sbp.call("iwlist {} scan > .macAddress.txt".format(cfg['tarjeta-red']), shell=True)
    fich = open(".macAddress.txt", "r")
    lines = fich.readlines()
    fich.close()
    sbp.call('rm .macAddress.txt', shell=True)
    macAddress = [x[x.find(":")+2:].strip() for x in lines  if 'Address' in x ]
    signalStrength = [int(x[x.find("vel=")+4:].strip().split()[0]) for x in lines if 'Signal level' in x ]
    dataMAC = [{"macAddress": macAddress[i], "signalStrength":signalStrength[i],"signalToNoiseRatio":0} for i in range(len(macAddress))]
    return dataMAC

def main():
    datos = {
        "considerIP":"false",
        "wifiAccessPoints": macAdd()
    }
    url = cfg['url']+cfg['key']
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
