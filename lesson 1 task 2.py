x = input('Введите координаты x вида: a b ').split()
y = input('Введите координаты y вида: a b ').split()
if len(x) == 2 and len(y) == 2:
    k = (int(y[0]) - int(y[1])) / (int(x[0]) - int(x[1]))
    b = int(y[1]) - k * int(x[1])
    # y[0] = k * x[0] + b
    # y[1] = k * x[1] + b
    print(f'y = {k} * x + {b}')
