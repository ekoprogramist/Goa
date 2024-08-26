#task 1
#საინფორმაციო

#task 2
#განიხილე:
def find_short(s):
    list1 = s.split(" ")


    word_len = len(list1[0])
    for i in list1:
        if len(i) < word_len:
            word_len = len(i)
    
    # word_len = 3
    return word_len

print(find_short("bitcoin take over the world maybe who knows perhaps"))

#ესეიგი არის შექმნილი ფუნქცია სახელას find_shirt პარამეტრათ აქვს გააცემული s შემდეგ არის შექმნილი ცარიელი ცვლადი სახელად list1 სახელმა არ უნდა დაგვაბლიოს split მხოლოდ strძე მუშაობს
#შემსეგ ამ ცვლადში გვაქ სპლიტი გამოყენებული split = გახლეჩვა...
#len -სიგრძე ამ შემთხვევაში List1ის index 0ზე 

#task3
# სპლიტებზე მუშაობა:
#სადაც სფეისი იყო იქ გახლიჩა.
str1 = "erekle dzindzibadze"
result1 = str1.split(" ")
print(result1)


#ანუ "ო" ასო სადაც შეხვდა იქ ამოიღო ეს ო ასოები ანუ "ო" ასოებთან გახლიჩა.
str2 = "my favorite color"
result2 = str2.split("o")
print(result2)

#რამდენი ასოც არ უნდა გადაცე იმუშავებს მარა სფეისები არ უნდა გააკეთო თუ არა აღარ იმუშავებს არც მძიმე.
str3 = "helicopter and fly"
result3 = str3.split("and")
print(result3)

#უბრალოდ ცარიელი ლისტი იმდენი ცარიელი qoutision mark რამდენი m იც მაქ დაწერილი str4ში.
str4 = "mmmmmmmmmmmm"
result4 = str4.split("m")
print(result4)




#მაინც " " გარეშე განმოიტანა.
str5 = "wyali"
result5 = str5.split(" ")
print(result5)





#py case snsitivy ენაა და ამიტომ არცერთი გახლეჩვა გააკეთა
str6 = "children Go into school"
result6 = str6.split("g")
print(result6)



#მძიმე არ მოქმედებს.
str7 = "cc mm cg"
result7 = str7.split("ც,გ")
print(result7)



str8 = "me miyvars wyali"
result8 = str8.split("wyali")
print(result8)





str9 = "me miyvars chemi da"
result9 = str9.split("da")
print(result9)







str10 = "dog"
result10 = str10.split("o")
print(result10)



#task 4
#codewars

