import math

# Ввод данных
a = float(input('Введите первое число: '))
b = float(input("Введите второе число: "))
operation = input('Введите операцию: ')

# Выполнение операции
if operation == '+':
    result = a + b
elif operation == '-':
    result = a - b
elif operation == '*':
    result = a * b
elif operation == '/':
    if b != 0:
        result = a / b
    else:
        result = 'Ошибка: деление на ноль'
elif operation == 'pow':
    result = a ** b
elif operation == 'sqrt':
    result = (math.sqrt(a), math.sqrt(b))
else:
    result = 'Неизвестная операция'

# Вывод результата
print(f'Результат: {result}')
