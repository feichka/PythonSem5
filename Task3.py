# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

with open('input.txt','r') as str:
    print('Входные данные:')
    dt = str.read().split()
    print(dt)
from collections import Counter
c = list(dt.count(dt[i]) for i in range(len(dt)))
d = list(zip(dt,c))
print(d)


