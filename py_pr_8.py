#структура запису в файл:
# Name
# Question
# Answer
def Open(file_name, mode):

    try:

        file = open(file_name, mode)

    except:

        print("[info] File", file_name, "wasn't opened!")

        return None

    else:

        print("[info] File", file_name, "was opened!")

        return file
#Створення файлу Афанасенка Віктора
#Функція Open для відкриття файлу з обробкою помилок

def Answer_the_question():# Функція зчитує останнї два рядки (прізвище + питання) з файлу та дає змогу користувачу ввести відповідь
    file1=Open("students.txt", "r")
    print("Question:\n")
    lines = file1.readlines()
    print(lines[-2].strip()) # Виведення останніх двох рядків прізвище + питання
    print(lines[-1].strip())
    answer=input("Enter your answer: ")
    file2=Open("students.txt", "a")
    file2.write(answer + "\n")
    file1.close()
    file2.close()
    print("[info] files closed!")
    

def Enter_new_question():# Функція додає у файл нове прізвище + питання
    file=Open("students.txt", "a")
    name=input("Enter your name: ")
    question=input("Enter your question: ")
    file.write(name + "\n")
    file.write(question + "\n")
    file.close()
    print("[info] file closed!")

def Show_all_file():# Функція виводить увесь вміст файлу на екран
    file=Open("students.txt", "r")
    content=file.read()
    print("\nFile content:\n\n", content)
    file.close()
    print("[info] file closed!")
#функції Федорченка Романа
#Сворення функцій: Answer_the_question, Enter_new_question, Show_all_file і головного меню

def Clear_file():  # Функція очищає вміст файлу students.txt після підтвердження користувача
    confirm = input("Are you sure you want to clear the file? (yes/no): ")
    if confirm.lower() == "yes":
        open("students.txt", "w").close()
        print("[info] File has been cleared!")
    else:
        print("[info] Operation canceled.")
# Функція Бобро Мар'яни
# Створення функції Clear_file, покращення функції Answer_the_question і додано зміни в головному меню (+ коментарі до всього коду)

print("Practic work 8. File handling in Python")
print("Student: \nАфанасенко Віктор ППМР1-102\nБобро Мар'яна ППМР1-102\nФедорченко Роман ППМР1-104\n")
# Головне меню програми — вибір дії користувача
while True :
    x=int(input("\nMenu:\n1. Answer the question\n2. Enter new question\n3. Show all file\n4. Clear file\n5. Exit\n6. Run all(try for practic work)\nChoose an action (1-6): "))
    if x==1:
        Answer_the_question()
    elif x==2:
        Enter_new_question()
    elif x==3:
        Show_all_file()
    elif x==4:
        Clear_file()
    elif x==5:
        break
    elif x==6:
        Show_all_file()
        Answer_the_question()
        Enter_new_question()

#file1_name = "students.txt"