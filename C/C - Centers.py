"""
N = int(input())
l = list(map(int, input().split()))
v = {}
x = max(l)
ans = []
for i in range(1, x+1):
    a = []
    for j, x in enumerate(l):
        if x == i:
            a.append(j)
    v[i] = a[1]
    v_s = sorted(v.items(), key=lambda sec: sec[1])
for k in range(0, N):
    print(*v_s[k][0])
"""

"""N = int(input())
A = [int(a) for a in input().split()]
cnt = [[] for n in range(N)]
for x in range(N*3):
    cnt[A[x]-1].append(x+1)
centers = [cnt[y][1] for y in range(N)]
 
idx = [*range(N)]
ans = sorted(idx, key=lambda i: centers[i])
print(*list(map(lambda x: x+1,ans)))"""
# TLE
N = int(input())
A = list(map(int, input().split()))

C = [0]*(N+1)
ans = [0]*(N+1)
cnt = 1

for a in A:
    C[a] += 1
    if C[a] == 2:
        ans[cnt] = a
        cnt += 1

print(*ans[1:])


"""
l=[0] * int(input())
for i in list(map(int,input().split())):
  l[i-1]+=1
  if l[i-1]==2:
    print(i,end=" ")

"""
