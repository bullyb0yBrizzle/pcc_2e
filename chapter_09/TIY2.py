class Human:
	def __init__(self,name,sex,age,height):
		self.name = name
		self.sex = sex
		self.age = age
		self.height = height

	def details(self):
		hdetails = f"Name is {self.name}, sex is {self.sex}, age \
is {self.age} and height is {self.height}"
		return (hdetails)

	def which_sex(self):
		print (f"The sex of {self.name} is {self.sex}")

me = Human("Nick","Male","40","5ft8in")

print(me.details())
me.which_sex()