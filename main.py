# simple calculator

operations = {'+': "Сложение:", '-': "Вычитание:", '*': "Умножение:", '/': "Деление:"}


def get_num(prompt):
    while True:
        try:
            num = float(input(prompt))
            return num
        except ValueError:
            print("Ошибка - введено некорректное число")


def calc(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    else:
        try:
            return num1 / num2
        except ZeroDivisionError:
            print("На ноль пока делить нельзя\n")
            main('/')


def main(operator):
    print('# ' + operations[operator])
    var1 = get_num("Введите первое число: ")
    var2 = get_num("Введите второе число: ")
    result = calc(var1, var2, operator)
    if result is not None:
        print(f"Результат {operations[operator][:-2]}я: {result} \n")


for ops in operations:
    main(ops)
