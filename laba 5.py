def lab51():
num = int(num)
x = [5, 7, 4, 1, 5358979323846264331415926]
if num in x:
    print(x, '\n', 'Поздравляю, Вы угадали число!')
else:
    print(x, '\n', 'Нет такого числа!')


def lab52():
    x = [2, 1, 5, 6, 7, 8, 5, 2]
    for i in x:
        if x.count(i) >= 2:
            print(i)


def lab53():
    week = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sun', 'Sut')
    weekends = int(input())
    print('Weekends:', week[:-weekends - 1:-1])
    print('Work days:', week[:-weekends])


def lab54():
    import random
    group1 = ['Петров', 'Сидоров', 'Кузнецов', 'Васильев', 'Зайцев', 'Баранов', 'Лебедев', 'Газизов', 'Муравьев',
              'Семенов']
    group2 = ['Никулин', 'Федоров', 'Лапин', 'Котов', 'Гусев', 'Попов', 'Титов', 'Жуков', 'Панов', 'Иванов']

    team = tuple(random.sample(group1, 5) + random.sample(group2, 5))


    print("Группа 1:", group1)
    print("Группа 2:", group2)
    print("Спортивная команда:", team)

    print("Длина спортивной команды:", len(team))

    sorted_team = tuple(sorted(team))
    print("Отсортированная спортивная команда:", sorted_team)

    ivanov_count = team.count('Иванов')
    print(f'Студент "Иванов" входит в команду: {"да" if ivanov_count > 0 else "нет"}')
    print("Количество раз фамилия 'Иванов' встречается в кортеже:", ivanov_count)