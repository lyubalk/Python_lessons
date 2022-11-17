"""Пользователь вводит месяц в виде целого
числа от 1 до 12. Сообщить, к какому времени
года относится месяц (зима, весна, лето, осень).
Напишите решения через list и dict. """

my_list = ['Зима', 'Весна', 'Лето', 'Осень']

my_dict = {1: 'Зима', 2: 'Весна',
           3: 'Лето', 4: 'Осень'}

seasons = abs(int(input('Введите номер месяца >>> ')))
if seasons == 1 or seasons == 2 or seasons == 12:
    print(my_dict.get(1))
    print(my_list[0])
elif seasons == 3 or seasons == 4 or seasons == 5:
    print(my_dict.get(2))
    print(my_list[1])
elif seasons == 6 or seasons == 7 or seasons == 8:
    print(my_dict.get(3))
    print(my_list[2])
elif seasons == 9 or seasons == 10 or seasons == 11:
    print(my_dict.get(4))
    print(my_list[3])
else:
    print('Такого месяца не существует!')
