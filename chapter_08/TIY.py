# 8-1 Message
# Write a function called display_message() that prints one sentence
# telling everyone what you are learning about in this chapter. Call it


def display_message(username):
	"""Display a simple greeting."""
	print(f"Hello, {username.title()}! I'm learning functions")


display_message('jesse')


# 8-2 Favourite Book
# Write a function called favouorite book that accepts one param, 
# title. The function should print a message, such as One of my favourite books is

def favourite_book(title):
	"""Show Favourite Book"""
	print(f"One of my favourite books is {title.title()}")


favourite_book("Misery")

# 8-3 T-shirt
#Write a function called make_shirt() that accepts a size
#and the text of a message that should be printed on the shirt. 
#The function should print a sentence summarizing the size of the 
#shirt and the message printed on it. Call the function once using 
#positional arguments to make a shirt. Call the function a second time
#using keyword arguments.

def make_shirt(size,message):
	print(f"T-shirt size is {size}")
	print(f"T-shirt message is {message}")

#calling using positional arguments
make_shirt('Large',"This shirt is MAHOOSIVE")

#calling using keyword arguments
make_shirt(size='Medium',message="This shirt is MEH")

#calling using keyword arguments
make_shirt(message="This shirt is MEH",size='Medium')

#8-4. Large Shirts: Modify the make_shirt() function so that shirts
# are large by default with a message that reads I love Python. Make 
#a large shirt and a medium shirt with the default message, and a 
#shirt of any size with a different message.

def make_shirt(size='Large',message='I love Python'):
	print(f"T-shirt size is {size}")
	print(f"T-shirt message is {message}")

make_shirt()
make_shirt('Medium')

make_shirt(message='This t-shirt is da bomb')


# 8-5. Cities: Write a function called describe_city() that accepts
# the name of a city and its country. The function should print a 
# simple sentence, such as Reykjavik is in Iceland. Give the 
# parameter for the country a default value. Call your function for 
# three different cities, at least one of which is not in the default 
# country.

def describe_city(city,country='Iceland'):
	print(f"{city.title()} is in {country.title()}")

describe_city ('Bristol','England')
describe_city ('Bangkok','Thailand')
describe_city ('Reykjavik')



# 8-6. City Names: Write a function called city_country() that takes
# in the name of a city and its country. The function should return
# a string formatted like this:

# "Santiago, Chile"

# Call your function with at least three city-country pairs, and 
# print the values that are returned.

def city_country(city,country):
	retval = f"{city.title()}, {country.title()}"
	return retval

myformattedcountry = city_country("Bristol","England")
print(myformattedcountry)
myformattedcountry = city_country("Bath","England")
print(myformattedcountry)
myformattedcountry = city_country("Bangkok","Thailand")
print(myformattedcountry)

# 8-7. Album: Write a function called make_album() that builds
# a dictionary describing a music album. The function should take 
# in an artist name and an album title, and it should return a dictionary 
# containing these two pieces of information. Use the function to make
# three dictionaries representing different albums. Print each return
# value to show that the dictionaries are storing the album information
# correctly. Use None to add an optional parameter to make_album() that
# allows you to store the number of songs on an album. If the calling line
# includes a value for the number of songs, add that value to the album’s
# dictionary. Make at least one new function call that includes the number
# of songs on an album.

def make_album(artist,album,songs=None):
	album = {'Artist':artist, 'Album':album}
	if songs:
		album['Songs'] = songs
	return album


album = make_album('Dire Straits','Money for Nothing')
print(album)
album = make_album('Foo Fighter','In your honour',14)
print(album)

# 8-8. User Albums: Start with your program from Exercise 8-7. Write a 
# while loop that allows users to enter an album’s artist and title. Once
# you have that information, call make_album() with the user’s input and
# print the dictionary that’s created. Be sure to include a quit value in
# the while loop.

# def make_album(artist,album,songs=None):
# 	album = {'Artist':artist, 'Album':album}
# 	if songs:
# 		album['Songs'] = songs
# 	return album


# while True:
# 	print("\nEnter artist and album to make new album")
# 	print("(Enter q to quit at any time)")

# 	art_name = input("Artist: ")
# 	if art_name == 'q':
# 		break

# 	alb_name = input("Album: ")
# 	if art_name == 'q':
# 		break
# 	album = make_album(art_name,alb_name)
# 	print(album)



# 8-9. Messages: Make a list containing a series of short text messages. Pass 
# the list to a function called show_messages(), which prints each text message.



def show_messages(messages):
	for m in messages:
		msg = f'Message is "{m.title()}"'
		print(msg)


messages = ["Hey, how you doing?","Sorry I couldn't get through","If you leave your name and your number...","I'll get back to you"]

show_messages(messages)


# 8-10. Sending Messages: Start with a copy of your program from Exercise 8-9. 
# Write a function called send_messages() that prints each text message and
# moves each message to a new list called sent_messages as it’s printed. After
# calling the function, print both of your lists to make sure the messages were
# moved correctly.


def show_messages(messages,sent_messages):
	while messages:
		current_message = messages.pop()
		print(f"Processing message: {current_message}")
		sent_messages.append(current_message)
	
def show_sent_messages(sent_messages):
	print ("\nThe following messages have been processed::")
	for s in sent_messages:
		print(s)


unsent_messages = ["Hey, how you doing?","Sorry I couldn't get through","If you leave your name and your number...","I'll get back to you"]
processed_messages = []

show_messages(unsent_messages,processed_messages)
show_sent_messages(processed_messages)
print ("\n")

# 8-11. Archived Messages: Start with your work from Exercise 8-10. Call the
# function send_messages() with a copy of the list of messages. After calling the
# function, print both of your lists to show that the original list has retained 
# its messages.

unsent_messages = ["Hey, how you doing?","Sorry I couldn't get through","If you leave your name and your number...","I'll get back to you"]
processed_messages = []

show_messages(unsent_messages[:],processed_messages)
show_sent_messages(processed_messages)

print(unsent_messages)

# 8-12. Sandwiches: Write a function that accepts a list of items a person wants
# on a sandwich. The function should have one parameter that collects as many
# items as the function call provides, and it should print a summary of the 
# sandwich that’s being ordered. Call the function three times, using a different number of arguments each time.


def make_sandwich(*toppings):
	print(f"We're about to make a sandwich consisting of:")
	for topping in toppings:
		print(f"\t{topping}")


make_sandwich("ham","mustard","cheese")
make_sandwich("pineapple","lettuce")
make_sandwich("vinegar","banana","tomato")
print("\n")

# 8-13. User Profile: Start with a copy of user_profile.py from page 149. 
# Build a profile of yourself by calling build_profile(), using your first 
# and last names and three other key-value pairs that describe you.

def build_profile(first, last, **user_info):
	user_info['first_name'] = first
	user_info['last_name'] = last
	return user_info

user_profile = build_profile('albert', 'einstein',location='princeton',field='physics')
print(user_profile)
user_profile = build_profile('Nicholas', 'Bull',location='Bristol',field='IT',status='Legendry')
print(user_profile)


# 8-14. Cars: 
# Write a function that stores information about a car in a dictionary. The
# function should always receive a manufacturer and a model name. It should
# then accept an arbitrary number of keyword arguments. Call the function with
# the required information and two other name-value pairs, such as a color or
# an optional feature. Your function should work for a call like this one:
# car = make_car('subaru', 'outback', color='blue', tow_package=True) Print the
# dictionary that’s returned to make sure all the information was stored correctly.


def car_info(manufacturer,model,**specifications):
	specifications['manufacturer'] = manufacturer
	specifications['model'] = model
	return specifications

car_details = car_info("ford","satsuma",color="orange",wheels="4",doors=5)
print(car_details)

