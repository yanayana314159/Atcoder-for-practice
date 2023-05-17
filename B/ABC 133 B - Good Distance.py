N, D = map(int, input().split())

li = []
for i in range(N):
    li.append(list(map(int, input().split())))
cot = 0
for n in range(N-1):
    for x in range(n+1, N):
        sum = 0
        for d in range(0, D):
            sum += (li[n][d]-li[x][d]) ** 2
        # print(f"sum={sum},sum ** 0.5={sum ** 0.5}")
        # print(n, x, d)
        double = sum ** 0.5
        # print(double.is_integer())
        if double.is_integer() == True:
            cot += 1

print(cot)
# AC


"""
float型がintか判定するコード
X.is_integer() $ True False型

n, d = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(i + 1, n):
        d2 = sum([(y - z)**2 for y, z in zip(l[i], l[j])])
        if d2**0.5 == int(d2**0.5):
            ans += 1
print(ans)

"""
