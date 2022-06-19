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

# name = 'abrakadabra'
# print(name.replace("ab", ""))

# web_dict = {"title":"Web разраб",
# "duration":19,
# "mentors":["nicola", "alena", "alex", "aleksandr", ]}
# frontend_dict = {"title":"front", 
# "duration":13, "mentors":["coach_1", "coach_2", "coach_3"]}
# java_dict = {"title":"Java",
# "duration":11, "mentors":["coach_4","coach_5","coach_6"]}

# courses_list = [web_dict, frontend_dict, java_dict]
# max_count = 0
# course_id = None

# for id, course in enumerate(courses_list):
#     mentors_count = len(course["mentors"])
#     # print(f'На курсе {course["title"]} {mentors_count} преподавателей')
#     if mentors_count > max_count:
#         max_count = mentors_count
#         course_id = id
# max_course = courses_list[course_id]
# print(f'Самый крутой курс {max_course["title"]} потому что на нем {max_count} преподавателей')

# students_list = [
#     {"name": "Василий", "surname": "Теркин", "gender": "м", "program_exp": True, "grade": [8, 8, 9, 10, 9], "exam": 8},
#     {"name": "Мария", "surname": "Павлова", "gender": "ж", "program_exp": True, "grade": [7, 8, 9, 9], "exam": 9},
#     {"name": "Ирина", "surname": "Андреева", "gender": "ж", "program_exp": False, "grade": [10, 9, 8, 10, 10], "exam": 7},
#     {"name": "Татьяна", "surname": "Сидорова", "gender": "ж", "program_exp": False, "grade": [7, 9, 8],"exam": 10},
#     {"name": "Иван", "surname": "Васильев", "gender": "м", "program_exp": True, "grade": [9, 8, 9, 6, 9], "exam": 5},
#     {"name": "Роман", "surname": "Золотарев", "gender": "м", "program_exp": False, "grade": [8, 9, 9, 6, 9], "exam": 6}
# ]
# def get_avg_ex_grade(students):
#   sum_ex = 0
#   for student in students:
#     sum_ex += student['exam']
#   return round(sum_ex / len(students), 2)


# print(get_avg_ex_grade(students_list))

# def avd_hw_grade(students, exp):
#   sum_hw = 0
#   counter = 0
#   for student in students:
#     if student ['program_exp'] == exp:
#       sum_hw += sum(student['grade']) / len(student['grade'])
#       counter +=1
#   return round(sum_hw / counter, 2)


# print(avd_hw_grade(students_list, True))
# print(avd_hw_grade(students_list, False))

# def fire_student(students):
#   students_copy = students.copy()
#   for student in students_copy:
#     if sum(student['grade']) / len(student['grade']) < 8.5:
#       students.remove(student)


# fire_student(students_list)

# print(students_list)

documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
        {"type": "passport", "number": "5455 028765", "name": "Иван Иванов"},
        {"type": "passport", "number": "2212 645321", "name": "Петр Петров"},
        {"type": "passport", "number": "9215 900076", "name": "Василий Васильев"},
        {"type": "passport", "number": "4532 765987", "name": "Антон Куков"},
        {"type": "passport", "number": "987 654321", "name": "Михаил Фридман"},
        {"type": "invoice", "number": "13-7", "name": "Константин Пупкин"},
        {"type": "invoice", "number": "14-5", "name": "Олег Костин"}
]
directories = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006', '4532 765987', '13-7'],
        '3': ['2212 645321', '9215 900076', '14-5'],
        '4': ['987 654321'],
        '5': []
}



def search_people(documents):
  doc_numb =input("doc number?: ")
  for doc in documents:
    if doc_numb == doc['number']:
      return f' {doc["name"]} {doc["number"]}'
  else:
    print("no this document")



def shelf(directories):
  doc_numb = input("doc number?: ")
  for doc_place in directories:
    if doc_numb in directories[doc_place]:
      return f'{doc_numb} находится на полке {doc_place}'
  else:
    return "NO DOCUMENT"

def doc_list(documents):
  for doc in documents:
    print(doc["type"], doc["number"], doc["name"])

def main(documents):
  while True:
    comand = input("enter a comand: ")
    if comand == 'p':
      print(search_people(documents))
    elif comand == 's':
      print(shelf(directories))
    elif comand == 'l':
      print(doc_list(documents))
    elif comand == 'q':
      print('exit')
      break



main(documents)
