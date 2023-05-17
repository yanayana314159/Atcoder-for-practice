A = int(input())
B = int(input())
C = int(input())
X = int(input())

solution = 0

for a in range(0, A+1):
    rest = X-500*a
    if rest == 0:
        solution += 1
        # print(f"aは{a}")
    elif rest > 0:
        # print(f"aは{a},残りは{rest}")
        for b in range(0, B+1):
            restb = rest-100*b
            if restb == 0:
                solution += 1
                # print(f"aは{a},bは{b}")
            elif restb > 0:
                for c in range(0, C+1):
                    restc = restb-50*c
                    if restc == 0:
                        solution += 1
                        # print(f"aは{a},bは{b},cは{c}")


print(solution)
# AC
"""解答例
 
for i in range(A+1):
    for j in range(B+1):
        for k in range(C+1):
            sum = 500*i+100*j+50*k
            if sum==X:
                ans += 1
 
print(ans)
"""
