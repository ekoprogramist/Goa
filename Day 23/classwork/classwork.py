#1) შექმენით ფუნქცია სახელად add რომელსაც ექნება ორი პარამეტრი, სახელად num1 num2, ამ პარამეტრებმ,ა უნდა მიიღოს რიცხვები და ფუნქციამ უნდა დაბეჭდოს ამ ორი რიცხვის ჯამი


# def add(num1, num2):
#     print(num1 + num2)


# add(12, 34)


#შექმენით ფუნქცია რომელსაც გადაეცემა 2 რიცხვი. ამ ფუნქციას უნდა დაარქვათ calculate. უნდა დაბეჭდოთ რომელი ოპრეაციის არჩევა შეუძლია მომხმარებელს და შემდეგ უნდა ჩაატაროთ ის ოპერაცია იმ ორ რიცხვს შორის რომელიც მომხმარებელმა შემოიყვანა

def calculator(num1, num2):
    print("1. +")
    print("2. -")
    print("3. *")
    print("4. /")

    choice = int(input("Please enter your choice: "))
    result = 0

    if choice == 1:
        result = num1 + num2
    elif choice == 2:
        result = num1 - num2
    elif choice == 3:
        result = num1 * num2
    elif choice == 4:
        result = num1 * num2
    else:
        print("Invalid choice")
    
    return result



print(calculator(13, 14))





































































