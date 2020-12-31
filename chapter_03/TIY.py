
#3-1
print("3-1")
#Instantitate names list
names = ['Dave','Allen','Pete','Fred','Mr Dead']
#Print first name
print(f"Hi {names[0]}" )
#Print second name
print(f"Hi {names[1]}\n\n" )

#3-2 
print("3-2")
#custom messages - third name
print(f"Hi {names[2]}, hope you're ok?")

#custom messages - fourth name
print(f"Hi {names[3]}, hope you don't have covid like {names[0]}?\n\n")

#3-4
print("3-4")
#Guest-list - print all names in list
Guestlist = ['Bobby Brown','Whitney Houston','Art Monk','Roy Keane']
print (f"Hi {Guestlist[0]}, would you like to come to dinner?")
print (f"Hi {Guestlist[1]}, would you like to come to dinner?")
print (f"Hi {Guestlist[2]}, would you like to come to dinner?")
print (f"Hi {Guestlist[3]}, would you like to come to dinner?")
Guestcnt = len(Guestlist)
print (f"There will be {Guestcnt} guests coming to dinner\n\n")



#3-5
#Remove name from list - not enough space for everyone
#Note - remove only works with text, cannot use index postion
print("3-5")
print(f"Unfortunately {Guestlist[1]} cannot make dinner")
Guestlist.remove("Whitney Houston")
print (f"Hi {Guestlist[0]}, would you like to come to dinner?")
print (f"Hi {Guestlist[1]}, would you like to come to dinner?")
print (f"Hi {Guestlist[2]}, would you like to come to dinner?")
Guestcnt = len(Guestlist)
print (f"There will be {Guestcnt} guests coming to dinner\n\n")

#3-6
#found new table, more seats available
print("3-6")
print("Hold the phone! Just found a MASSIVE dining table")
#insert guest at beginning of list
Guestlist.insert(0,'Hulk Hogan')
#insert guest in middle of list
Guestlist.insert(3,'Brian Hogan')
#insert guest at end of list
Guestlist.append('William Shakespeare')
print (f"Hi {Guestlist[0]}, would you like to come to dinner?")
print (f"Hi {Guestlist[1]}, would you like to come to dinner?")
print (f"Hi {Guestlist[2]}, would you like to come to dinner?")
print (f"Hi {Guestlist[3]}, would you like to come to dinner?")
print (f"Hi {Guestlist[4]}, would you like to come to dinner?")
print (f"Hi {Guestlist[5]}, would you like to come to dinner?")
Guestcnt = len(Guestlist)
print (f"There will be {Guestcnt} guests coming to dinner\n\n")


#3-7
#Shrinking guest list - table just not that big
print("3-7")
print("Soz, everyone. Table has turned out to be a tiny thing. Only 2 can come to dinner")
#Remove all guests until 2 remain.  Send message each time someone removed
Unluckyloser = Guestlist.pop()
print (f"Really sorry {Unluckyloser} but you didn't make supper club this time round!")
Unluckyloser = Guestlist.pop()
print (f"Really sorry {Unluckyloser} but you didn't make supper club this time round!")
Unluckyloser = Guestlist.pop()
print (f"Really sorry {Unluckyloser} but you didn't make supper club this time round!")
Unluckyloser = Guestlist.pop()
print (f"Really sorry {Unluckyloser} but you didn't make supper club this time round!")
print(f"Hey {Guestlist[0]}, just letting you know you made the cut!")
print(f"Hey {Guestlist[1]}, just letting you know you made the cut!")
Guestcnt = len(Guestlist)
print (f"There will be {Guestcnt} guests coming to dinner\n\n")
#Table being removed, no one going to dinner
del Guestlist[1]
del Guestlist[0]
#Empty guestlist
print(Guestlist)
print("\n")

#3-8
#Seeing the world
#Five different places I would like to visit
print ("3-8")
places = ["Thailand","St. Lucia","St. Barts","St. Vincent and the Grenadines","Vietnam"]
#Print places in raw order
print(places)
#Now print in alphabetical order using sorted() method
print(sorted(places))
#Print original list to prove only sorted when above was using sorted
print(places)
#Print original list in reverse alphabetical order
print(sorted(places,reverse=True))
#Print original list to prove only sorted when above was using sorted
print(places)
#Change the order of the list by reversing permanently
places.reverse()
#Print to show changes have been made permanently
print(places)
#And now reverse again to put it back to normal
places.reverse()
#Print to show changes have been made permanently
print(places)
#Now sort list permanently into alphabetical order
places.sort()
#Print to show changes have been made permanently
print(places)
#Now sort list permanently into reverse alphabetical order
places.reverse()
#Print to show changes have been made permanently
print(places)
print(F"\n\n")










