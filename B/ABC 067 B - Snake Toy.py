N, K = map(int, input().split())
l = list(map(int, input().split()))

l_s = sorted(l, reverse=True)
print(sum(l_s[:K]))

# AC
