a = int(input("Введите число а: "))
b = int(input("Введите число b: "))
c = input('''Введите знак операции:
    "+" = плюс
    "-" = минус
    "*" = умножить
    "/" = разделить
''')
d = 0
match c:
    case "+":
        d = a + b
        print(f"{a} {c} {b} = {d}")
    case '-':
        d = a - b
        print(f"{a} {c} {b} = {d}")
    case '*':
        d = a * b
        print(f"{a} {c} {b} = {d}")
    case '/':
        d = a / b
        print(f"{a} {c} {b} = {d}")
    