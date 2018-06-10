import uuid
import os
from flask import current_app as app
import base64


def generateFileName():
    return str(uuid.uuid4())


def saveToImage(imageFile=None, extension='.png'):
    imageName = generateFileName() + extension
    imageDirectory = os.path.join(app.config.get('BASE_DIR'), 'static', 'uploads', 'image')

    if not os.path.isdir(imageDirectory):
        os.makedirs(imageDirectory)
    imageFile = imageFile.replace('data:image/' + extension.split('.')[1] + ';base64,', '')
    imagePath = os.path.join(imageDirectory, imageName)
    image = open(imagePath, "wb")
    image.write(base64.b64decode(imageFile))
    image.close()

    return imageName


def saveToCSV(csvFile=None, extension='.csv'):
    csvName = generateFileName() + extension
    csvDirectory = os.path.join(app.config.get('BASE_DIR'), 'static', 'uploads', 'csv')

    if not os.path.isdir(csvDirectory):
        os.makedirs(csvDirectory)

    csvFile = csvFile.replace('data:text/csv;base64,', '')
    csvPath = os.path.join(csvDirectory, csvName)
    csv = open(csvPath, "wb")
    csv.write(base64.b64decode(csvFile))
    csv.close()

    return csvName


def saveAsCSV(csvData=None):
    csvName = generateFileName() + '.csv'
    csvDirectory = os.path.join(app.config.get('BASE_DIR'), 'static', 'uploads', 'csv')

    if not os.path.isdir(csvDirectory):
        os.makedirs(csvDirectory)

    csvPath = os.path.join(csvDirectory, csvName)
    with open(csvPath, 'w') as f:
        f.write(csvData)
    f.close()

    return csvName
