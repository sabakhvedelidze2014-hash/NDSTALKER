import time
import colorama
import os
import webbrowser  # დამატებულია ბრაუზერისთვის

from colorama import Fore, Back, Style

a = 1
b = 2
c = 3
d = 4
e = 5
f = 6
g = 7
h = 8
i = 9
j = 10
k = 11
l = 12
m = 13
n = 14
o = 15
p = 16
q = 17
r = 18
s = 19
t = 20
u = 21
v = 22
w = 23
x = 24
y = 25
z = 26

banner = """
d8b   db d8888b. .d8888. d888888b  .d8b.  db      db   dD d88888b d8888b. 
888o  88 88  `8D 88'  YP `~~88~~' d8' `8b 88      88 ,8P' 88'     88  `8D 
88V8o 88 88   88 `8bo.      88    88ooo88 88      88,8P   88ooooo 88oobY' 
88 V8o88 88   88   `Y8b.    88    88~~~88 88      88`8b   88~~~~~ 88`8b   
88  V888 88  .8D db   8D    88    88   88 88booo. 88 `88. 88.      88 `88. 
VP   V8P Y8888D' `8888Y'    YP    YP   YP Y88888P YP   YD Y88888P 88   YD 
---------------------------------------------------------------------------
     NDSTALKER Is Not Responsible For Anything You Do With This Program.
"""

print("Loading...")
time.sleep(3)
choice = input("Are You Sure You Want To Continue? (Y/N) NDSTALKER Is Not Responsible For Anything You Do With This Program. ")
if choice == "Y" or choice == "y":
    print("Running NDSTALKER Code...")
    time.sleep(1)

    print("[ ▬         ] 10%")
    time.sleep(0)
    print("[ ▬▬        ] 20%")
    time.sleep(0)
    print("[ ▬▬▬       ] 30%")
    time.sleep(0)
    print("[ ▬▬▬▬      ] 40%")
    time.sleep(0)
    print("[ ▬▬▬▬▬     ] 50%")
    time.sleep(0)
    print("[ ▬▬▬▬▬▬    ] 60%")
    time.sleep(0)
    print("[ ▬▬▬▬▬▬▬   ] 70%")
    time.sleep(0)
    print("[ ▬▬▬▬▬▬▬▬  ] 80%")
    time.sleep(0)
    print("[ ▬▬▬▬▬▬▬▬▬ ] 90%")
    time.sleep(0)
    print("[ ▬▬▬▬▬▬▬▬▬ ] 91%")
    time.sleep(0)
    print("[ ▬▬▬▬▬▬▬▬▬ ] 92%")
    time.sleep(0)
    print("[ ▬▬▬▬▬▬▬▬▬ ] 93%")
    time.sleep(0)
    print("[ ▬▬▬▬▬▬▬▬▬ ] 94%")
    time.sleep(0)
    print("[ ▬▬▬▬▬▬▬▬▬ ] 95%")
    time.sleep(0)
    print("[ ▬▬▬▬▬▬▬▬▬ ] 96%")
    time.sleep(0)
    print("[ ▬▬▬▬▬▬▬▬▬ ] 97%")
    time.sleep(0)
    print("[ ▬▬▬▬▬▬▬▬▬ ] 98%")
    time.sleep(0)
    print("[ ▬▬▬▬▬▬▬▬▬ ] 99%")
    time.sleep(0)
    print("[ ▬▬▬▬▬▬▬▬▬ ] 99.05%")
    time.sleep(0)
    print("[ ▬▬▬▬▬▬▬▬▬▬ ] 100%")
    time.sleep(0)

    print(f"{Fore.GREEN}{banner}")
     
    choice2 = input("1.Target Name: ")
    choice3 = input("2.Target Last Name: ")
    choice4 = input("3.Target Age: ")
    choice5 = input("4.Target Phone Number: ")

    search_query = f"{choice2}+{choice3}+{choice4}+{choice5}"

    # შეცვლილი ნაწილი
    webbrowser.open(f"https://www.google.com/search?q={search_query}")

else:
    print("Exiting...")
    time.sleep(2)
    os._exit(0)