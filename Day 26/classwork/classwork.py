# name = input("enter yuor firstname: ")

# print(name.capitalize())



# name = "erekle".upper()

# print(name)


# capitalize ადიდებს სთრინგის პირველ ასოს
# upper ადიდებს სთრინგის ყველა ასო

# sentes = "my name is erekle my lastname is dzindzibadze"
# count = sentes.count("e")

# print(count)


# name1 = input("enter your name in uppercase: ")
# print(name1.lower())



#lower ფუნქცია აპატარავებს სტრინგში დიდ ასოებს
#counr ფუნქცია ითვლის ასოებს ერთ წინადადებაში (რომელიც ჩვენ მოგვესურვება)

sentes1 = "my name is erekle"
count = sentes1.index("i")



sentes2 = "my name is erekle"
count = sentes2.find("i")


#index არის ფუნქცია რომელიც გვიბრონებს ინტეგერს და პასუხში არის გადმოცემული რა ასოსაც მიუთითებთ იმისი index ანუ (ადგილი)
#find არის ფუნქცია რომელიც გვიბრონებს ინტეგერს და პასუხში არის გადმოცემული რა ასოსაც მიუთითებთ იმისი index ანუ (ადგილი) find და index ის განსხვავებაა რომ თუ ისეთი აო ნა სითყვა რომელიც str  არ მოიძებნა find ფუნქცია დააბრუნებს(-1) და index (error)

email_input = ""

while email_input.endswith("@gmail.com") != email_input:
    email_input("how long email do you want")


print(email_input)