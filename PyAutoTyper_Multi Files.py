import time,os,shutil,keyboard
from os import path
import io
#from pynput.keyboard import Key, Controller
#keyboard = Controller()



Version = "v1.1 (25-Nov-19)"
##########################
'''
    Author : Shirish Saxena
'''
##########################

#Root_Dir = os.getcwd() #Get Cur Dir
Dir_To_Search_TxT = ""
Dir_DxT = ""

Reference_DxT = ""

print Dir_DxT

print "\nShowY A-MultiFiles %s" %Version
print "Support Email : me@showy.pro \n\n\n"


def Create_File(fname):
    global Dir_DxT,Reference_DxT
    shutil.copy(Reference_DxT,"%s\\%s.dxt"%(Dir_DxT,fname))
    print "%s.txt --> %s.dxt" %(fname,fname)

def ISimulateThingY(Location):
    global Dir_To_Search_TxT,Dir_DxT
    (abso_filen,ext_file) = os.path.splitext(Location)
    print "Start [F6] : %s " %Location #waits for f6 hotkey to start
    keyboard.wait('F6')
    Create_File(abso_filen) #create dxt
    print "Open %s.dxt --> Start Typing in 3 Sec\n" %abso_filen
    time.sleep(1)
    os.startfile("%s\%s.dxt" %(Dir_DxT,abso_filen))
    time.sleep(2)
    #file1 = open(Location,"r+") #Normal Open
    file1 = io.open("%s\\%s"%(Dir_To_Search_TxT,Location), mode="r", encoding="utf-8")
    SaveContent = file1.read()
    #SaveContent = file1.read()
    file1.seek(0)
    #SaveContent = SaveContent.encode('utf-8')
    keyboard.write("  \n")
    keyboard.write(SaveContent)
    print "Done : %s.dxt \n" %abso_filen
    

start = time.time()

if not os.path.exists(Dir_DxT ):
    os.makedirs(Dir_DxT)

Root_Dir = Dir_To_Search_TxT #Get Cur Dir
for dirName, subdirList, fileList in os.walk(unicode(Root_Dir)):
    for fname in fileList:
        if fname.endswith(('.txt')) == True:
            ISimulateThingY(fname)

print "\n\nTotal Time : %.2f mins\n\n" %((time.time()-start)/60)
raw_input("")
