f = open('a.txt', 'r', encoding='utf-8')

print(next(f))
# print(f.__next__())
f.close()
