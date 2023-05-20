h, w = map(int, input().split())
N = []
ans = []
[N.append(str(input())) for i in range(h)]

for i in range(h):
    for j in range(w):
        if N[i][j] == "s":
            # 右
            if w-j >= 5:
                if "".join(N[i][j]+N[i][j+1]+N[i][j+2]+N[i][j+3]+N[i][j+4]) == "snuke":
                    [print(i+1, j+k+1) for k in range(5)]
                    break
                if h-i >= 5:  # 右下
                    if "".join(N[i][j]+N[i+1][j+1]+N[i+2][j+2]+N[i+3][j+3]+N[i+4][j+4]) == "snuke":
                        [print(i+k+1, j+k+1) for k in range(5)]
                        break
                if i >= 4:  # 右上
                    if "".join(N[i][j]+N[i-1][j+1] +
                               N[i-2][j+2]+N[i-3][j+3]+N[i-4][j+4]) == "snuke":
                        [print(i-k+1, j+k+1) for k in range(5)]
                        break

            if j >= 4:  # 左
                if "".join(N[i][j]+N[i][j-1]+N[i][j-2]+N[i][j-3]+N[i][j-4]) == "snuke":
                    [print(i+1, j-k+1) for k in range(5)]
                    break
                # 左下
                if h-i >= 5:
                    if "".join(N[i][j]+N[i+1][j-1]+N[i+2][j-2]+N[i+3][j-3]+N[i+4][j-4]) == "snuke":
                        [print(i+k+1, j-k+1) for k in range(5)]
                        break
                # 左上
                if i >= 4:
                    if "".join(N[i][j]+N[i-1][j-1] +
                               N[i-2][j-2]+N[i-3][j-3]+N[i-4][j-4]) == "snuke":
                        [print(i-k+1, j-k+1) for k in range(5)]
                        break

            # 下
            if h-i >= 5:
                if "".join(N[i][j]+N[i+1][j]+N[i+2][j]+N[i+3][j]+N[i+4][j]) == "snuke":
                    [print(i+k+1, j+1) for k in range(5)]
                    break
            # 上
            if i >= 4:
                if "".join(N[i][j]+N[i-1][j]+N[i-2][j]+N[i-3][j]+N[i-4][j]) == "snuke":
                    [print(i-k+1, j+1) for k in range(5)]
                    break

# AC

"""回答例

こういう問題苦手，紙とペン使えばよかった
H, W = map(int, input().split())
 
S = [list(input()) for _ in range(H)]
# print(H, W, S)
 
# "snuke" という文字列が一直線上に存在する箇所の座標を出力する関数
for i in range(H):
    for j in range(W):
        if S[i][j] != "s":
            continue
        if S[i][j] == "s":
            # 以下、"s" が存在する場合の処理。周囲の8マスを調べる。
 
            # 右方向に調べる場合
            if j+4 <= W-1:
                if [S[i][j+1], S[i][j+2], S[i][j+3], S[i][j+4]] == ["n", "u", "k", "e"]:
                    for k in range(5):
                        print(i+1, j+k+1)
            
            # 左方向に調べる場合
            if j-4 >= 0:
                if [S[i][j-4], S[i][j-3], S[i][j-2], S[i][j-1]] == ["e", "k", "u", "n"]:
                    for k in range(5):
                        print(i+1, j-k+1)
 
            # 上方向に調べる場合
            if i-4 >= 0:
                if [S[i-4][j], S[i-3][j], S[i-2][j], S[i-1][j]] == ["e", "k", "u", "n"]:
                    for k in range(5):
                        print(i-k+1, j+1)
            
            # 下方向に調べる場合
            if i+4 <= H-1:
                if [S[i+1][j], S[i+2][j], S[i+3][j], S[i+4][j]] == ["n", "u", "k", "e"]:
                    for k in range(5):
                        print(i+k+1, j+1)
 
            # 右上方向に調べる場合
            if i-4 >= 0 and j+4 <= W-1:
                if [S[i-4][j+4], S[i-3][j+3], S[i-2][j+2], S[i-1][j+1]] == ["e", "k", "u", "n"]:
                    for k in range(5):
                        print(i-k+1, j+k+1)
            
            # 左上方向に調べる場合
            if i-4 >= 0 and j-4 >= 0:
                if [S[i-4][j-4], S[i-3][j-3], S[i-2][j-2], S[i-1][j-1]] == ["e", "k", "u", "n"]:
                    for k in range(5):
                        print(i-k+1, j-k+1)
            
            # 右下方向に調べる場合
            if i+4 <= H-1 and j+4 <= W-1:
                if [S[i+1][j+1], S[i+2][j+2], S[i+3][j+3], S[i+4][j+4]] == ["n", "u", "k", "e"]:
                    for k in range(5):
                        print(i+k+1, j+k+1)
 
            # 左下方向に調べる場合
            if i+4 <= H-1 and j-4 >= 0:
                if [S[i+1][j-1], S[i+2][j-2], S[i+3][j-3], S[i+4][j-4]] == ["n", "u", "k", "e"]:
                    for k in range(5):
                        print(i+k+1, j-k+1)
"""
