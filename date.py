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

# from pydoc import doc


# documents = [
#         {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
#         {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
#         {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
#         {"type": "passport", "number": "5455 028765", "name": "Иван Иванов"},
#         {"type": "passport", "number": "2212 645321", "name": "Петр Петров"},
#         {"type": "passport", "number": "9215 900076", "name": "Василий Васильев"},
#         {"type": "passport", "number": "4532 765987", "name": "Антон Куков"},
#         {"type": "passport", "number": "987 654321", "name": "Михаил Фридман"},
#         {"type": "invoice", "number": "13-7", "name": "Константин Пупкин"},
#         {"type": "invoice", "number": "14-5", "name": "Олег Костин"}
# ]
# directories = {
#         '1': ['2207 876234', '11-2', '5455 028765'],
#         '2': ['10006', '4532 765987', '13-7'],
#         '3': ['2212 645321', '9215 900076', '14-5'],
#         '4': ['987 654321'],
#         '5': []
# }



# def search_people(documents):
#   doc_numb =input("doc number?: ")
#   for doc in documents:
#     if doc_numb == doc['number']:
#       return f' {doc["name"]} {doc["number"]}'
#   else:
#     print("no this document")



# def shelf(directories):
#   doc_numb = input("doc number?: ")
#   for doc_place in directories:
#     if doc_numb in directories[doc_place]:
#       return f'{doc_numb} находится на полке {doc_place}'
#   else:
#     return "NO DOCUMENT"

# def doc_list(documents):
#   for doc in documents:
#     print(doc["type"], doc["number"], doc["name"])

# def add_doc(documents):
#   type = input("type?: ")
#   number = input("number?: ")
#   name = input("name?: ")
#   place = input("enter place?: ")
#   my_dict = dict(type = type, number = number, name = name)
#   if place in directories:
#     directories[place].append(number)
#     documents.append(my_dict)
#   else:
#     print("Not this place")
#   print(documents)
#   print(directories)

# def doc_del(documents):
#   doc_numb = input("doc number?: ")
#   documents_copy = documents.copy()
#   for numb, doc in enumerate(documents_copy):
#     if doc_numb == doc['number']:
#       documents.remove(doc)
#       print(documents)
    

    



# def main(documents):
#   while True:
#     comand = input("enter a comand: ")
#     if comand == 'p':
#       print(search_people(documents))
#     elif comand == 's':
#       print(shelf(directories))
#     elif comand == 'l':
#       print(doc_list(documents))
#     elif comand == 'a':
#       print(add_doc(documents))
#     elif comand == 'd'
#       print(doc_del)
#     elif comand == 'q':
#       print('exit')
#       break



# main(documents)



# class Character:
#   name = 'x'
#   power = 0
#   energy = 100
#   hands = 2
# # print(Character.__dict__)

# peter = Character()


# peter.name = 'Peter Parker'
# peter.power = 70
# peter.alias = 'Spider-Man'

# # print(peter.__dict__)

# bruce = Character()
# bruce.name = 'Bruce Wayn'
# bruce.power = 80
# bruce.alias = 'Batman'

# class Character:
#   name = 'x'
#   power = 0
#   energy = 100
#   hands = 2
#   backpack = []

#   def eat(self, food):
#     if self.energy < 100:
#       self.energy += food
#     else:
#       print("No hungry")

#   def do_exercise(self, hours):
#     if self.energy > 0:
#       self.energy -= hours * 2
#       self.power += hours * 2 
#     else: 
#       print("Too tired")

#   def change_alias(self, new_alias):
#     print(self)
#     self.alias = new_alias


# bruce = Character()
# peter = Character()

# peter.backpack.append('Web-shooter')

# print(peter.backpack)
# print(bruce.backpack)


# bruce.name = 'Bruce Wayn'
# bruce.power = 80

# bruce.change_alias('Batman')

# print(bruce.power)
# print(bruce.energy)
# print()
# bruce.do_exercise(4)
# print(bruce.power)
# print(bruce.energy)
# print()
# bruce.do_exercise(8)
# print(bruce.power)
# print(bruce.energy)

# class Character:
#   def __init__(self, name, power, energy = 100, hands = 2):
#     self.name = name
#     self.power = power
#     self.energy = energy
#     self.backpasck = []
#     self.hands = 2

#   def eat(self, food):
#     if self.energy < 100:
#       self.energy += food
#     else:
#       print("No hungry")

#   def do_exercise(self, hours):
#     if self.energy > 0:
#       self.energy -= hours * 2
#       self.power += hours * 2 
#     else: 
#       print("Too tired")

#   def change_alias(self, new_alias):
#     print(self)
#     self.alias = new_alias

#   def beat_up(self, foe):
#     if not isinstance(foe, Character):
#       return
#     if foe.power < self.power:
#       foe.status = 'defeated'
#       self.status = 'winer'
#     else:
#       print ('Retreat')




# from unicodedata import name


# class Character:
#     name = 'xxx'
#     power = 0
#     energy = 100
#     hands = 2

# class Spider:
#     power = 0
#     energy = 50
#     hands = 8
    
#     def webshoot(self):
#         print('Pew-Pew!')

        
# class SpiderMan(Character, Spider):
#   pass


# peter_parker = SpiderMan
# print(peter_parker.name)


# class Character:
#     # перенесем все в init
#      def __init__(self, name, power, energy=100, hands=2):
#         self.name = name
#         self.power = power
#         self.energy = energy
#         self.hands = hands
    

# class Spider:
#     def __init__(self, power, energy=50, hands=8):
#         self.power = power
#         self.energy = energy
#         self.hands = hands
    
#     def webshoot(self):
#         print('Pew-Pew!')

        
    
# class SpiderMan(Character, Spider):
#     def turn_spider_sense(self):
#         self.energy -= 10
#         self.power += 20

              
        
# peter_parker = SpiderMan('Peter Parker', 80)
# print(peter_parker.energy)
# print(peter_parker.power)
# print(peter_parker.hands)
# peter_parker.turn_spider_sense()
# print(peter_parker.energy)
# print(peter_parker.power)



class Character:
    def __init__(self, name, power, energy=100, hands=2):
        self.name = name
        self.power = power
        self.energy = energy
        self.hands = hands

    def move(self):
        print('Moving on 2 squares')
    
    def attack(self, foe):
        foe.health -= 10
        
        
class Spider:
    def __init__(self, power, energy=50, hands=8):
        self.power = power
        self.energy = energy
        self.hands = hands
    
    def webshoot(self):
        print('Pew-Pew!')
    
    def move(self):
        self.webshoot()
        print('Moving on 1 square')   
        
    def attack(self, foe):
        foe.status = 'stunned'
    
    
class SpiderMan(Character, Spider):
    def __init__(self, name, power):
        super().__init__(name, power)
        self.backpack = []
        
    def turn_spider_sense(self):
        self.energy -= 10
        self.power += 20
    
    def webshoot(self):
        if 'web' in self.backpack:
            super().webshoot() 
        else:
            print('No web!')

    def move(self):
        self.webshoot()
        print('Moving on 3 square')
        
    def attack(self, foe):
        super().attack(foe)
        Spider.attack(self, foe)
        
#     добавим возможность сравнения персонажей 
    def __lt__(self, other):
        if not isinstance(other, Character):
            print('Not a Character!')
            return
        return self.power < other.power
    
    def __str__(self):
        res = f'Сила персонажа = {self.power}'
        return res
    
    
peter_parker = SpiderMan('Peter Parker', 80)
miles_morales = SpiderMan('Miles Morales', 80)

print(peter_parker < miles_morales)
# и даже "больше" будет работать!
# print(peter_parker > miles_morales)
# peter_parker.__lt__(miles_morales)

print(peter_parker)


