N = int(input())
A = int(input())
# 500円を使えるだけ使う
rest = N % 500

if rest <= A:
    print("Yes")
else:
    print("No")


"""
N
A
の入力形と
N Aの入力形は別
"""
# AC
