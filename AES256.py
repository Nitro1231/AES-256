import base64
import random
import string
from hashlib import sha256
from Crypto import Random
from Crypto.Cipher import AES

BS = 32
pad = lambda s: s + (BS - len(s.encode('utf-8')) % BS) * chr(BS - len(s.encode('utf-8')) % BS)
unpad = lambda s : s[:-ord(s[len(s)-1:])]

class AES256:
    def __init__(self, key):
        self.key = bytes(self.keyGenerator(key), 'utf-8')

    def encrypt(self, raw):
        raw = pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw.encode('utf-8')))

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:16]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return unpad(cipher.decrypt(enc[16:])).decode('utf-8')

    def keyGenerator(self, key):
        stringLength = 16 - len(key)
        random.seed(key)
        letters = string.ascii_letters
        return key + ''.join(random.choice(letters) for i in range(stringLength))