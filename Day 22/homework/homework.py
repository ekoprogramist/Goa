# 1. შექმენით ფუნქცია, რომელიც იღებს რაიმე რიცხვს და აბრუნებს მასზე 5'ით მეტს.

# 2. შექმენით ფუნქცია, რომელიც იღებს ორ integer'ს და აბრუნებს მათ ნამრავლს

# 3. შექმენით ფუნქცია, რომელიც იღებს string'ს ამ string'ის სიგრძეს (გამოიყენეთ ფუნქცია len()).

# 4. შექმენით ფუნქცია, რომელიც იღებს string'ების list'ს და აბრუნებს ამ string'ების სიგრძეების list'ს (გამოიყენეთ ფუნქცია len()).

# 5. შექმენით ფუნქცია, რომელიც იღებს string'ს და აბრუნებს True-ს თუ ის არის Palindrome (ანუ იგივენაირად იკითხება მარცნიდანაც და მარჯვნიდანაც მაგალითად: "wow") და სხვა შემთხვევაში False-ს.

# 6. შექმენით ფუნქცია, რომელიც პოულობს ყველაზე გრძელ string'ს string'ების სიაში.

# 7. შექმენით ფუნქცია, რომელიც იღებს რიცხვს და აბრუნებს მის factorial ს (რა არის ფაქტორიალი: https://en.wikipedia.org/wiki/Factorial).

# 8. შექმენით ფუნქცია, რომელიც იღებს 2 integer'ების list'ს და აბრუნებს ორივე list'იდან მაქსიმალური რიცხვების ჯამს.

# 9. შექმენით ფუნქცია, რომელიც იღებს 2 integer'ების list'ს და აბრუნებს ორივე list'იდან მინიმალური რიცხვების სხვაობას.

# 10. შექმენით ფუნქცია, რომელიც იღებს integer'ების list'ს და აბრუნებს ამ სიაში მაქსიმალური და მინიმალური რიცხვების სხვაობას.



# task 1

def random_number(num):
    return num + 5


print(random_number(23))




# #task 2


def random_integer_number(num1, num2):
    return num1 * num2

print(random_integer_number(23, 67))





# # task 3

def  manual_string(str1):
    return  len(str1)

print(manual_string)


print(manual_string("erekle"))





# #task 4
words = ["banana", "apple", "oreng_juice", "borjomi"]
def list_list(words):
    str_len = []
    for i in words:
        lens = len(i)
        str_len.append(lens)
    return  str_len 



print(list_list(words))




# #task 5
def palidrtom(str2):
    rivers = str2[:: -1]
    if str2 == rivers:
        return  True
    else:
        return False

print(palidrtom("wow"))
print(palidrtom("erekle"))
print(palidrtom("Gio"))


# #task 6
str_hh = ["erekle", "giorgi", "daviti", "luka"]
def strings(strin_gs1):
    str_ebi = []
    for i in strin_gs1:
        lens = len(i)
        str_ebi.append(lens)
    nisan_GTR = sorted(str_ebi)
    return nisan_GTR[-1]

print(strings(str_hh))








# task 7

def factorial(enter_number):
    sum = 1
    for i in range(1, enter_number+1):
        sum = sum * i
    return sum


print(factorial(7))













# # task 8
number9999 = [12, 45, 67, 89, 23]
def number1000000(number89, number56):
    sorted1 = sorted(number89)
    sorted2 = sorted(number56)
    return sorted1 [-1] + sorted2 [-1]



# # task 9

def num(number134, number345):
    sorted12 = sorted(number134)
    sorted13 = sorted(number345)
    return sorted12 [0] - sorted13 [0]
list1 = [999998999, 89, 78, 89]
list2 = [1000000000, 78, 78, 90]
    

print(num(list1, list2))










# # task 10
def manual_int(number12):
    sorted100000 = sorted(number12)
    return sorted100000 [-1] - sorted100000 [0]

list10000 = [78, 45, 67, 12]

print(manual_int(list10000))



# # 11. შექმენით ფუნქცია, რომელიც იღებს integer'ების list'ს და აბრუნებს ყველა ელემენტის ჯამს.

# # 12. შექმენით ფუნქცია, რომელიც იღებს string'ს და აბრუნებს ხმოვანი ასოების რაოდენობას string'ში.

# # 13. შექმენით ფუნქცია, რომელიც იღებს integer'ების list'ს და აბრუნებს ახალ list'ს თითოეული integer'ის კვადრატით. 
# # (მაგალითად: input: [2, 4]. output: [4, 16])

# # 14. შექმენით ფუნქცია, რომელიც იღებს string's და აბრუნებს მის შებრუნებულს.

# # 15. შექმენით ფუნქცია, რომელიც იღებს რაიმე integer'ს და თუ ლუწია აბრუნებს True'ს, თუ კენტი False'ს.

# # 16. შექმენით ფუნქცია, რომელიც იღებს string'ების სიას და აბრუნებს ყველაზე გრძელ string'ს.

# # 17. შექმენით ფუნქცია, რომელიც იღებს მთელი რიცხვების სიას და აბრუნებს სიაში ყველაზე მცირე რიცხვს.

# # 18. შექმენით ფუნქცია, რომელიც იღებს ორ integer'ს და აბრუნებს მათ უდიდეს საერთო გამყოფს (GCD-Greatest common divisor).

# # 19. შექმენით ფუნქცია, რომელიც იღებს string'ს და აბრუნებს იმავე string'ს uppercase'ში. 
# # (მაგალითად: input: "Hello World". output: "HELLO WORLD".

# # 20. შექმენით ფუნქცია, რომელიც იღებს integer'ების სიას და აბრუნებს მათ საშუალო არითმეტიკულს.
# # (მაგალითად: input: [1, 5, 12]. output: (1 + 5 + 12)/3, ანუ 6.) (ელემენტების დასათვლელად გამოიყენეთ ფუნქცია len).


# task 11
def inte_gerebi():
        number_list = [12,  34, 56, 89]
        for i in number_list:
               return i
        sum(number_list)
print(inte_gerebi())
       
        
# task 12
def vowel_count(string):
    vowels = "aeiou"
    vowel_len = 0

    for i in string:
        if i in vowels:
            vowel_len += 1
    
    return vowel_len

print(vowel_count("Hello everyone"))

# task 13
def double_number(integer):
     numbers = []
     for i in integer:
          numbers.append(i ** 2)
     return numbers      
          
print(double_number([10, 34, 90]))

# task 14
def reverce_string(string):
     return string[:: -1]

print(reverce_string("good_boy"))

# task 15
def check(number):
     if number % 2 == 0:
          return True
     elif number % 2 != 0:
          return False

print(check(22))


# task 16

def longest_string(strings):
    if not strings: 
        return None
    return max(strings, key=len)

print(longest_string(["erekle" "2121212121212121212"]))


#task 17
def integer(number):
     return min(number)

print(integer([20, 56, 67, 89]))

#task 18
import math

def gcd(int1, int2):
     return math.gcd(int1, int2)


print(gcd(12, 56))


#task 19
def string(uppercase):
     text = "hello my best friend"
     uppercase = text.upper()
     return uppercase
     
print(string("hello my best friend"))



#task 20
def average_arithmetic(num1, num2, num3, num4):
     return num1 + num2 + num3 + num4 // 4

print(average_arithmetic(12, 3, 45))



















































          
             
    



























