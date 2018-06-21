[num, bangs] = input().split()
n = int(num)
k = len(bangs)
p = 1
while n > 0:
    p *= n
    n -= k
print(p)
