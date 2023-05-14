from ntpath import join


s = str(input())
list = []
for i in range(len(s)):
    if (i+1) % 2 == 1:
        list.append(s[i])

print("".join(list))

# AC
"""
n=len(s)
for i in range(0 ,n,2):
  t=t+s[i]
print(t)

s = input()
print(s[::2])

こんな書き方もある
print(s[1::2])
"""
