N, X = map(int, input().split())
y = []
for i in range(N):
    y.append(int(input()))
rest = X-sum(y)
# print(rest)
print(int(N+rest//min(y)))


# AC
"""
N, X = map(int, input().split())
m = [int(input()) for _ in range(N)] #こんな書き方あるんだ
 
 
for i in range(N):
    X -= m[i]
 
m.sort()
max_doughnuts =  X // m[0]
 
print(len(m) + max_doughnuts)
"""
