animals = ['Dog', 'Cat', 'Rabbit', 'Horse', 'Dolphin']
total = 0
for animal in animals:
    from_D = animal.startswith('D')
    is_long = len(animal) > 5
    if from_D and is_long:
        break
    elif not from_D and is_long:
        total += animal.find('b')
    else:
        total += len(animal)
print(total)



"""
startswith()関数とは文字列が指定した文字で始まるかどうかを判定する関数です。
今回はanimal.startswith('D')で、animalが'D'で始まればTrueを返します。そうじゃないならFalseを返します。
find()関数とは文字列の中から指定した文字が最初に出てくる位置を返す関数です。

"""