N = int(input())
A = "No"

mult_list = []
Numlist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(1, 10):
    mult_list.append(list(map(lambda x: i*x, Numlist)))
flat_list = []
for sublist in mult_list:
    flat_list.extend(sublist)

if N in flat_list:
    A = "Yes"


print(A)

# AC 冗長な気がする
"""　回答例　面白みはない
N = int(input())
 
ans = False
 
for i in range(1,10):
    for j in range(1, 10):
        if i * j == N:
            ans = True
 
if ans:
    print("Yes")
else:
    print("No")

#可読性高いコード
N = int(input())
for i in range(1, 10):  
    if not N%i and N//i < 10:
    not N % i は、N % i の結果が 0 でない場合に True、0 の場合に False を返します。not は、論理 NOT 演算子であり、True を False に、False を True に反転させる働きがあります。
    例えば、N が 10、i が 3 の場合を考えます。N % i は 1 となります。not N % i は not 1 と同じで、False となります。この場合、条件式は False and N // i < 10 となり、if文の中の処理が実行されません
        print("Yes")
        exit()
print("No")

    
"""
