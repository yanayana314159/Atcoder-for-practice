
s = str(input())

answer = s[0]+str(len(s)-2)+s[-1]

print(answer)

# AC
"""回答例
s=input()
l=[s[0], str(len(s)-2), s[-1]]
print(''.join(l))
"""
