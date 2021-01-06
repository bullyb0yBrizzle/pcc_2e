# 6-1
# Use dictionary to store information about a person you know
# Store:
# Firstname
# Lastname
# Age
# City

person = {
	"firstname": "Dave",
	"lastname": "Smith",
	"Age": 21,
	"City": "Bristol"

}

print (person.get("firstname"))
print (person.get("lastname"))
print (person.get("Age"))
print (person.get("City"))


print (person)
print ("\n")

# 6-2 
# Five friends and their favourite numbers
favs = {"Dave":1,
"Allen":2,
"Jane":3,
"Peter":4,
"Fred":5
}

print(f"Dave's favourite number is {(favs.get('Dave'))}")
print(f"Allen's favourite number is {(favs.get('Allen'))}")
print("\n")

# 6-3
# Glossary
# Create a glossary using words learned so far:
words = {
	"print()":"print information on screen",
	"get()":"get value of key-value pair in dictionary. If value absent 'none' returned",
	"list()":"create list using values supplied in parenthesis"
}

print(f"print()\n\t{(words.get('print()'))}")
print(f"get()\n\t{(words.get('get()'))}")
print(f"list()\n\t{(words.get('list()'))}")
print ("\n")

# 6-4 Glossary 2
# change glossary output to a loop
words = {
	"print()":"print information on screen",
	"get()":"get value of key-value pair in dictionary. If value absent 'none' returned",
	"list()":"create list using values supplied in parenthesis"
}
print("\n")

#print all keys and values using items()
for k,v in words.items():
	print(f"{k}\n\t{v}")
print("\n")

# print all keys
for k in words.keys():
	print(f"{k}")
print("\n")

# print all values
for v in words.values():
	print(f"{v}")
print("\n")

# 6-5 Rivers
# Make a dictionary containing 3 rivers and the country
# each river runs through

rivers = {
	"nile":"egypt",
	"danube":"hungary",
	"avon":"england"

}

for r,c in rivers.items():
	print (f"The {r.title()} runs through {c.title()}")
print("\n")

for r in rivers.keys():
	print (f"{r.title()}")
print("\n")

for c in rivers.values():
	print (f"{c.title()}")
print("\n")

# 6-6 Polling
# Make a list of people who should take the favourite languages poll
# Loop through list of people who should take poll
# If they have already taken the poll print a message thanking them for responding
# If not, print a message inviting them to take the poll

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

people = ["dave","phil","steve","roger","jen"]

for p in sorted(people):
	if p in favorite_languages.keys():
		print (f"Thank you {p.title()} for taking the poll")
	else:
		print (f"Please {p.title()} take the goddamned poll!!")
print("\n")

# 6-7 People
# Store 3 dictionaries inside a list
# Loop through list and print out all you know
People =[]

Dave = {
	"firstname": "Dave",
	"lastname": "Smith",
	"Age": 21,
	"City": "Bristol"
}

Stebbie = {
	"firstname": "Stebbie",
	"lastname": "Lath",
	"Age": 29,
	"City": "Bath"
}

Jackie = {
	"firstname": "Jackie",
	"lastname": "Jeens",
	"Age": 76,
	"City": "Barnstaple"
}

People.append(Dave)
People.append(Stebbie)
People.append(Jackie)

print("We know the following about all the people:\n")
#print(People)
for p in People:
	
	for k,v in p.items():
		print(f"\t{k} - {v}")
	print("\n") 


# 6-8 - Pets
# Make several dictionaries, each one representing a pet
# In each dictionary, include "kind" + "owner name"
# Store these dictionaries in a list called pets
# Loop through list and print everything you know

Rat = {
	"name":"rat",
	"kind":"rodent",
	"owner_name":"dave"
}

Cat = {
	"name":"cat",
	"kind":"feline",
	"owner_name":"chas"
}

Parrot = {
	"name":"parrot",
	"kind":"bird",
	"owner_name":"tracey"
}

Dog = {
	"name":"dog",
	"kind":"dog",
	"owner_name":"dogg the bounty hunter"
}

Horse = {
	"name":"horse",
	"kind":"equine",
	"owner_name":"feliz"
}

pets=[]
pets.append(Rat)
pets.append(Cat)
pets.append(Parrot)
pets.append(Dog)
pets.append(Horse)
print("This is what we know about the pets:\n")
for p in pets:
	for  k,v in p.items():
		print(F"\t{k} - {v}")
	print("\n")


# 6-9 - Favourite Places
# Make a dictionary called favourite places
# Think of 3 names to use as keys in dictionary and store 1 to 3 
# favourite places per person.  Loop through dictionary and print
# each person's name andd their favourite places

favourite_places = {
 	"Dave":["Austria","Quebec"],
 	"Barry":["Sunderland","Mansfield"],
 	"Alistair":["Plymouth","Mexico"],
 	"Richie":["Harlow"],
 	"Jenny":["Bangkok","Koh Lanta","Koh Samui"]
	}

for k,v in favourite_places.items():
 	print(f"{k}'s favourite places are:")
 	for i in v:
 		print (f"\t{i}")
 	print("\n")


# 6-10 - Favourite numbers
# Make sure each user can have one or more favourite number
# Then print each person's name along with their favourite number

favs = {"Dave":[1,7,9],
"Allen":[2],
"Jane":[3,4],
"Peter":[4,76,87],
"Fred":[5,85]
}

for k,v in favs.items():
 	print(f"{k}'s favourite numbers are:")
 	for i in v:
 		print (f"\t{i}")
 	print("\n")
print("\n")

# 6-11 - Cities
# Make a dictionary called cities.  Use the names of three cities
# as keys in the dictionary. Create a dictionary of information
# about each city and include the country that the city is in, its
# approximate population, and one fact about that city.  The keys
# for each city's dictionary should be something like country, 
# population and fact.  Print the name of each city and all of
# the information you have stored about it

cities {
	"Bristol":{
	"country":"england",
	"population":"500000",
	"fact":"The place to be"
	}
	"Bath":{
	"country":"england",
	"population":"200000",
	"fact":"Roman baths are here"
	}
}
