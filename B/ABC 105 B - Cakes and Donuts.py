N = int(input())

max4 = int(N/4)
max7 = int(N/7)
A = "No"

for i in range(0, max7+1):
    rest = N-7*i
    if rest % 4 == 0:
        A = "Yes"

print(A)
# AC
"""
range関数に少し引っかかった
range(0, 5)
--> 0 1 2 3 4
割り算して，少数点以下切り捨てなので気をつけなければならない．
"""
