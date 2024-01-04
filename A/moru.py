import math
levels=[1,2,3,3,3,4,5,6]
min=2
max=4
player=3
canList=[]

for i in levels:
    if min<=i<=max:
        canList.append(i)
x=len(canList)

ans=int(math.factorial(x)/(math.factorial(player)*math.factorial(x-player)))
print(canList)
print(ans)