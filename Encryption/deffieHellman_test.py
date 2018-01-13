#public
g = 5
n = 5156161461

#alice
a = 4554889

#bob
b = 1451415

#alice
ga = g^a%n

#bob
gb = g^b%n

#gb and ga become public
#cannot recalculate the value a or b
#alice
gba = ga^b%n
gab = gb^a%n

message = "Secret Key Exchange"

#sending message encrypted
for i in message:
    print("Messege from sender:", i)
    i = ord(i)
    i = i + gba
    print("Encrypting on sender:", i)
    print("Character sent!")

#decrypting message
    print("Character received!")
    i = i - gab
    i = chr(i)
    print("Decrypting on receiver:", i)


