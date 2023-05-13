N = str(input())
sum = 0
"""
print(f"1番目は{N[0]}")
print(f"2番目は{N[1]}")
print(f"3番目は{N[2]}")
"""

if int(N[0]) == 1:
    sum = sum+1
if int(N[1]) == 1:
    sum = sum+1
if int(N[2]) == 1:
    sum = sum+1

print(int(sum))

# AC sum += 1
"""回答例(chatgpt)
N = input()
sum = 0

for i in range(len(N)):
    if N[i] == '1':
        sum += 1

print(sum)
"""
