# boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard', 'Tom']
# girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
# if len(boys) == len(girls):
#     print("best")
#     for boy, girl in zip(sorted(boys), sorted(girls)):
#         print(boy, "and", girl)
# else:
#     print("no comment")
#     print()


# persons= int(input("quantity people"))
# cook_book = [
#   ['салат',
#       [
#         ['картофель', 100, 'гр.'],
#         ['морковь', 50, 'гр.'],
#         ['огурцы', 50, 'гр.'],
#         ['горошек', 30, 'гр.'],
#         ['майонез', 70, 'мл.'],
#       ]
#   ],
#   ['пицца',  
#       [
#         ['сыр', 50, 'гр.'],
#         ['томаты', 50, 'гр.'],
#         ['тесто', 100, 'гр.'],
#         ['бекон', 30, 'гр.'],
#         ['колбаса', 30, 'гр.'],
#         ['грибы', 20, 'гр.'],
#       ],
#   ],
#   ['фруктовый десерт',
#       [
#         ['хурма', 60, 'гр.'],
#         ['киви', 60, 'гр.'],
#         ['творог', 60, 'гр.'],
#         ['сахар', 10, 'гр.'],
#         ['мед', 50, 'мл.'],  
#       ]
#   ]
# ]
# for menu, names in cook_book:
#     print(f'{menu.capitalize()}')
#     for ingredients, weigth, gramm in names:
#         print(f'{ingredients}, {weigth * persons}, {gramm}')
# print()

# geo_logs = [
#     {'visit1': ['Москва', 'Россия']},
#     {'visit2': ['Дели', 'Индия']},
#     {'visit3': ['Владимир', 'Россия']},
#     {'visit4': ['Лиссабон', 'Португалия']},
#     {'visit5': ['Париж', 'Франция']},
#     {'visit6': ['Лиссабон', 'Португалия']},
#     {'visit7': ['Тула', 'Россия']},
#     {'visit8': ['Тула', 'Россия']},
#     {'visit9': ['Курск', 'Россия']},
#     {'visit10': ['Архангельск', 'Россия']}
# ]
# for geo in geo_logs:
#     if list(geo.values())[0][1] == 'Россия':
#         print(geo)

name = 'abrakadabra'
print(name.replace("ab", ""))




