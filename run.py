import os
print("Nubmer of players?")
inp = str(input("> "))
if inp != "1" and (inp != "2"):
    print("2 Players max!")
elif inp == "1":
    os.system("python3 files/1p.py")
else:
    os.system("python3 files/2p.py")
