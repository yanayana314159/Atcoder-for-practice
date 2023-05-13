r, g, b = map(int, input().split())

Num = r*100+g*10+b
if Num % 4 == 0:
    print("YES")
else:
    print("NO")

# AC
