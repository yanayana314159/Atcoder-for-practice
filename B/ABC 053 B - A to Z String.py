s = str(input())
a = s.find("A")
z = s.rfind("Z")

print(z-a+1)

# AC
"""解答例
s=input()
print(s.rindex('Z')-s.index('A')+1)
"""
