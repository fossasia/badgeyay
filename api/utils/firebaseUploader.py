from firebase_admin import storage


def fileUploader(file_path, file_name):
    bucket = storage.bucket()
    fileUploaderBlob = bucket.blob('badges/' + file_name + '.pdf')
    try:
        with open(file_path, 'rb') as file_:
            fileUploaderBlob.upload_from_file(file_)
    except Exception as e:
        print(e)
    fileUploaderBlob.make_public()
    return fileUploaderBlob.public_url
