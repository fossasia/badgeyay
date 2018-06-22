from Crypto.Cipher import AES
from hashlib import md5
import base64


password = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'

BLOCK_SIZE = 16


def pad(data):
    pad = BLOCK_SIZE - len(data) % BLOCK_SIZE
    return data + pad * chr(pad)


def unpad(padded):
    pad = ord(chr(padded[-1]))
    return padded[:-pad]


def _encrypt(data, nonce, password):
    m = md5()
    m.update(password.encode('utf-8'))
    key = m.hexdigest()

    m = md5()
    m.update((password + key).encode('utf-8'))
    iv = m.hexdigest()

    data = pad(data)

    aes = AES.new(key, AES.MODE_CBC, iv[:16])

    encrypted = aes.encrypt(data)
    return base64.urlsafe_b64encode(encrypted)


def _decrypt(edata, nonce, password):
    edata = base64.urlsafe_b64decode(edata)

    m = md5()
    m.update(password.encode('utf-8'))
    key = m.hexdigest()

    m = md5()
    m.update((password + key).encode('utf-8'))
    iv = m.hexdigest()

    aes = AES.new(key, AES.MODE_CBC, iv[:16])
    return unpad(aes.decrypt(edata)).decode('utf-8')
