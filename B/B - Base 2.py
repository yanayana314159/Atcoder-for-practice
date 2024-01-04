l = list(map(int, input().split()))
ans = 0
for i in range(0, 64):
    ans += l[i]*2**i

print(ans)

# AC
