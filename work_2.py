import fractions

# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. 
# Функцию hex используйте для проверки своего результата.

# num = int(input('Введите целое число: '))
# print(hex(num))

# res_str = ''
# while num > 0:
#     remainder = num % 16
#     if remainder < 10:
#         res_str = str(remainder) + res_str
#     else:
#         res_str = chr(ord('a') + remainder - 10) + res_str
#     num //= 16

# print(f"Шестнадцатеричное представление числа: {res_str}")

###########################################################################################3

# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
# Программа должна возвращать сумму и произведение* дробей. 
# Для проверки своего кода используйте модуль fractions.

fraction_1 = str(input('Введите первую дробь чеоез /:  '))
fraction_2 = str(input('Введите вторую дробь чеоез /:  '))

numerator_1, denominator_1 = fraction_1.split('/')
numerator_1 = int(numerator_1)
denominator_1 = int(denominator_1)

numerator_2, denominator_2 = fraction_2.split('/')
numerator_2 = int(numerator_2)
denominator_2 = int(denominator_2)
print(numerator_1, denominator_1, numerator_2, denominator_2)
sum_numerator = numerator_1 * denominator_2 + numerator_2 * denominator_1
sum_denominator = denominator_1 * denominator_2
print('Сумма дробей = ', sum_numerator, '/', sum_denominator)

composition_1 = numerator_1 * numerator_2
composition_2 = denominator_1 * denominator_2
print('Произведение дробей = ', composition_1, '/', composition_2) 

f1 = fractions.Fraction(composition_1, denominator_1)
f2 = fractions.Fraction(numerator_2, denominator_2)
print('Сумма = ', f1 + f2)
print('Поизведение = ', f1 * f2)

# Ответы почему то не совпадают, вроде всё верно сделал.



