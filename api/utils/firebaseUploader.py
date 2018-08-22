from firebase_admin import storage


def fileUploader(file_path, blob_path):
    bucket = storage.bucket()
    fileUploaderBlob = bucket.blob(blob_path)
    try:
        with open(file_path, 'rb') as file_:
            fileUploaderBlob.upload_from_file(file_)
    except Exception as e:
        print(e)
    fileUploaderBlob.make_public()
    return fileUploaderBlob.public_url


def deleteFile(blob_path):
    bucket = storage.bucket()
    fileDeleteBlob = bucket.blob(blob_path)
    try:
        fileDeleteBlob.delete()
    except Exception as e:
        print(e)
