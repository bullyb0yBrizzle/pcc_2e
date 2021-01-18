# practice

#message =input("Insert something here to play back")
#print(message)

# 7-1 Rental Car
# What car of rental car would you like?
# Print message

#message = input("What kind of a rental car would you like?: ")
#print(f"\nLet me see if I can find you a {message}")

# 7-2 Restaurant Seating
# Write a program that asks the user how mant people are in their dinner
# group. If > 8 print msg saying to wait, otherwise table ready

#question =input("How many people are there in your dinner party?: ")
#question = int(question)

#if question > 8:
	#print ("\nYou'll have to wait")
#else:
	#print ("\nPlease be seated")

# 7-3 Multiples of Ten
# Ask user for a number and then report whether the number is a 
# multiple of 10

#number = input("Give me a number goddam it...?: ")
#number = int(number)

#if number % 10 == 0:
	#print("\nYours is one number that is multiple of 10")
#else:
	#print("\nNot divisible by 10")
	

# 7-4 Pizza Toppings
# Write loop that prompts user to enter a series of pizz toppings
# until a quit value is entered.  As they enter each topping print
# message saying you'll add that topping to pizza

#prompt =  "\nPlease enter a pizza topping:"
#prompt += "\n(Enter 'quit' when you are finished.)"

#while True:
	#topping = input(prompt)
	#if topping == 'quit':
		#break
	#else:
		#print(f"I'll add {topping.title()} to the pizza")

# 7-5 Movie Tickets
# Theatre charges based upon age
# <3 - free
# >= 3 & <= 12 - 10
# >12 - 15
# Write a loop in which you ask users their age and tell them 
# the cost of their movie ticket


#prompt =  "\nPlease enter your age:"
#prompt += "\n(Enter 'quit' when you are finished.)"

#while True:
	#age = input(prompt)
	#if age == 'quit':
		#break
	#elif int(age) < 3 :
		#print(f"free")
	#elif int(age) >=3 and int(age) <=12:
		#print("£10")
	#elif int(age) > 12 :
		#print ("£15")

# 7-6 Three Exits
# Write different versions of above that do each of the following:
# Conditional test in while to stop loop
# Use an active variable to control how long the loop runs
# User a break statement to exit loop (ALREADY DONE)


#USING ACTIVE FLAG
#prompt =  "\nPlease enter your age:"
#prompt += "\n(Enter 'quit' when you are finished.)"

#active = True

#while active:
	#age = input(prompt)
	#if age == 'quit':
		#active = False
	#elif int(age) < 3 :
		#print(f"free")
	#elif int(age) >=3 and int(age) <=12:
		#print("£10")
	#elif int(age) > 12 :
		#print ("£15")



#USING CONDITIONAL TEST
#prompt =  "\nPlease enter a pizza topping:"
#prompt += "\n(Enter 'quit' when you are finished.)"

#topping = ""

#while topping != "quit":
	#topping = input(prompt)
	#print(f"I'll add {topping.title()} to the pizza")


# 7-8 Deli
# Make a list called sandwich_orders and fill with names of various
# sandwiches.  Then make an empty list called finished_sandwiches.  
# Loop through the list of sandwich orders and print a message for 
# each order.  As each sandwich is madem move it to list of finished 
# sandwiches.  After all sandwiches have been made, print a message
# listing each sandwich that has been made

sandwich_orders = ["cheese","ham","marmite"]
finished_sandwiches = []

while sandwich_orders:
	current_sandwich = sandwich_orders.pop()
	print(F"sandwich order for {current_sandwich} now completed")
	finished_sandwiches.append(current_sandwich)	

print("\nThe following sandwiches have been confirmed:")
for s in finished_sandwiches:
	print(f"\t{s}")

print("\n")

# 7-9 No Pastrami
# Using the similar list to above, add 3x instances of pastrami
# Add code near beginning to say deli has run out of pastrami
# Then use while loop to remove all instances of pastrami making 
# sure none ends up in finished sandwiches

sandwich_orders = ["cheese","pastrami","ham","pastrami","marmite","pastrami"]
finished_sandwiches = []

while 'pastrami' in sandwich_orders:
	sandwich_orders.remove("pastrami")

while sandwich_orders:
	current_sandwich = sandwich_orders.pop()
	print(F"sandwich order for {current_sandwich} now completed")
	finished_sandwiches.append(current_sandwich)	

print("\nThe following sandwiches have been confirmed:")
for s in finished_sandwiches:
	print(f"\t{s}")


# 7-10 Dream Vacation
# Write a program that polls a user about their dream vacation
# Write a prompt that asks if you could go anywhere in the world,
# where would you go
# Include a block of code to print results


responses = {}
polling_active = True

while polling_active:
	name = input("\nWhat is your name? ")
	vacation = input("Where is your dream destination? ")

##THIS LINE BELOW IS MENTAL
	responses[name] = vacation
	another = input("Would you like to let another person enter their dream destination? (yes/no) ")
	if another == 'no':
		polling_active = False


print("\n --- Destination Results ---")
for k,v in responses.items():
	print(f"{k} would like to go to {v}")
