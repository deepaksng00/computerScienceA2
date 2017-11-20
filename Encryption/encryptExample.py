import random

def encryption():
    f = open("key.txt", "w+")
    f.close()
    e = open("encrypt.txt", "w+")
    e.close()
    inputstr = input("Plase type the message you want to encrypt: ")
    for i in inputstr:
        l = ord(i)
        rand = random.randint(1, 9)
        l = l + rand
        a = chr(l)
        x = str(rand)
        f = open("key.txt", "a")
        f.write(x)
        f.close()
        e = open("encrypt.txt", "a")
        e.write(a)
        e.close()
        
        

def __init__():
    print("Welcome to the encryption program")
    print("Please select your option:")
    print("1.   Encrypt")
    print("2.   Decrypt")
    print("3.   Exit")
    x = input("")
    if x == "1":
        encryption()


__init__()
    
