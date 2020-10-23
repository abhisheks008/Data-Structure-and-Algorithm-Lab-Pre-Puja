n = int(input())
a = [int(x) for x in input().strip().split()]
valid = [[False]*101 for i in range(n)]
valid[0][a[0]] = True
for i in range(1, n):
    for v in range(101):
        if valid[i-1][v]:
            valid[i][(v + a[i]) % 101] = True
            valid[i][(v - a[i]) % 101] = True
            valid[i][(v * a[i]) % 101] = True

v = 0
for i in range(n-1,0,-1):
    for w in range(101):
        if valid[i-1][w]:
            if (w + a[i]) % 101 == v:
                a[i] = '+' + str(a[i])
                v = w
                break
            if (w - a[i]) % 101 == v:
                a[i] = '-' + str(a[i])
                v = w
                break
            if (w * a[i]) % 101 == v:
                a[i] = '*' + str(a[i])
                v = w
                break

print(*a, sep='')
