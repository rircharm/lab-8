def Open(file_name, mode):

    try:

        file = open(file_name, mode)

    except:

        print("File", file_name, "wasn't opened!")

        return None

    else:

        print("File", file_name, "was opened!")

        return file

file1_name = "students.txt"

file_1_w = Open(file1_name, "w")

if(file_1_w != None):

   file_1_w.write("Афанасенко Віктор \n")
   file_1_w.write(" Як у Python відкрити файл, прочитати всі слова та знайти слово, яке зустрічається найчастіше? \n")
   
   file_1_w.close() 

   print("File students.txt was closed!")

