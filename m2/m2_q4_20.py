num =3
list_a = []
while num < 5:
    for i in range(num, 10, 3):
        i -= 6
        list_a.append(i)
    num += 1
print(sum(list_a))

"""計算機
num = 3 のときのforループ処理
3, 6, 9それぞれ-6してappendするので[-3, 0, 3]となる

num = 4 のときのforループ処理
4, 7それぞれ-6してappendするので[-2, 1]となる

最終的にlist_aの内容はsum([-3, 0, 3, -2, 1]) = -1
"""