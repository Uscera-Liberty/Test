n = int(input())
messagetoencrypt = str(input().split())
encryptedMessage = ""
LIST = "abcdefghijklmnoprstuvwxyz"
for letter in messagetoencrypt:
    place = LIST.find(letter)
    newPlace = (place + n + len(LIST)) % len(LIST)

    if letter in LIST:
        encryptedMessage += LIST[newPlace]


print(encryptedMessage)
