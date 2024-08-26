# #შექმენით ფუნქცია რომელსაც დაარქმევთ Calculate_average სადაც იქნება ერთი სია შექმნილი სახელად numbers თქვენი დავალება არის გამოთვალოთ ამ რიცხვების საშუალო არითმეტიკული გამოიყენეთ  sum და len ფუნქციებიd
# #
# #
# #
# #

# #შექმენით  მისალმების ფუნქცია სახელად greet რომელიც მიესალმება მომხმარებელს და default მნიშვნელობად იქნება hello guest
# def greet(name = "Guest"):
#     print("welcome " + name)

# greet('erekle')
# greet()
# greet('andria')


# #შექმენით ფუნქცია რომელსაც გადაეცემა ორი მნიშვნელობა firstnum და secondnum და თქვენი დავალებაა იპოვოთ ამ რიცხვებს შორის ყველა რიცხვის ჯამი

# def sum_sum(firstnum, secondnum):
#     print(sum(firstnum + secondnum))

# sum_sum = (12, 34)
# sum_sum = (12, 134)

# #შექმენით ფუნქცია რომელსაც გადაეცემა ლისტი. თქვენი დავალებაა ამ ლისტიდან ამოიღიოთ ყველა ციფრი და დაახარისხოთ ისინი კენტებად და ლუწებად




#შექმენით ფუნქცია რომელსაც დაარქმევთ sum(ჯამი) ეგ ფუნქცია მიიღებს ორ რიცხვს პარაამეტრებს გაუწერეთ num1 და num2 თქვენი დავალებაა ამ ორი რიცხვის ჯამი დაბეჭდეთ
def manual_sum(num1, num2):
    print(num1 + num2)

manual_sum(12, 45)

#შექმენით ფუნქცია რომელიც დაბე#ჭდავს ორი სტრინგის გაერთიანებას მაგალითად str1  და str2 და დაბეჭდეთ მათი შეერთება ფუნქციას დაარქვით joined_string
def joined_string(str1, str2):
    print(str1 + str2)

joined_string("20", "24")

#შექმენით ფუნქცია find_maximum რომელსაც გადაასცემთ ორ მნიშვნელობას მაგალიტად num1 და num2 შემდეგ დააბრუნეთ აქედან რომელიც უფრო მეტია
def find_maximum(num3, num4):
    if num3 > num4:
        return num3
    elif num3 < num4:
        return num4
    else:
        return "Both number is equal"
    

print(find_maximum(8,5))

#დაწერეთ პითონის ფუნქცია, რომელიც ითვლის მართკუთხედის ფართობს მისი სიგრძისა და სიგანის პარამეტრების მიხედვით.

def trangle(a, b):
    print(a + b * 2)


trangle(23, 34)



#task 14
def is_prime(number):
     if number <= 1:
         return False
     for i in range(2, int(number**0.5) + 1):
         if number % i == 0:
             return False
     return True

result = is_prime(17)
print(result)

#task 15
def  count_xmovnebi(a, i, e, o, u):
    print(a, i, o, e, u)  

print(count_xmovnebi)
