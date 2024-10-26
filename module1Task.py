from time import sleep
empty_list = []
while True:
    user_input = int(input('Число: '))
    if user_input != 0:
        empty_list.append(user_input)
        sleep(4)
    else:
        break
print(f'Введенные числа: {empty_list}')
sum_list = sum(empty_list)
print(f'Сумма чисел: {sum_list}')

