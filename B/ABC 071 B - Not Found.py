n = sorted(input())

X = "abcdefghijklmnopqrstuvwxyz"
ans = sorted(list(set(X) - set(n)))
if len(ans) > 0:
    print(ans[0])
else:
    print("None")

# AC
"""
s = input()
for i in 'abcdefghijklmnopqrstuvwxyz':
  if i not in s:
    exit(print(i))
print("None")"""
