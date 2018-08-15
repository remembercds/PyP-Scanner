import os
import subprocess

web = "pythonprogramming.net"

#cmd = 'whois '

#def whois(web_ip):
#    whoIsIs = os.system(cmd + web_ip)
#    print(whoIsIt)
#

def sub(web_ip):
    subprocess.call('whois ' + web_ip, shell=True)


#sub(web)
"""
ideas: maybe add more prasing to the whois data 
"""



