"""Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды
и выведите в формате чч:мм:сс.
Используйте форматирование строк."""

time = int(input('Введите время в секундах >>> '))

if time > 90000:
    year = time // 31622400
    month = (time % 31622400) // 2419200
    day = (time % 2419200) // 86400
    hour = (time % 86400) // 3600
    minute = (time % 3600) // 60
    second = (time % 3600) % 60
    print(f'Год: {year}, '
          f'\nМесяц: {month},'
          f'\nДней: {day},'
          f'\nЧас: {hour},'
          f'\nМинут: {minute},'
          f'\nСекунд: {second}')
else:
    hour = time // 3600
    minute = (time % 3600) // 60
    second = (time % 3600) % 60
    print(f'Время: {hour} : {minute} : {second}')
