import sys
import os

def main():
	menu()

def menu():
    refresh()
    print(" _    _                    __      ___     _ _           ______")
    print("| |  | |                   \ \    / (_)   (_) |         |___  /")
    print("| |__| |_   _ _ __   ___ _ _\ \  / / _ ___ _| |_ ___  _ __ / / ")
    print("|  __  | | | | '_ \ / _ \ '__\ \/ / | / __| | __/ _ \| '__/ /  ")
    print("| |  | | |_| | |_) |  __/ |   \  /  | \__ \ | || (_) | | / /__") 
    print("|_|  |_|\__, | .__/ \___|_|    \/   |_|___/_|\__\___/|_|/_____|")
    print("       __/ | |                                                 ")                                               
    print("      |___/|_|                                                 ")                                           
    print()
    print()
    
    selected = input("""
    1. Disable HyperVisor
    2. Enable HyperVisor
    3. Credits

    Please note your computer will reset after the hypervisor is enabled or disabled                        
    Make your selection now:  """)
    
    if selected == "1":
        disable()
    elif selected == "2":
        enable()
    elif selected == "3":
        credit()
    else:
        print("Invalid option!")
        menu()
        
                                             
def refresh():
    platforms = {
        'linux1' : 'Linux',
        'linux2' : 'Linux',
        'darwin' : 'OS X',
        'win32' : 'Windows'
    }                                 
 
    if sys.platform == "linux1" or sys.platform == "linux2":
        os.system("clear")
    elif sys.platform == "win32":
        os.system("cls")
    else:
        print("Error! Unknown OS!")
        print("HyperVisitorZ should be ran on Linux devices.")
        
def credit():
    refresh()
    print("HyperVisitorZ")
    print()
    print("Written by Tenor-Z")
    print("https://github.com/Tenor-Z")
    print()
    print("January 13th, 2023")
    print()
    print("Wrote this for college because a lot of us were")
    print("having issues with VMWare and GNS3, and VMWare is")
    print("a bee-otch!")
    print()
    print("Hi Harrison!")
    print()
    back = input("Press ENTER to go back")
    menu()

def disable():
    os.system("bcdedit /set hypervisorlaunchtype off")
    print("Disabling....")
    os.system("shutdown -r -t 0")

def enable():
    os.system("bcdedit /set hypervisorlaunchtype on")
    print("Enabling....")
    os.system("shutdown -r -t 0")    
main()