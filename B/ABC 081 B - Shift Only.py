N = int(input())
A = list(map(int, input().split()))  # 数字が格納されたリスト
B = sum(map(lambda x: x % 2, A))  # 余りを足した数，1以上になった場合には割り算を止める

i = 0
while B == 0:
    A = list(map(lambda x: x / 2, A))

    B = sum(map(lambda x: x % 2, A))
    i += 1


else:
    print(i)

# AC
"""
A = list(map(lambda x: x / 2, A))を
A = map(lambda x: x / 2, A)としていたことでAに返り値が入らず，無限ループを起こしていた．そのことに気が付かなかったため時間がかかった．
mapを使う時には注意
"""
