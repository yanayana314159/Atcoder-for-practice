N = int(input())
l = list(map(int, input().split()))

l_s = sorted(l, reverse=True)

Alice = 0
Bob = 0
for i in range(N):
    if i % 2 == 0:
        Alice += l_s[i]
    if i % 2 == 1:
        Bob += l_s[i]

print(Alice-Bob)


# AC
"""
n = int(input())
a = sorted(map(int, input().split()), reverse=True)
print(sum(a[::2]) - sum(a[1::2]))
"""
