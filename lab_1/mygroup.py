groupmates = [
    {
        "name": "Сениксон Сандро",
        "surname": "Лопеш",
        "exams": ["Информатика", "Философия", "АиГ"],
        "marks": [5, 5, 3]
    },
    {
        "name": "Франк",
        "surname": "Мателама",
        "exams": ["Информатика", "Философия", "АиГ"],
        "marks": [5, 5, 5]
    },
    {
        "name": "Настия",
        "surname": "Груздева",
        "exams": ["Информатика", "Философия", "АиГ"],
        "marks": [4, 3, 4]
    },
    {
        "name": "Озил",
        "surname": "Давасурен ",
        "exams": ["Информатика", "Философия", "АиГ"],
        "marks": [5, 5, 5]
    },
    {
        "name": "Алина",
        "surname": "Золоева",
        "exams": ["Информатика", "Философия", "АиГ"],
        "marks": [5, 5, 5]
    },
    {
        "name": "Дидо",
        "surname": "Елонго",
        "exams": ["Информатика", "Философия", "АиГ"],
        "marks": [5, 5, 5]
    },
    {
        "name": "Полин",
        "surname": "Ндзила",
        "exams": ["Информатика", "Философия", "АиГ"],
        "marks": [4, 4, 4]
    }

]


# ljust(15) - é um método de corda que adiciona o número necessário de espaços de modo que o comprimento da corda
# é igual ao parâmetro que está sendo passado. resumindo criacao da tabulacao
def print_students(students):
    control = 0 # variavel de controle
    counter = 3
    while counter:
        try:
            average = int(input("Enter the average value to filter:attempt {} ".format(counter)))

        except:
            print("Message error: Invalid input, please enter a number!!!")
            counter = counter - 1
            continue; # esta funcao para a execucao de uma instucao incorreta e depois volta o codigo para uma nova execucao


        if average > 0:
            print(u"Num".ljust(5), u"Имя".ljust(15), u"Фамилия".ljust(10), u"Экзамены".ljust(36), u"Оценки".ljust(10),
                  u"Средняя оценка".ljust(10))
            i = 1
            for student in students:
                average_mark = sum(student["marks"]) / len(student["marks"])  # calculando a media

                if average_mark > average:
                    print(i, "-".ljust(3), student["name"].ljust(15), student["surname"].ljust(10),
                          str(student["exams"]).ljust(36), str(student["marks"]).ljust(10),
                          str(average_mark)[0:3].ljust(10))
                    i = i + 1

            if control == 0:
                # infelizmente nao temos nenhum estudante com a medeia superior a media digitado - este e o valor exibido
                print(
                    "Message error: Unfortunately, we don't have any students with an average higher than the "
                    "average {} entered!! ".format(average))

        else:
            print("Message error: Students not found, please enter number bigger to 0")
            counter = counter - 1


print_students(groupmates)  # chamada da função


