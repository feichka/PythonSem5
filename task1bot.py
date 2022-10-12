print('На столе лежит 2021 конфета. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. ')
s = 150
while s> 0:
    x = int(input('Игрок 1, сколько конфет от 1 до 28 Вы возьмете? '))
    if x > 28:
        print('Неверное количество. Попробуйте еще раз')
    else:
        res = s-x
        print(res)
        if res <= 28:
            print('Бот выиграл и забрал у тебя все конфеты!')
            break
        elif res>=58:
            y = 29-x
            print('Я возьму', y)
            res = res - y
            s = res
            print(res)
        elif 57 <res:
            y = res-57
            print('Я возьму', y)
            res = res - y
            s = res
            print(res)
            if res<=28:
                print('Игрок 1, вы выиграли!')
                break
        elif res < 58:
            y = res-29
            print('Я возьму', y)
            res = res - y
            s = res
            print(res)


