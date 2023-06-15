N = int(input())
l = []
[l.append(int(input())) for _ in range(N)]

l_s = sorted(set(l))

print(len(l_s))

# AC
