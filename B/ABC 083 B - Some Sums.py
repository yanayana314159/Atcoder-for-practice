N, A, B = map(int, input().split())
ans = 0

for i in range(N+1):
    n = str(i)
    k = len(n)
    sum = 0
    for j in range(k):
        sum += int(n[j])
    if A <= sum <= B:
        # print(i)
        ans += i


print(ans)
# AC
"""forとifの構造で手間取った
10で割りまくってくもの

def sum_all_digits(n):
  sum_digits = 0
  while n > 0:
    sum_digits += n % 10
    n //=10
  return sum_digits
 
n,a,b = (int(x) for x in input().split())
 
ans = 0
for i in range(1,n+1):
  sum_digits = sum_all_digits(i)
  if a <= sum_digits and sum_digits <=b:
    ans +=i
print(ans)


#桁数が小さければこれもあり
while i<=n:
  m=i//10000+i%10000//1000+i%1000//100+i%100//10+i%10
  if a<=m and m<=b:
    sum+=i
  i+=1
 
print(sum)
"""
