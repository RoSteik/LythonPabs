from university.properties.Group import Group
from university.properties.Institute import Institute
from university.properties.Student import Student

if __name__ == "__main__":
    IKTA = Institute("Інститут комп'ютерних технологій, автоматики та метрології (ІКТА)",
                     "Комп’ютерні науки та інформаційні технології",
                     "Системна Інженерія (Інтернет речей)",
                     "Комп'ютеризовані системи автоматики",
                     False,
                     "Stepan Bandera street",
                     35_000)
    iot_11 = Group(IKTA, "IoT-11", 27, 79.8, "Some schedule")
    student = Student("Rostyk", "Tiger", iot_11, 80.8)

    student.do_homework()
    print(student)

