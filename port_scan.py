import sys
import socket
import subprocess #for cool clear screen thingy
import threading
from queue import Queue #to make scanner supa fast
from whois import sub

subprocess.call('clear', shell=True) #clears whole console

print("""
______     ______   _____                                 
| ___ \    | ___ \ /  ___|                                
| |_/ /   _| |_/ / \ `--.  ___ __ _ _ __  _ __   ___ _ __ 
|  __/ | | |  __/   `--. \/ __/ _` | '_ \| '_ \ / _ \ '__|
| |  | |_| | |     /\__/ / (_| (_| | | | | | | |  __/ |   
\_|   \__, \_|     \____/ \___\__,_|_| |_|_| |_|\___|_|   
       __/ |                                              
      |___/                          

 """)

print("Python version:", sys.version)

<<<<<<< HEAD
target = input('Enter in a website to scan their IP: ')
=======
target = input('Enter in a website to scan their IP o boy: ')
>>>>>>> 367b2d1a401a5abc028d4de537d1471d4874dead
server = target

whois = sub(server)
print(whois)    

server_ip = socket.gethostbyname(server) #get ip adress of server name
print('IP:', server_ip)

print_lock = threading.Lock() #threading lock

def pscan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        con = s.connect((target,port))
        with print_lock:
            if port == 22:
                print(port, "SSH is open!")
            if port == 80:
                print(port, "http is open!")
            else:
                print("port",port,"is open!")
        con.close()
    except:
        pass

def threader():
    while True:
        worker = q.get()
        pscan(worker)
        q.task_done()

q = Queue()

for x in range(100):
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start()

for worker in range(1,1024): #goes through ports 1-100
    q.put(worker)

q.join()


print("_______________________Scan Complete_____________________")

"""
idea: make if else statements so different ports can print their port numbers function
"""



