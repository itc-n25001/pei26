a = 17
b = 5
dm = divmod(a, b)
p = pow(dm[0], dm[1])
all_num = [a, b, dm[0], dm[1], p]
min_all = min(all_num)
max_all = max(all_num)
sum_all = sum(all_num)
print(f'{min_all}, {max_all}, {sum_all}')


"""
divmod()関数とは商と余りを同時に求める関数です。
pow()関数とは累乗(べき乗)を求める関数です。
min()関数とは最小値を求める関数です。
max()関数とは最大値を求める関数です。
sum()関数とは合計を求める関数です。
"""