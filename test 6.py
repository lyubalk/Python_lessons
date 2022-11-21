"""Реализовать два небольших скрипта:
гитератор, генерирующий целые числа, начиная с указанного;
гитератор, повторяющий элементы некоторого списка,
определённого заранее.
Подсказка: используйте функцию count() и cycle() модуля
itertools. Обратите внимание, что создаваемый цикл не
должен быть бесконечным. Предусмотрите условие его авершения.
Например, в первом задании выводим целые числа,
начиная с 3. При достижении числа 10 — завершаем цикл.
Вторым пунктом необходимо предусмотреть условие, при
котором повторение элементов списка прекратится.
"""


from itertools import cycle, count

v_start = int(input('Введите стартовое число '))
v_stop = v_start * 2 + 10 + 1

# v.1
for i in count(v_start):
    if i < v_stop:
        print(i)
    else:
        break
del i

# v.2
my_list = [i for i in range(v_stop)]
count = 0
for b in cycle(my_list):
    if count < v_stop + 10:
        print(b)
        count += 1
    else:
        break
