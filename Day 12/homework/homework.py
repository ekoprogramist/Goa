#task 1
# გამოიტანეთ რიცხვები 0-დან 20-ის ჩათვლით 

for i in range(0,21):
     print(i)

# #task 2   
    
# #მომხმარებელს შემოატანინეთ რიცხვი და დაპრინტეთ შემოტანილი რიცხვი ლუწია თუ არა თუ ლუწია დაუპრინტეთ "Number is even"
num = int(input("Enter random number:  "))

if num %  2 == 0:
     print("you have even number")



else:
    print("you have odd number..")


#task 3
#დაპრინტეთ 20-მდე ლუწი რიცხვები
for i in range(0,21,2):
    print(i)




# #task4 
# #50-იდან 100-ის ჩათვლით არსებული ყველა რიცხვი დააჯამეთ for ციკლის გამოყენებით. ეს ჯამი უნდა შეინახოს ცვლადში, ამიტომ ციკლის გარეთ შექმენით sum ცვლადი (sum-ჯამი)
for i in range(50,101):
      print(i)
 


print(sum(range(50,101))) 


# #task 5
# #)დაწერეთ ალგორითმი რომელიც ბეჭდავს 5-ის ჯერად რიცხვებს (რიცხვები რომლებიც იყოფა 5-ზე) 1-დან 50-ის ჩათვლით


for i in range(0,51,5):
     print(i) 


#task 6
#მომხმარებელს input-ის გამოყენებით შემოატანინეთ ორი რიცხვი. შემდეგ შეამოწმეთ რომელია უდიდესი და გამოიყენეთ for ციკლი: უმცირესიდან უდიდესამდე დაპრინტეთ ყველა რიცხვი

num1 = int(input("Enter random number: "))
num2 = int(input("Enter random number: "))

for i in range(min(num1,num2),max(num1,num2)):

    print(i)

# #task 7
# გადაიმეორეთ გავნლილი მასალა და გააკეთეტ მაგალითეი

num1 = 120
num2 = 230
num3 = 340
num4 = 120

print(num1 + num2 // num3 + num4 )
print(sum(num1,num2) + sum(num3,num4))

#task 8
#დაწერეთ ალგორითმი, რომელიც დაბეჭდავს 5-იდან ათის ჩათვლით რიცხვების ნამრავლს for loop-ის გამოყენებით.


helper2 = 1

for i in range(5,11):
    helper2 = helper2 * i

print(helper2)



#task 9
#BOSS: For loop დახმარებით ეცადეთ, რომ სიტყვა დაპრინტოთ საპირისპირო მიმართულებით (შეიძლება არ გამოგივიდეთ მაგრამ სცადეთ)
name = "erekle"
str = "" 
for i in name: 
   str = i + str 
print (str)











