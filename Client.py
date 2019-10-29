import AES256

key = str(time.time()).encode('utf-8')

print(AES256.encrypt("awdawd", key))