N, L = map(int, input().split())
l = []
[l.append(str(input())) for _ in range(N)]
l_s = sorted(l)

ans = "".join(l_s)

print(ans)

# AC
