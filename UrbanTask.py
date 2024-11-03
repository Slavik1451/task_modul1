# словарь:
my_dict = {'Slava': 2000, 'Anton': 2001, 'Marina': 1998}
print(my_dict)
print(my_dict['Slava'])
print(my_dict.get('Kolya', 'Такого ключа нет'))
my_dict.update({'Alena': 2001, 'Igor': 1997})
print(my_dict['Alena'])
removed_value = my_dict.pop('Marina')
print(f'Удалено: Marina - {removed_value} \n{my_dict}')

# множества:
my_set = {1, 1, 2, 2, 3, 3, 33}
print(my_set)
my_set.add(4)
my_set.add(35)
my_set.remove(33)
print(my_set)
