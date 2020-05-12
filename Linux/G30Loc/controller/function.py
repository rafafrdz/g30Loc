import cv2

from .._settings.settings import mediaFolder
from ..controller.pathClass import createFolder, mediaFile, dropFolder


def initMedia():
    createFolder(mediaFolder)


def closeMedia():
    dropFolder(mediaFolder)


def camshot():
    camshot = cv2.VideoCapture(0)
    shot, img = camshot.read()
    if shot:
        cv2.imwrite(filename=str(mediaFile), img=img)
    camshot.release()
