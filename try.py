
a = [[0 for _ in range(51)]for _ in range(51)]
# print(a, len(a), len(a[1]), sep='\n')
n = 50
for j in range(50,0,-1):
    k = j
    for i in range(n,0,-1):
        if n-i+1<=j:
            a[i][j] = k
            k += 1
        else:
            a[i][j] = 0
j = 20
s = 0
for i in range(1,n+1):
    s += a[i][j]
print(s)

p = 1
k = 21
while k < 29:
    p *= (26-k)
    k += 2
print(p)


