N = int(input())
li = list(map(int, input().split()))
ans = 0
for i in range(len(li)-2):
    for j in range(i+1, len(li)-1):
        for k in range(j+1, len(li)):
            M = max(li[i], li[j], li[k])
            S = li[i] + li[j] + li[k]
            if li[i] != li[j] and li[i] != li[k] and li[j] != li[k] and M < S-M:
                ans += 1
print(ans)


"""解答例
N = int(input())
L = list(map(int, input().split()))
L.sort()
 
ans = 0
for i in range(len(L)-2):
    for j in range(i+1, len(L)-1):
        if L[i] == L[j]: continue
        for k in range(j+1, len(L)):
            if L[i] == L[k] or L[j] == L[k]: continue
            if L[i] + L[j] > L[k]: ans += 1
 
print(ans)

"""
