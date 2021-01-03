#5-1 - conditional tests

foot = 'big'
print("Is my foot == big?  I predict True")
print(foot=='big')
print("\n")

print("Is my foot == small?  I predict False")
print(foot=='small')
print("\n")

##using lower case
print("Is my foot == big using lower()?  I predict True")
print(foot.lower()=='big')
print("\n")

#<>
print("Is my foot <> big using lower()?  I predict False")
print(foot.lower()!='big')
print("\n")


#not in list 
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
	print(f"{user} is not in the list")

#in list 
banned_users = ['andrew', 'carolina', 'david']
user = 'andrew'
if user in banned_users:
	print(f"{user} is in the list")
print("\n\n")


#5-3 Alien Colours
#Use if to determine alien colour

#Pass
alien_colour ='Green'
if alien_colour.lower() == 'green':
	print ("Green - 5 Points")

#Fail
alien_colour ='red'
if alien_colour.lower() == 'green':
	print ("Green - 5 Points")
print("\n\n")

#5-4 Alien Colours 2
# Use if/else - v1 in if
alien_colour ='Green'
if alien_colour.lower() == 'green':
	print ("5 Points")
else:
	print  ("10 Points")

# Use if/else - v2 in else
alien_colour ='Green'
if alien_colour.lower() != 'green':
	print ("5 Points")
else:
	print  ("10 Points")
print("\n\n")

#5-5 Alien Colours 3
#Use if/else/elif to determine alien colour
alien_colour ='Green'
if alien_colour.lower() == 'green':
	print ("5 Points")
elif alien_colour.lower() == 'yellow':
	print  ("10 Points")
else:
	print  ("15 Points")
print("\n")

alien_colour ='yellow'
if alien_colour.lower() == 'green':
	print ("5 Points")
elif alien_colour.lower() == 'yellow':
	print  ("10 Points")
else:
	print  ("15 Points")
print("\n")

alien_colour ='red'
if alien_colour.lower() == 'green':
	print ("5 Points")
elif alien_colour.lower() == 'yellow':
	print  ("10 Points")
else:
	print  ("15 Points")
print("\n")

#5-6 
#Write if-elif-else for:
# <2 
# >=2 & <4
# >=4 & <13
# >=13 & <20
# >=20 & <65
# >=65

age = 101

if age < 2:
	print ("baby")
elif age >= 2 and age < 4:
	print  ("toddler")
elif age >= 4 and age < 13:
	print  ("kid")
elif age >= 13 and age < 20:
	print  ("teenager")
elif age >= 20 and age < 65:
	print  ("adult")
elif age >= 65:
	print  ("elder")
print("\n")


#5-7
#favourite fruits - check whether value is in the list
favourite_fruits = ["Banana","Orange","Lemon","Apple","Kiwi"]

if "Banaaa" in favourite_fruits:
	print("In list")
elif "Oraage" in favourite_fruits:
	print("In list - Orange")
elif "satsuma" not in favourite_fruits:
	print ("satsuma not in list")
print("\n\n")

#5-8 + 5-9
#Hello-Admin
# make a list of 5 usernames + admin
# print greeting to each user
#5-9 - add test to make sure list is not empty

usernames = ["Dave","Fred","Alex","Will","Alison","Admin"]
#usernames = []
if usernames:
	for name in usernames:
		if usernames:
			print (f"Hi {name}, so glad you could login again")
		if name == "Admin":
			print ("Hello admin, would you like a sitrep?")
else:
	print("The list is empty, we need to find some users")
print ("\n\n")

#5-10 - Checking usernames
#make list of five or more users
#make list of five new users
#loop through new list to see if exists.  If it does enter message to create a new username
#if username not used print message to say it's available
#ensure case sensativity is switched off

current_users = ['John','Dave','Phil','Brian','Allen']
new_users = ['Felix','Matthew','John','Allen','Steve']

#use list comprehension to convert all to lower case
current_users = [user.lower() for user in current_users]
new_users = [user.lower() for user in new_users]

for usern in new_users:
	if usern in current_users:
		print(f"Sorry {usern} that name has already been taken")
	else:
		print(f"{usern} is available")


print("\n")
#5-11 - Ordinal numbers
# Store number 1-9
#Loop through and print ordinal ending of number

numbers = list(range(1,10))

for n in numbers:
	if n == 1:
		print ("1st")
	elif n == 2:
		print ("2nd")
	elif n == 3:
		print ("3rd")
	else:
		print(f"{n}th")
