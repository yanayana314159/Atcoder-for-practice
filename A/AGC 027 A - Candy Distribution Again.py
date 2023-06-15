N, x = map(int, input().split())
l = sorted(map(int, input().split()))
ans = 0
for i in range(N):
    x = x-l[i]
    ans += 1
    if (i == N-1) and (x != 0):
        ans -= 1
        continue
    if x < 0:
        ans -= 1
        continue
    # print(x)

print(ans)
# AC
