import shutil
from pathlib import Path

from .._settings.settings import properties, settingsFolder, mediaFolder, media, bodyMail


def customPath(fileName, *args):
    return Path.cwd().joinpath(Path(*args, fileName)).relative_to(Path.cwd())


def createFolder(folderName, *args, settings=True):
    if (settings):
        Path.mkdir(customPath(folderName, settingsFolder, *args), parents=True, exist_ok=True)
    else:
        Path.mkdir(customPath(folderName, *args), parents=True, exist_ok=True)


def dropFolder(folderName, *args, settings=True):
    if (settings):
        shutil.rmtree(str(customPath(folderName, settingsFolder, *args)), ignore_errors=True)
    else:
        shutil.rmtree(str(customPath(folderName, *args)), ignore_errors=True)


propertiesFile = customPath(properties, settingsFolder)
mediaFile = customPath(media, settingsFolder, mediaFolder)
bodyMailText = customPath(bodyMail, settingsFolder)
