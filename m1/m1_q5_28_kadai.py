days = ['月','月','火','水','木','金','金']

days.remove('月')
days.remove('金')

days.insert(0, '日')
days.insert(6, '土')

print(days)
