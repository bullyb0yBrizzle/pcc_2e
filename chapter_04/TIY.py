#4-1 - pizzas
print("4-1")
pizzas = ["Pepperoni","Margherita","Ham and Cheese"]
#Now print the name of each pizza
for name in pizzas:
	print(f"I like {name} pizza")
print("I really love pizza\n\n")

#4-2 animals
print("4-2")
animals = ["Zebra","Lion","Elephant","Koala","Monkey"]
#Now print each animal
for animal in animals:
	print (f"A {animal} would make a great pet")
print("In fact, any of the above animals would make a great pet!\n\n")

#4-3 Counting to 20
print("4-3")
numbers = list(range(1,21))
for number in numbers:
	print(number)
print("\n\n")

#4-4 One Million - print numbers 1 to 1000000
print("4-4")
#numbers = list(range(1,1000001))
#for number in numbers:
	#print(number)
print("\n\n")

#4-5 Summing a million
#make list and then get max(),min() and sum()
print("4-5")
numbers = list(range(1,1000001))
print(f"the max() is {max(numbers)}")
print(f"the min() is {min(numbers)}")
print(f"the sum() is {sum(numbers)}")
print("\n\n")


#4-6 Odd numbers
#make list of odd numbers between 1-20 and print them out on screen
print("4-6")
numbers = list(range(1,21,2))
for number in numbers:
	print(number)
print("\n\n")


#4-7 Threes
#make list of Multiples of 3 and use loop to print numbers in list
print("4-7")
numbers = list(range(0,31,3))
for number in numbers:
	print(number)
print("\n\n")


#4-8 Cubes
#make a cube of 1-10 
print("4-8")
squares = []
numbers = list(range(1,11))
for number in numbers:
	square = number**3
	squares.append(square)
print(squares)
print("\n\n")


#4-9 Cubes
#make a cube of 1-10 using comprehension
print("4-9")
squares = [number**3 for number in list(range(1,11))]
print(squares)
print("\n\n")




#4-10 Slices
#Use slice to get 
#first three in list
#middle three in list
#last three in list
print("4-10")
animals = ["Zebra","Lion","Elephant","Koala","Monkey"]
print(f"The first 3 animals in the list are {animals[:3]}")
print(f"The middle 3 animals in the list are {animals[1:4]}")
print(f"The last 3 animals in the list are {animals[-3:]}")
print("\n\n")


#4-11 My Pizzas, Your pizzas
#Make copy of original pizza list
#add new pizza to original list
#add new pizza to new list
#print out each list, looping through pizzas
print("4-11")
pizzas = ["Pepperoni","Margherita","Ham and Cheese"]
friend_pizzas = pizzas[:]
pizzas.append("Spam")
friend_pizzas.append("Firehot Tandori")
print("My favourite pizzas are:")
for pizza in pizzas:
	print (f"\t{pizza}")

print("My friend's favourite pizzas are:")
for pizza in friend_pizzas:
	print (f"\t{pizza}")


print("\n\n")




#4-13 Buffet
#Create a tuple that will store 5 foods
foods = ("bread","bananas","peaches","pasta","peanuts")
for food in foods:
	print(food)
#below - try to modify first food to something else - will throw an error
#foods[0] = "vinegar"
#change  2 foods
print("\nRevised menu:")
foods = ("bread","acorns","peaches","pasta","carrots")
for food in foods:
	print(food)
print("\n\n")



