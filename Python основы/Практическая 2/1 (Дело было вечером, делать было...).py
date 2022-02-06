def in_txt(arg):
    if arg == "Error":
        return arg
    else:
        try:
            if int(float(arg)) == float(arg):
                return "int"
            else:
                return "float"
        except:
            return "str"

list1 = []
run = True
num_element = 0

while run:   
    print("------------------\nЧтобы остановить введите цифру 0")
    list1.append(input("Введите что-нибудь: "))  

    if list1[len(list1)-1] == "666":
        print("\n###########\nБу-га-га!\n###########\n")
        del list1[len(list1)-1]
        list1.append("Error")

    if list1[len(list1)-1] == "0":
        print("--#--#--#--#--#--#--#--#--")
        del list1[len(list1)-1]
        run = False

        for i in list1:
            num_element += 1
            print(f"Элемент №{num_element}: {i}; его тип: {in_txt(i)}")                     