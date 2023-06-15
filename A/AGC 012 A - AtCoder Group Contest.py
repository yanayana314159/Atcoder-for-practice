N = int(input())
l = sorted(map(int, input().split()), reverse=True)
# print(l)
ans = 0
for i in range(N):
    # print(l[2*i+1])
    ans += l[2*i+1]

print(ans)

# AC
