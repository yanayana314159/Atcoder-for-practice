A, B = map(int, input().split())

l = []
for i in range(A, B+1):
    N = str(i)
    if (N[0] == N[4]) and (N[1] == N[3]):
        l.append(N)

print(len(l))

# AC
