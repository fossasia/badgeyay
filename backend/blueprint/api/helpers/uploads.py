import uuid
import os
from flask import current_app as app


def generateFileName():
    return str(uuid.uuid4())


def saveToImage(imageFile=None, extension='.png'):
    imageName = generateFileName() + extension
    imageDirectory = os.path.join(app.config.get('BASE_DIR'), 'static', 'uploads', 'image')

    if not os.path.isdir(imageDirectory):
        os.makedirs(imageDirectory)

    imagePath = os.path.join(imageDirectory, imageName)
    image = open(imagePath, "wb")
    image.write(imageFile.decode('base64'))
    image.close()

    return imageName


def saveToCSV(csvFile=None, extension='.csv'):
    csvName = generateFileName() + extension
    csvDirectory = os.path.join(app.config.get('BASE_DIR'), 'static', 'uploads', 'csv')

    if not os.path.isdir(csvDirectory):
        os.makedirs(csvDirectory)

    csvPath = os.path.join(csvDirectory, csvName)
    csvFile.save(csvPath)

    return csvName
