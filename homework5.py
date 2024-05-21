my_list = ['апельсин', 'банан', 'яблоко', 'киви', 'хурма']
print('Список: ', my_list)
print('Первый элемент: ', my_list[0], '\nПоследний элемент: ', my_list[len(my_list) - 1],
      '\nПодсписок с третьего до пятого элементов: ', my_list[2:6])
my_list[2] = 'груша'
print('Изменённый список: ', my_list)
my_dict = {'апельсин': 'orange', 'банан': 'banana', 'яблоко': 'apple', 'киви': 'kiwi', 'хурма': 'persimmon'}
print('Словарь: ', my_dict)
print('Значение заданного ключа: ', my_dict['банан'])
my_dict['груша'] = 'pear'
my_dict['апельсин'] = 'fruit'
print('Изменённый словарь: ', my_dict)