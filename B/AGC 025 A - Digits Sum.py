N = int(input())
l = [100000, 1]
for i in range(1, N):
    A = str(i)
    B = str(N-i)
    SumA = 0
    SumB = 0
    for j in range(len(A)):
        SumA += int(A[j])
    for k in range(len(B)):
        SumB += int(B[k])

    ans = SumA+SumB
    if ans < l[0]:

        l[0] = ans
        l[1] = A

print(l[0])

# AC,めっちゃ時間かかった．
"""
n=int(input())
ans=0
if n%10==0:
  print(10)
else:
  for i in range(n):
    ans+=n%10
    n//=10
  print(ans)

s=input()
n=int(s)
a=0
if n==10**(len(s)-1):
    print(10)
else:
    for i in s:
        a+=int(i)S
    print(a)


"""
