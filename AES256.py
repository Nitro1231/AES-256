import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES

Size = 32 # 256 bits
pad = lambda s: s + (Size - len(s.encode('utf-8'))% Size) * chr(Size - len(s.encode('utf-8')) % Size) # Pading for bit len, UTF-8 has 2 byte for each.
unpad = lambda s : s[:-ord(s[len(s)-1:])]

class AES256:
    def encrypt(self, msg, key):
        msg = pad(msg)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(msg.encode('utf-8')))
    
    def decrypt(self, msg, key):
        msg = base64.b64decode(msg)
        iv = msg[:32]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        return unpad(cipher.decrypt(mg[32:]))