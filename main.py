#Этот код определяет класс Person с тремя атрибутами: идентификатор,
# имя и возраст.
class Person:
    id: int
    name: str
    age: int
# Метод init инициализирует атрибуты
# объекта значениями,
# переданными конструктору.
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age
#Этот код определяет класс Group с двумя атрибутами: id и name.
# Метод init инициализирует атрибуты объекта значениями, переданными конструктору.
class Group:
    id: int
    name: str

    def __init__(self, id, name):
        self.id = id
        self.name = name
#Этот код определяет класс Skill с одним атрибутом: skill_title.
# Метод init инициализирует атрибут объекта значением, переданным конструктору.
class Skill:
    skill_title: str

    def __init__(self, title):
        self.skill_title = title
#Этот код определяет класс Skill с одним атрибутом: skill_title.
#Метод init инициализирует атрибут объекта значением, переданным конструктору.
class Student(Person, Skill):
    student_id: int
    group_id: int

    def __init__(self, person_id, name, age, student_id, group_id, skill_title):
        super().__init__(person_id, name, age)
        super(Skill, self).__init__(skill_title)
        self.student_id = student_id
        self.group_id = group_id

    def say_hell(self):
        print('hello')

#Этот код создает объект Student и присваивает его переменной student.  Метод student.say_hell()
#печатает строку «привет».
student = Student(1, "Petya", 16, 12, 1)
student.say_hell()

#Этот код определяет класс Teacher, который наследуется от класса Person.  Атрибуты
#Teacher_id, group_id и subject_description относятся к учителям.
#Метод init инициализирует атрибуты объекта значениями, переданными конструктору.
class Teacher(Person):
    teacher_id: int
    group_id: int
    subject_description: str

    def __init__(self, person_id, name, age, teacher_id, group_id, subject_description):
        super().__init__(person_id, name, age)
        self.teacher_id = teacher_id
        self.group_id = group_id
        self.subject_description = subject_description

#Этот код определяет класс Grade с шестью атрибутами: entry_id, group_id,
#subject_id, student_id, Teacher_id иgrade_level.
#Метод init инициализирует атрибуты объекта значениями, переданными конструктору.
class Grade:
    entry_id: int
    group_id: int
    subject_id: int
    student_id: int
    teacher_id: int
    grade_level: int

    def __init__(self, entry_id, group_id, subject_id, student_id, teacher_id, grade_level):
        self.entry_id = entry_id
        self.group_id = group_id
        self.subject_id = subject_id
        self.student_id = student_id
        self.teacher_id = teacher_id
        self.grade_level = grade_level

#Первая строка кода определяет класс Subject. Класс Subject имеет два атрибута: id и name.
# Атрибут id — это уникальный идентификатор субъекта, а атрибут name — имя субъекта.
class Subject:
    id: int
    name: str

    def __init__(self, id, name):
        self.id = id
        self.name = name

#Вторая строка кода определяет класс StudentJournal. У класса StudentJournal есть
# три атрибута: student_list, Teacher_list и оценки. Атрибут student_list — это список студентов в журнале, атрибут Teacher_list — это список учителей
# в журнале, а атрибутgrade — словарь оценок для каждого учащегося.
class StudentJournal:
    student_list = []
    teacher_list = []
    grades = dict()

    def add_student(self, student: Student):
        self.student_list.append(student)

    def add_teacher(self, teacher: Teacher):
        self.student_list.append(teacher)

    def add_grade(self, student, subject, grade):
        self.grades[student.student_id] = {
            'student_name': student.name,
            'subject': subject.name,
            'grade': grade.grade_level,
        }

    def draw_report(self):
        for student in self.grades.values():
            print(student)


group = Group(1, "9-A")
teacher = Teacher(1, "Teacher", 34, 1, group.id, "Math")
student = Student(2, "Shoaziz", 25, 1, group.id)
jounal = StudentJournal()
jounal.add_student(student)
jounal.add_teacher(teacher)
subject = Subject(1, "History")
grade = Grade(1, group.id, subject.id, student.student_id, teacher.teacher_id, 5)
jounal.add_grade(student, subject, grade)
jounal.draw_report()



#Первая строка кода определяет класс Subject. Класс Subject имеет два атрибута: id и name. Атрибут id — это уникальный идентификатор субъекта, а атрибут name — имя субъекта.
#Вторая строка кода определяет класс StudentJournal. У класса StudentJournal есть три атрибута: student_list, Teacher_list и оценки. Атрибут student_list — это список студентов в журнале, атрибут Teacher_list — это список учителей в журнале, а атрибутgrade — словарь оценок для каждого учащегося.
# Третья строка кода определяет класс Grade. Класс Grade имеет пять атрибутов: id, group_id, subject_id, student_id, Teacher_id иgrade_level. Атрибут id — уникальный идентификатор оценки, атрибут group_id — идентификатор группы, к которой принадлежит оценка, атрибут subject_id — идентификатор предмета, за который выставлена ​​оценка, атрибут student_id — идентификатор студента который получил оценку, атрибут student_id — это идентификатор учителя, поставившего оценку, а атрибутgrade_level — это уровень оценки, который получил ученик.
# Четвертая строка кода создает группу. Группа имеет идентификатор 1 и имя «9-A».
# Пятая строка кода создает учителя. У учителя есть идентификатор 1, имя «Учитель», возраст 34 года, пол 1, group_id 1 и предмет «Математика».
# Шестая строка кода создает студента. Студент имеет идентификатор 2, имя «Шоазиз», возраст 25, пол 1 и group_id 1.
# Седьмая строка кода создает студенческий журнал.
# Восьмая строка кода добавляет учащегося в студенческий журнал.
# Девятая строка кода добавляет учителя в журнал учеников.
# Десятая строка кода создает тему. Субъект имеет идентификатор 1 и имя «История».
# Одиннадцатая строка кода создает оценку. Оценка имеет id 1, group_id 1, subject_id 1, student_id 2, Teacher_id 1 иgrade_level 5.
# Двенадцатая строка кода добавляет оценку в студенческий журнал.
# Тринадцатая строка кода печатает отчет студенческого журнала.



















