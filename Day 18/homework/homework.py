#1
count = int(input("please enter qunatuty number of how many numbers do you want: "))


number = []


for i in range(count):


     num = int(input("lease enter number" + str (i + 1) + ":"))

number.append(num)
print(number)

print(len(number))



#2
start = int(input("Enter start number: "))
end = int(input("Enter end number: "))

numbers1 = []

for i in range(start, end):
       numbers1.append(i)

print(numbers1)


print(max(numbers1))
print(min(numbers1))
print(sum(numbers1))

#3
numbers = []

for i in range(1, 10):
     numbers.append(i)
print(numbers)
print(len(numbers))














































