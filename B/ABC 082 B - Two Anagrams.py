s = str(input())
t = str(input())

X = ''.join(sorted(s))
Y = ''.join(sorted(t, reverse=True))

if X < Y:
    print("Yes")
else:
    print("No")

# AC
"""
アルゴリズムで引っかかった．
自由に並び替えていい→どっちかを弱く，どっちかを強くすることで判定を大きくできる．
"""
