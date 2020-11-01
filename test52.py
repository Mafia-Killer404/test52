#!/usr/bin/python2
#coding=utf-8
#The Credit For This Code Goes To lovehacker
#If You Wanna Take Credits For This Code, Please Look Yourself Again...
#Reserved2020
 
 
import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
 
 
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
 
##### LOGO #####
logo = """
\033[1;91m●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●
\033[1;92m●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●

\033[1;93m●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●
\033[1;94m●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●

*_ꙮ⃢▄▆▇█�⃢✿⁍⃢🇪⃢⁌✿⃢��⃢✿⁍⃢🇪⃢⁌✿⃢��⃢✿⁍⃢🇪⃢⁌✿⃢�⃢✿⁍⃢🇪⃢⁌✿⃢��█▇▆▄⃢ꙮ_*

\033[1;91m        █▀▄▀█ █▀▀█ █▀▀ ░▀░ █▀▀█
\033[1;93m        █░▀░█ █▄▄█ █▀▀ ▀█▀ █▄▄█
\033[1;92m        ▀░░░▀ ▀░░▀ ▀░░ ▀▀▀ ▀░░▀

\033[1;97m        █░█ ░▀░ █░░ █░░ █▀▀ █▀▀█
\033[1;96m        █▀▄ ▀█▀ █░░ █░░ █▀▀ █▄▄▀
\033[1;95m        ▀░▀ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀ ▀░▀▀

*_ꙮ⃢▄▆▇█�⃢✿⁍⃢🇪⃢⁌✿⃢��⃢✿⁍⃢🇪⃢⁌✿⃢��⃢✿⁍⃢🇪⃢⁌✿⃢�⃢✿⁍⃢🇪⃢⁌✿⃢��█▇▆▄⃢ꙮ_*

\033[1;91m●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●
\033[1;92m●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●

\033[1;93m●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●
\033[1;94m●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●

"""
R = '\033[1;91m'
G = '\033[1;92m'                                
Y = '\033[1;93m'
B = '\033[1;94m'
P = '\033[1;95m'
S = '\033[1;96m'
W = '\033[1;97m'
######Clear######
def clear():
    os.system('clear')
 
#### time sleep ####
def t():
    time.sleep(1)
def t1():
    time.sleep(0.01)
 
#### print std #love###
def love(z):
	for e in z + "\n":
		sys.stdout.write(e)
		sys.stdout.flush()
		t1()
 
def menu():
    clear()
    os.system('clear')
    print(logo)
    time.sleep(0.05)
    print("\033[1;41m\033[1;37m1   To return to this menu from any Tool   \033[1;0m")
    time.sleep(0.05)
    print("\033[1;41m2\033[1;37m       Stop Process Press CTRL + z        \033[1;0m")
    time.sleep(0.05)
    print("\033[1;41m3\033[1;37m         Type python2 Cloning.py          \033[1;0m")
    time.sleep(0.05)
    print("\033[1;96m[1]  Install With Out Fb Id  Tool      ●")
    time.sleep(0.05)
    
   print("\033[1;95m[13] Tool Update                       ●")
    time.sleep(0.05)
    print("\033[1;91m[0]  EXIT")
    time.sleep(0.05)
    mafia()
def mafia():
	black = raw_input("\033[1;91m slect option>>>   ")
	if black =="":
		print ("Select a valid option !")
		mafia()
	elif black =="1":
		clear()
		print(logo)
		os.system("ls")
                os.system("cd World")
		os.system("cd Cloningx")
                love("\033[1;93mTool User Name\033[1;92m Black\033[1;93m Password \033[1;92mMafia")
                time.sleep(6)
                os.system("python2 Cloningx.py")
	
if __name__ == "__main__":
    menu()
 
