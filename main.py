n = int(input())
a = str(input().split())
list = "abcdefghijklmnop"
for i in range(len(list)):
    if n > -1:
        print(list[i + n])

