# 1) შექმენით ფუნქცია რომელსაც გადაეცემა 2 რიცხვი. ფუნქციამ უნდა ჩაატაროს ყველა არითმეტიკული მოქმედება ამ ორ რიცხვს შორის.

# 2) შექმენით ფუნქცია რომელსაც გადაეცემა ორი რიცხვი. ამ ფუნქციამ პირველ რიცხვს მანამ უნდა დაუმატოს მეორე რიცხვი სანამ ჯამი არ გახდება 100ის ტოლი ან 100ზე მეტი.

# 3) შექმენით ფუნქცია რომელიც ამოწმებს რიცხვი კენტია თუ ლუწი.

# 4) შექმენით ფუნქცია რომელსაც გადაეცემა ლისტი. ფუნქციამ უნდა იპოვოს ლისტში უდიდესი რიცხვი.

# 5) შექმენით ფუნქცია რომელსაც გადაეცემა ლისტი. ფუნქციამ უნდა იპოვოს ამ ლისტში შემავალი რიცხვების ჯამი

# 6) შექმენით ფუნქცია რომელსაც გადაეცემა სტრინგები და ინტეჯერები რაღაც თანმიმდევრობით. ფუნქციამ უნდა შეძლოს და ეს სტრინგების და ინტეჯერების თანმიმდევრობა უნდა გამოიტანოს შებრუნებულად.

# 7) შექმენით ფუნქცია რომელსაც გადაეცემა სტრინგების ლისტი. ამ ფუნქციამ უნდა იპოვოს ყველაზე გრძელი და ყველაზე მოკლე სტრინგები ამ ლისტში.

# 8) შექმენით ფუნქცია რომელსაც გადაეცემა რაიმე სტრინგი. ამ ფუნქციამ უნდა შეძლოს და თითოეული ასო შეცვალოს (პატარა ასო დიდი ასოთ a-A ხოლო დიდი ასო პატარათი A-a).

# 9) შექმენით ფუნქცია რომელსაც გადაეცემა სტრინგი. ამ ფუნქციის მეშვეობით უნდა დაითვალოთ თანხმოვნების რაოდენობა ამ სტრინგში.

# 10) შექმენით ფუნქცია რომელსაც გადაეცემა ინტეჯერი და თუ ლუწია აბრუნებს True-ს ხოლო თუ კი კენტია აბრუნებს False



# task 1
def number(num1,num2):
    number = num1 + num2
    number2 = num1 - num2
    number3 = num1 * num2
    return number,number2,number3
       
num1 = 5
num2 = 7
print(number(num1,num2))






# task 2
def number(num):
    return sum(num)
print(number([2,3,4,5,6,1]))




# # task 3
def check(number):
     if number % 2 == 0:
          return True
     elif number % 2 != 0:
          return False

print(check(22))



# task 4
def  manual_integer(int1):
    return  max(int1)

print(manual_integer([12, 45, 89, 100]))


# task 5
def list_sum(int35):
    return sum(int35)

print(list_sum([100, 67 ,200]))



# task 6
def stringss_reverce(string):
    return string[::-1]

print(stringss_reverce("boys"))




# # task 7
def guess(word):
    max_word = ""
    for i in word:
        if len(i) > len(max_word):
            max_word += i
    return max_word

print(guess(["car", "money", "eujfuwes"]))










# task 8
def check(string):
    word = ""
    for i in string:
        if i.islower():
            word += i.upper()
        elif i.isupper():
            word += i.lower()
    return word

print(check("AnIMals"))



# task 9
def vowel_count(word):
    vowel = "aioeuAIOEU"
    count = 0
    for i in word:
        if i in vowel:
            count += 1
    return count

print(vowel_count("mOnEy"))





# task 10
def even_kent(count):
    if count % 2 == 0:
        return True
    else:
        return False










# 11)შექმენით ფუნქცია, რომელსაც გადაეცემა მთელი რიცხვების სია. თქვენი დავალებაა, რომ ამ სიის ლუწ ინდექსებზე მყოფი რიცხვების ჯამი დააბრუნოთ. აუცილებლად გამოიყენეთ return ამ და ასევე შემდეგ დავალებებში.

# 12)შექმენით ფუნქცია, რომელსაც გადაეცემა მთელი რიცხვი. თქვენი დავალებაა, რომ დააბრუნოთ ლუწია თუ კენტი ის.

# 13)შექმენით ფუნქცია, რომელიც დააბრუნებს მარტივია თუ არა რიცხვი (მარტივია რიცხვი, თუ მას მარტო ორი გამყოფი აქვს).

# 14)შექმენით ფუნქცია, რომელსაც გადაეცემა სახელების სია. თქვენი დავალებაა, რომ დააბრუნოთ ამ სიის განახლებული ვერსია, სადაც ყველა სახელი დიდი ასოთი დაიწყება.

# 15)შექმენით ფუნქცია, რომელსაც გადაეცემა მთელი რიცხვების სია. შემდეგ გამოიყენეთ ციკლი, რათა განიხილოთ ამ სიის ყველა რიცხვი - თუ რიცხვი ლუწია, ახალ სიაში დაამატეთ მისი განაყოფი ორზე, ხოლო თუ კენტია, მაშინ რიცხვის ნამრავლი ორზე. საბოლოოდ დააბრუნეთ განახლებული სია/ 

# 16)შექმენით ფუნქცია, რომელსაც გადაეცემა სტრინგი და დააბრუნეთ ეს სტრინგდი შებრუნებულ + დიდი ასოებით (reversed / upper). 

# 17)შექმენით ფუნქცია რომელსაც გადაეცემა სია შემდგარი სტრინგებისგან ---> (["dato" , "nika" , "polieqtori" , "zaza"....)], დამატებით შექმენით ორი სია odd = [] და even = [], გადაუარეთ ორიგინალ სიას for ციკლით და გაიგეთ რომელი ელემენტი შედგება კენტი ასოებისგან და რომელი ლუწი, საბოლოოდ ჩაამატეთ შესაბამისი სტრინგები შესაბამის სიებში (odd / even) დიდ ასოებათ (upper) და ბოლოს დაბეჭდეთ. 

# 18) შექმენით ფუნქცია რომელსაც გადაეცემა სია შემდგარი სტრინგებისგან, გადაუარეთ ამ სიას და შეამოწმეთ თუ მისი characterების რაოდენობა არის ლუწი, ჩაამატეთ ეს კონკრეტული სიის ელემენტი ახალ ცარიელ სიაში და გადააკეთეთ იგი upper ფუნქციით, თუ იქნება ამ სტრინგის ასოების რაოდენობა კენტი, ჩაამატეთ ეს ელემენტი ახალ სიაში რომელსაც პირველი character ექნება გადიდებული, დანარჩენი პატარა. საბოლოოდ გამოიტანეთ ეს სია. 

# 19) შექმენით ფუნქცია რომელსაც გადაეცემა სია შემდგარი ყველანაირი სტრინგისგან (დიდი ასოებით / პატარა ასოებით : "dato" , "LUKA") , გადაურეთ ამ სიას და თუ ეს კონკრეტული ელემენტი არის შემდგარი დიდი ასოებისგან, დაამატეთ სიაში ისე როგორც lower, ხოლო თუ შედგება პატარა ასოებისგან დაამატეთ სიაში ისე როგორც upper / !HINT : გადახედეთ ფუნქციებს, isupper() და islower()! 

# 20)შექმენით ფუნქცია რომელსაც გადაეცემა სტრინგი, ამ სტრინგზე გამოიყენეთ find() ფუნქცია და თუ find ფუნქცია დააბრუნებს ლუწ ინდექს მაშინ ეს სტრინგი დააბრუნეთ დიდი ასოებით (upper) ხოლო თუ დააბრუნებს კენტ ინდექსს, მაშინ დააბრუნეთ ეს სტრინგი რომლის პირველი ასოც იქნება დიდი (capitalize) 


# task 11
def sum_even_index(nums):
    sum_even = 0
    for i in range(0, len(nums), 2): 
        sum_even += nums[i]
    return sum_even

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = sum_even_index(nums)
print(result)  




# task 12
def even_or_kent(numbers):
    for i in numbers:
        if i % 2 == 0:
            print("even")
        else:
            print("kent")
    return numbers

print(even_or_kent([12, 78]))
        


# task 13
def num(numbers1):
    if numbers1 % 1 == 0 and numbers1 % numbers1  == 0:
        return "simple"
    else:
        return "dificult"


print(num(2))






#task 14
word = "erekle"
print(word.capitalize())





#task 15
def num1(numbers10):
    lists = []
    for i in numbers10:
        if i % 2 == 0:
            lists.append(i / 2)
        elif i % 2 != 0:
            lists.append(i * 2)
    return lists

print(num1([2,3,5,6,7]))






#tassk 16
def string(word):
    word = word.upper()
    word = word [::-1]
    return word
print(string("money"))




#task 17 
def string1(word1):
    odd = []
    even = []
    for i in word1:
        if len(i) % 2 == 0:
            even.append(i.upper())
        elif len(i) % 2 != 0:
            odd.append(i.upper())
    return odd,even

print(string1(["erekle", "leila", "gio"]))







# task 18
def stringss(string, char):
    index = string.find(char)

    if index % 2 == 0:
        return string.upper()
    else:
        return string.capitalize()
    
print(stringss("Hello world", "w"))








# task 19

def transform_strings(strings):
    transformed_list = []
    for s in strings:
        if s.isupper():
            transformed_list.append(s.lower())
        elif s.islower():
            transformed_list.append(s.upper())
        else:
            transformed_list.append(s)  # თუ სტრინგი არ არის მხოლოდ დიდი ან პატარა ასოებით
    return transformed_list

strings = ["dato", "LUKA", "SANDRO", "mariam", "Elene"]
print(transform_strings(strings))



#task 20

def transform_based_on_find(s, sub):
    index = s.find(sub)
    if index == -1:
        return "Substring not found"
    elif index % 2 == 0:  # თუ ინდექსი ლუწია
        return s.upper()
    else:  # თუ ინდექსი კენტია
        return s.capitalize()

s = "hello world"
print(transform_based_on_find(s, "world"))

































































































