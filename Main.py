import lupa
import datetime

import logging
import os
import json
import time
import colorama
import random
import platform
import sys
from configparser import ConfigParser
from colorama import Fore, Back, Style
from lupa import LuaRuntime
import Brug

colorama.init(
    autoreset=True
)  # initialize the fucking thing since im an asshole - mini LFMAOAOAOO
shit = False
doneIntro = False
lua = LuaRuntime()
config = ConfigParser()

###### INTERNAL SETTINGS ######
sysdir = "assets" # SysDir. This Directory contains Chn.Preloader and Datadir.
preloader = sysdir + "/preload" # Chn.Preloader. This PATH holds all the important directories
datadir = preloader + "/data" # Datadir, The OS will not operate without this directory
osName = "ChungOS"  # Keep in mind that this is shitto different than os.name
fallBackToTERMINAL = False  # (False by Default) If set to true, uses your OS's terminal instead, whatever it may be bash, or CMD, or pw3yyyyysh
Diagnostics = True # More Important version of Debug Mode in Settings

try:
    os.chdir(datadir)
except IndexError:
    os.chdir("assets/preload/data")


with open("options.json") as f:
    curOptions = json.load(f)
for i in range(3):
        os.chdir("..")





while not shit:
    if not fallBackToTERMINAL is True:
        try:
            if curOptions.get("colors") == "true":
                msg = input(
                    Fore.YELLOW + __name__ + Fore.RED + ">>>" + Fore.GREEN + " "
                ).lower()
            else:
                msg = input(Fore.YELLOW + __name__ + Fore.RED + ">>>" + Fore.GREEN + " ").lower()
        except PermissionError:
            msg = input(osName.lower() + "$")
        
        if msg == "time":
            print(datetime.datetime.now())
        elif msg == "ls" or msg == "dir": 
            #print("Directory " + os.curdir + " is " + os.path + " and has nil volume.")
            print(Fore.WHITE + "Listing PATH where the Main.py executes in.")
            print("\n".join(os.listdir()))
        
        elif msg == "settings":
            print('Welcome to the settings menu.')
            time.sleep(1)
            print('Here you are able to customize your experience.')
            time.sleep(1)
            print('Continue to go to the settings menu?')
            thefuckinginputsinceyallareass = input().lower()
            
            if thefuckinginputsinceyallareass == "y":
                os.chdir("assets/preload/data")
                print("Ok, let's input the new options you want. One second let me prepare the list.")
                time.sleep(1) # ffs lets make the usr not wait for long
                killMe = input("Aha! Got it! Would you like colors to be enabled? (y/n)\n").lower()
                if killMe == "y":
                   curOptions['colors'] = 'true'
                elif killMe == "n":
                   curOptions['colors'] = 'false'
                # Writes to it
                with open('options.json', 'w') as d:
                    json.dump(curOptions, d)
                input()
                for i in range(3):
                    os.chdir("..")

            else:
                pass

        
        elif msg == "exit":
            exit()

        elif msg == "run-lua":
            for i in os.listdir("assets/preload/raw_scripts"):
                os.chdir("assets/preload/raw_scripts")
                if i.endswith(".lua"):
                    with open(i, "r") as f:
                        lua.eval(str(f.read()))
                for i in range(2):
                    os.chdir("..")
        elif msg.startswith("run-luafile") and msg.endswith(".lua"):
            if Diagnostics is True:
                if random.randint(1, 50) == 1 and curOptions.get("eastereggs") == "true":
                    logging.debug("Ran the " + msg + " with our Trusty Lua Runtime!")
                else:
                    logging.debug("Ran:", msg)
            os.chdir("assets/preload/raw_scripts/")
            with open(msg[12:], "r") as f:
                try:
                    lua.eval(str(f.read()))
                except Exception as errno:
                    print("Unfortunately, " + errno)
            for i in range(3):
                os.chdir("..")
    
        elif msg.startswith("mkdir"):

            try:
                os.system(
                    "mkdir " + str(msg[6:])
                )  # we are using str() method incase the directory name is a number lol.
            except IndexError:
                print("Could not make directory.")    
        elif bool(msg) is False: # i love overcomplicating things.
            pass        
        
        elif msg[0:3] in ('exit', 'quit'):
            exit()
        
        elif msg == 'power':

        
            try:
                print("What would you like to do?", os.getlogin() + '?')
                if os.name == 'nt':
                    print("""
                    1. Shutdown
                    2. Reboot
                    3. Lock
                    4. Log Out
                    """)
                killMe = int(input(""))
                if killMe == 1:
                    print("Are you sure you want to shut down? (y/n)")
                    confirm = input().lower()
                    if confirm == "y":      
                        os.system("shutdown /s /hybrid /c \"MiniOS has shutdown this P\" /t 005")
                    else:
                        print("Ok then.")
                elif killMe == 2:
                    os.system("schutdown /r /c \"MiniOS has reboot this PC\" /t 005")
                elif killMe == 3:
                    print("We are generous, we won't lock your PC. good luck trying to make us to. ;)") # :/ - Arezalgamer89
                elif killMe == 4:
                    os.system("shutdown /l /t 000")
                else:
                    print("What would you like to do?", os.getlogin() + '?')
                    print("""
                            1. Reboot
                            2. Lock
                            3. Freeze Computer (Halt)
                        """)
                    killMe = input()
                    if killMe == 1 and not os.name == 'nt':
                        os.system('reboot')
                    elif killMe == 2 and not os.name == 'nt':
                        print("Are you sure you want to lock miniOS (and potentially your PC too?)")
                        confirm = input().lower()
                        if confirm == "y":
                            if platform.system() == 'Darwin': # Basically mac
                                os.system("/System/Library/CoreServices/Menu\ Extras/user.menu/Contents/Resources/CGSession -suspend") #? Unsure about this...
                            else:
                                os.system('loginctl lock-screen')
                    elif killMe == 3 and not os.name == 'nt':                        
                        print("Your Computer is Unresponsive now, You must force-shutdown your Mac/PC")
                        time.sleep(0.5)
                        os.system("halt")
            
            except Exception as e:
                if curOptions.get("colors") == "true":
                    print(Fore.RED + "ERROR:" + Fore.WHITE + str(e))
                else:
                    print(Fore.WHITE + "ERROR:" + str(e))
        
        elif msg == 'cmd' and platform.system == "Windows":
            try:
                os.system('start')
            except:
                os.system('cmd')
        elif msg == 'bash' or msg == 'terminal' and platform.system == "Linux":
            os.system("gnome-terminal -e 'bash -c \"sudo apt-get update; exec bash\"'")
        elif msg == 'terminal' and platform.system == 'Darwin':
            os.system("start") #! HELP, I NEED HELP WHAT SHOULD I TYPE HERE AAAA
        
        
        else:
            print(Fore.WHITE + "'" + msg + "' Command or LuaRT File could not be found")
                
                
    else:  # Fallback
        if doneIntro is False:
            if os.name == "nt":
                print(
                    "Welcome to " + osName + "! Use this Terminal to Perform CMD Tasks!"
                )
            else:
                print(
                    "Welcome to "
                    + osName
                    + "! Use the Prompt Below to Perform your Bash/Mac Terminal Tasks!"
                )
        doneIntro = True
        msg = input(">>> ")
        os.system(msg)



def Settings():
    Settings = [] # known to be unused for now...


    print("")