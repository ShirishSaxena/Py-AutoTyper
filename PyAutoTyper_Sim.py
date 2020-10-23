import time
import os.path
from os import path
import random
import keyboard
#from pynput.keyboard import Key, Controller
#keyboard = Controller()



Version = "v1.2 (26-Nov-19)"

WaitTime = 3
Version ='1.2 '

KeyTime=0
ReleaseTime = 0

Vars_Simulate=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
               'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C',
               'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','[',1,2,3,4,5,6,7,8,9,0,'-','=',']',';',
               '.',',','`']


print "\nShowY AutoTyper %s" %Version
print "Support Email : me@showy.pro"
print "Works best with ASCII Char. Names\n\n\n"

Location = raw_input("Input File Name to Simulate Key Presses : ")

def ISimulateThingY(Location):
    global KeyTime,ReleaseTime,Vars_Simulate
    
    file1 = open(Location,"r+")
    SaveContent = file1.read()
    file1.seek(0)
    #SaveContent = SaveContent.decode('utf-8')
    #keyboard.write('        \n')
    #keyboard.write(SaveContent)
    start=time.time()
    for element in SaveContent:
        if element not in Vars_Simulate:
            keyboard.write(element)
        else:
            #print (element)
            keyboard.press(element)
            Rand_Rel=round(random.uniform(0.005, 0.009),1) #Time to wait Release key
            time.sleep(Rand_Rel)
            keyboard.release(element)
            Rand_KeyNext=round(random.uniform(0.02, 0.06),2) #Time to wait for next word
            time.sleep(Rand_KeyNext)
            KeyTime += Rand_KeyNext
            ReleaseTime += Rand_Rel

            
    end=time.time()
    print "\nFile has finished Typing\n\n"
    return (end-start)

if '.txt' not in Location:
    Location= Location+'.txt'
    
if path.exists(Location):
    print ("File Exists\n")
    print ("Heading over to Simulating Key presses\n\n")
    print("\n\nIt will start to simulate Keypresses in : %d sec\n" %WaitTime)
    print("\nPress F6 Hotkey to Start : ")
    keyboard.wait('F6')
    print("\nHotkey Pressed Starting 3 seconds")
    time.sleep(WaitTime)
    print("\n\n..\n\n")
    print ("Simulation Took : %.2f" %round(ISimulateThingY(Location),2))
    print "\nEverything is Done. Thanks\n\n"
    ReleaseTime = round(ReleaseTime,2)
    KeyTime=round(KeyTime,2)
    print("Total Time between words : %.2f \nTotal Time between key press & release : %.2f\n\n" %(ReleaseTime,KeyTime))
    tt = ReleaseTime+KeyTime
    print("Total Wait Time : %.2f \n\n" %(tt))
    raw_input("\n\nPress any for exit")
else :
    print ("%s doesn't exists\n Try Again \n" %Location)
    raw_input("\n\nPress Any key to Exit")



