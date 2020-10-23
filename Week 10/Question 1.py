n = int(input())
string = []
string = input().split(" ")
string.sort()
for i in range (0,n):
    print (string[i], end = " ")
