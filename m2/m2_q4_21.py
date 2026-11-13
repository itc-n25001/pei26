list_a = [4, 8, 3, 7, 9]
list_b = [10, 3, 6, 7, 2]
list_c = []
i = 0
while i < 5:
    if list_a[i] > list_b[i]:
        list_c.append(list_a[i] - list_b[i] ** 2)
    elif list_a[i] == list_b[i]:
        list_c.append(list_a[i] * 2 % 4)
    else:
        list_c.append((list_b[i] - list_a[i]) // 2)
    i += 1
print(max(list_c))

"""計算機
算術演算子の優先順位
**: べき乗 3 ** 2 = 9
%: 余り 14 % 4 = 2
//: 商のn小数点以下切り捨て 3 // 2 = 1
※優先順位も気をつけましょう
**が最優先, *, /, //, %は同じ優先順位で左から計算する、その後に+, -を計算

4と10: (4 -10) // 2 = 3
8と3: 8 - 3 ** 2 = -1
3と6: (6 - 3) // 2 = 1
7と7: 7 * 2 % 4 = 2
9と2: 9 - 2 ** 2 = 5
なのでmax([-3, -1, 1, 2, 5]) = 5
"""