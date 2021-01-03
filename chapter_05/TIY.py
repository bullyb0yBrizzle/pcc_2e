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
