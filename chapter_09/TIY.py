#9-1. Restaurant: Make a class called Restaurant. The __init__()
# method for Restaurant should store two attributes: a
# restaurant_name and a cuisine_type. Make a method called
# describe_restaurant() that prints these two pieces of
# information, and a method called open_restaurant() that prints
# a message indicating that the restaurant is open. Make an
# instance called restaurant from your class. Print the two 
# attributes individually, and then call both methods. 

# 
class Restaurant:
	def __init__(self,restaurant_name,cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		description = f"Restaurant name is {self.restaurant_name.title()} and \
cuisine_type is {self.cuisine_type.title()}"
		return description

	def open_restaurant(self):
		print(f"The {self.restaurant_name.title()} is open")

restaurant = Restaurant("The lamb and flag","English")

print(restaurant.describe_restaurant())
restaurant.open_restaurant()



#9-2. Three Restaurants: Start with your class from Exercise 9-1.
# Create three different instances from the class, and call
# describe_restaurant() for each instance. 


restaurant1 = Restaurant("The kebab and calculator","Greek")
restaurant2 = Restaurant("The Mouse","British")
restaurant3 = Restaurant("Raj Pavillions","Indian")

print(restaurant1.describe_restaurant())
print(restaurant2.describe_restaurant())
print(restaurant3.describe_restaurant())


# 9-3. Users: Make a
# class called User. Create two attributes called first_name and
# last_name, and then create several other attributes that are
# typically stored in a user profile. Make a method called
# describe_user() that prints a summary of the user’s information.
# Make another method called greet_user() that prints a
# personalized greeting to the user.
 
class User:
	def __init__(self,first_name,last_name,age,gender,location):
 		self.first_name = first_name
 		self.last_name = last_name
 		self.age = age
 		self.gender = gender
 		self.location = location
 		self.name = f"{first_name} {last_name}"

	def describe_user(self):
 		print(f"The user details are as follows:\n\t\
First name is {self.first_name} \n\t\
Last name is {self.last_name} \n\t\
Age name is {self.age} \n\t\
Gender is {self.gender} \n\t\
Location is {self.location}")

	def greet_user(self):
 		print (f"Hi {self.name}, hope you're doing ok")

me = User("Nicholas","Bull",40,"Male","Bangkok")

me.describe_user()
me.greet_user()

print("\n")




# 9-4. Number Served: 
# start with your program from Exercise 9-1 (page 162). Add an
# attribute called number_served with a default value of 0. Create
# an instance called restaurant from this class. Print the number
# of customers the restaurant has served, and then change this
# value and print it again. Add a method called set_number_served()
# that lets you set the number of customers that have been served.
# Call this method with a new number and print the value again.
# Add a method called increment_number_served() that lets you
# increment the number of customers who’ve been served. Call this
# method with any number you like that could represent how many
# customers were served in, say, a day of business.

class Restaurant:
	def __init__(self,restaurant_name,cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		description = f"Restaurant name is {self.restaurant_name.title()} and \
cuisine_type is {self.cuisine_type.title()}"
		return description

	def open_restaurant(self):
		print(f"The {self.restaurant_name.title()} is open")

	def set_number_served(self,number_served):
		self.number_served = number_served

	def increment_number_served(self,served):
		self.number_served += served
		return self.number_served

myrestaurant = Restaurant("Chandos Deli","Spanish")
print(myrestaurant.number_served)
myrestaurant.set_number_served(4)
print(myrestaurant.number_served)

myrestaurant.increment_number_served(5)
print(myrestaurant.number_served)

print("\n")

# 9-5. Login Attempts: 
# Add an attribute called login_attempts to your User class from
# Exercise 9-3 (page 162). Write a method called
# increment_login_attempts() that increments the value of
# login_attempts by 1. Write another method called
# reset_login_attempts() that resets the value of login_attempts
# to 0.
# Make an instance of the User class and call
# increment_login_attempts() several times. Print the value of
# login_attempts to make sure it was incremented properly, and
# then call reset_login_attempts(). Print login_attempts again to
# make sure it was reset to 0.


class User:
	def __init__(self,first_name,last_name,age,gender,location):
 		self.first_name = first_name
 		self.last_name = last_name
 		self.age = age
 		self.gender = gender
 		self.location = location
 		self.name = f"{first_name} {last_name}"
 		self.login_attempts = 0

	def describe_user(self):
 		print(f"The user details are as follows:\n\t\
First name is {self.first_name} \n\t\
Last name is {self.last_name} \n\t\
Age name is {self.age} \n\t\
Gender is {self.gender} \n\t\
Location is {self.location}")

	def greet_user(self):
 		print (f"Hi {self.name}, hope you're doing ok")

	def increment_login_attempts(self):
 		self.login_attempts += 1
 		

	def reset_login_attempts(self):
 		self.login_attempts = 0

me = User("Nicholas","Bull",40,"Male","Bangkok")

me.increment_login_attempts()
me.increment_login_attempts()
me.increment_login_attempts()
me.increment_login_attempts()
me.increment_login_attempts()
me.increment_login_attempts()
print(me.login_attempts)

me.reset_login_attempts()
print(me.login_attempts)
me.increment_login_attempts()
me.increment_login_attempts()
me.increment_login_attempts()
print(me.login_attempts)
print("\n")


#9-6. Ice Cream Stand: An ice cream stand is a specific kind of
# restaurant. Write a class called IceCreamStand that inherits
# from the Restaurant class you wrote in Exercise 9-1 (page 162)
# or Exercise 9-4 (page 167). Either version of the class will
# work; just pick the one you like better. Add an attribute called
# flavors that stores a list of ice cream flavors. Write a method
# that displays these flavors. Create an instance of IceCreamStand,
# and call this method.

class IceCreamStand(restaurant):

	def __init__(self,restaurant_name,cuisine_type):
		super().__init__(self,restaurant_name,cuisine_type)
		self.flavors = ["Honey","Bumsuckle","Choccy chip"]

	def display_flavors(self)
		for 

