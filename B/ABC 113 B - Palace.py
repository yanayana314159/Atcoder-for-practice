N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))
diff_list = []


for i, h in enumerate(H):
    temp = T-h*0.006
    diff = abs(temp-A)
    diff_list.append(diff)

# print(diff_list)
print(diff_list.index(min(diff_list))+1)

# AC
"""回答例
N = int(input())
T, A = [int(x) for x in input().split()]
diff = [abs(A - T + (int(x) * 0.006)) for x in input().split()]
print(diff.index(min(diff)) + 1)
"""
