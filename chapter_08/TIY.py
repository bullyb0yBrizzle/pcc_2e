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
	