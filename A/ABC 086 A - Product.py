# スペース区切りの整数の入力
a, b = map(int, input().split())

"""
map()関数は、第1引数に関数、第2引数にリストやイテラブルオブジェクトを受け取り、そのリストの各要素に対して、指定された関数を適用した結果を新しいイテラブルオブジェクトとして返します。
"""
if a*b % 2 == 0:
    print("Even")
else:
    print("Odd")

# AC
