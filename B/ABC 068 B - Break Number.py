N = int(input())

I = 0
while N >= 2:
    N = N/2
    I += 1
print(2**I)

# AC

"""回答例
N = int(input())
 
for i in range(8):
    tmp_ans = 2**i
    if tmp_ans <= N:
        continue
    else:
        print(int(tmp_ans/2))
        break

N=int(input())
ans=2
while ans<=N:
    ans*=2
ans//=2
print(ans)
"""
