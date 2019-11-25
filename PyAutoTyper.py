import time
import os.path
from os import path

import keyboard
#from pynput.keyboard import Key, Controller
#keyboard = Controller()



Version = "v1.1 (25-Nov-19)"
##########################
'''
    Author : Shirish Saxena
'''
##########################

WaitTime = 3
Version ='1.1 '

print "\nShowY AutoTyper %s" %Version
print "Support Email : me@showy.pro"
print "Works best with ASCII Char. Names\n\n\n"

Location = raw_input("Input File Name to Simulate Key Presses : ")

def ISimulateThingY(Location):
    file1 = open(Location,"r+")
    SaveContent = file1.read()
    file1.seek(0)
    SaveContent = SaveContent.decode('utf-8')
    keyboard.write('        \n')
    keyboard.write(SaveContent)
   # for element in SaveContent:
   #     keyboard.press("%s" %element)
   #     keyboard.release("%s" %element)
   # time.sleep(1)
    print "\nFile has finished Typing\n\n"

if path.exists(Location):
    print ("File Exists\n")
    print ("Heading over to Simulating Key presses\n\n")
    print("\n\nIt will start to simulate Keypresses in : %d sec\n" %WaitTime)
    print("\nPress F6 Hotkey to Start : ")
    keyboard.wait('F6')
    print("\nHotkey Pressed Starting 3 seconds")
    time.sleep(WaitTime)
    print("\n\n..\n\n")
    ISimulateThingY(Location)
    print "\nEverything is Done. Thanks"
else :
    print ("%s doesn't exists\n Try Again \n" %Location)
    raw_input("\n\nPress Any key to Exit")



