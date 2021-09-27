n = int(input())
a = str(input().split())
encryptedMessage = ""
list = "abcdefghijklmnoprstuvwxyz"
for i in a :
    place = list.find(i)
    newPlace = (place + n + len(list)) % len(list)

    if i in list:
        encryptedMessage += list[newPlace]


print(encryptedMessage)
