num = 12
list_s= []
s = 2
while s <= num:
    if num % s == 0:
        num //= s
        if s not in list_s:
            list_s.append(s)

    else:
        s += 1
print(list_s)

"""
ループ1：num = 6 list_s = [2] s = 2
ループ2：num = 3 list_s = [2] s = 2
ループ3：num = 3 list_s = [2] s = 3
ループ4：num = 1 list_s = [2, 3] s = 3
while 3 <= 1はFalseなのでループ終了
答えは[2, 3]"""