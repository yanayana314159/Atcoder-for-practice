import sys
import math

def main():
    h, a,b = map(int, input().split())
    i=0

    if h<=a:
        ans="YES"
        print(ans)
        print(1)
    
    else:
        if a<=b:
            ans="NO"
            print(ans)
        else:
        # ターン数の計算を行う
            turns_to_defeat = math.ceil((h - a) / (a - b))+1
        
        # 必要なターン数が1より小さい場合は1ターンで倒せる
            turns_to_defeat = max(turns_to_defeat, 1)
        
        # 残りHPを計算して結果を表示
            print("YES")
            print(turns_to_defeat)
            


if __name__ == '__main__':
    main()
    