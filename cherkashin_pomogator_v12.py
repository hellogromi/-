print("Здравствуйте! Hello!")
print("Какой язык выберете? What language will you chosse?")
print('Русский = "р" English = "e"')
language = input()
if language == "р":
    answer = input("начнём?:", )
    if answer == "да" or answer == "д":
        print('Здравствуйте, вас приветствует "помогатор"')
        print('Помогатор умеет складывать, вычитать, умножать, делить, целочисленно делить, возводить в степень одно число в другое, вычислять квадратный корень из числа, искать остаток, переводить в десятичную систему счисления, производить анализ числа ')
elif language == "e":
    answer = input("let's start?:", )
    if answer == "yes" or answer == "y":
        print('Hello, you are welcomed by the "helper"')
        print('The "helper" can add, subtract, multiply, divide, divide integers, exponentiate one number into another, calculate the square root of a number, look for the remainder')    
else:
    print("Такого языка не добавленно")
    print("No such language has been added")
while answer == "да" or answer == "yes" or answer == "y" or answer == "д":
    if language == "Р":
        print('~ сложение: +')
        print('~ вычитание: -')
        print('~ умножение: *')
        print('~ деление: /')
        print('~ степень: **')
        print('~ квадратный корень: ^')
        print('~ целочисленное деление: //')
        print('~ взятие остатка: %')
        print('~ перевод в десятичную систему счисления: 10')
        print('~ анализ: ?')
        a = int(input("число 1:", ))
        b = input("знак действия:", )
        e = a ** 0.5
        if b == "+" or b == "-" or b == "*" or b == "/" or b == "**" or b == "//" or b == "%" or b == "10":
            c = int(input("число 2:", ))
            if b == "+":
                print(a + c)
            elif b == "-":
                print(a - c)
            elif b == "*":
                print(a * c)
            elif b == "/" and c != 0:
                print(a / c)
                if c == 0:
                    print("на ноль делить нельзя")
            elif b == "//":
                print(a // c)
            elif b == "**":
                print(a ** c)
            elif b == "%":
                print(a % c)
            elif b == "10":
                print(int(str(a), c))
        elif b == "^":
            print(a ** (1 / 2))
        elif b == "?":
            print("количество разрядов:", len(str(a)))
            if (a % 2) == "0":
                print("четное")
            else:
                print("Нечетное")
            if "." not in e:
                print("является полным квадратом числа", e)
            else:
                print("не является полным квадратом")
        answer = input("Желаете продолжить?")        
    else:
        print('~ addition: +')
        print('~ subtraction: -')
        print('~ multiplication: *')
        print('~ division: /')
        print('~ degree: **')
        print('~ square root: ^')
        print('~ integer division: //')
        print('~ taking the remainder: %')
        print('~ to the decimal number system: 10') 
        print('~ analysis: ?')
        a = int(input("number 1:", ))
        b = input("action sign:", )
        e = a * a
        d = a * a * a
        if b == "+" or b == "-" or b == "*" or b == "/" or b == "**" or b == "//" or b == "%" or b == "10":
            c = int(input("number 2:", ))
            if b == "+":
                print(a + c)
            elif b == "-":
                print(a - c)
            elif b == "*":
                print(a * c)
            elif b == "/" and c != 0:
                print(a / c)
                if c == 0:
                    print("you can't divide by zero")
            elif b == "**":
                print(a ** c)
            elif b == "//":
                print(a // c)
            elif b == "%":
                print(a % c)
            elif b == "10":
                print(int(str(a), c))
        elif b == "^":
            print(a ** (1 / 2))
        elif b == "?":
            print("number of digits:", len(str(a)))
            if (a % 2) == "0":
                print("even")
            else:
                print("Odd")
            if "." not in str(e):
                print("is the full square of the number", e)
            else:
                print("is not the full square of the number")
        answer = input("Do you want to continue:", )
if language == "р":
    print("Пока")
elif language == "e":
    print("Good bye!")
