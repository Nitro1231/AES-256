import time
import AES256

AES = AES256.AES256('ThisIs16bytesKey')
encrypted = AES.encrypt('Test1234Test test aBcD 가나다라')
decrypted = AES.decrypt(encrypted)
print(encrypted)
print(decrypted)