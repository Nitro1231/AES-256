import socket, AES256

def main():
    IP = '127.0.0.1'
    Port = 5555
    ServerSocekt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ServerSocekt.connect((IP, Port))

    msg = "test"

    while True:
        ServerSocekt.send(msg.encode('utf-8'))
        data = ServerSocekt.recv(1024)

        print(str(data.decode('utf-8')))
        msg = input()

    ServerSocekt.close()

main()

#AES = AES256.AES256('ThisIs16bytesKey')
#encrypted = AES.encrypt('Test1234Test test aBcD 가나다라')
#decrypted = AES.decrypt(encrypted)
#print(encrypted)
#print(decrypted)