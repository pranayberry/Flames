#Flames Calculator
result = {
			'f':"Friendzoned (Friend)",
			'l':"You Have Found the One (Lover)",
			'a':"You Might Hit Things Off (Affair)",
			'm':"You Lucky Bastard (Marriage)",
			'e':"Better Keep a Distance (Enemy)",
			's':"Sister (Self Explanatory)"
		 };
def inp():
	while True:
		name1 = raw_input("Enter Your Name\n>")
		name2 = raw_input("Enter Your Crush's\n>")
		name1 = name1.lower()			
		name2 = name2.lower()
		name1 = name1.replace(" ","")
		name2 = name2.replace(" ","")
		if name1 != name2 and name1.isalpha() and name2.isalpha():      #Inputing data till user enters the correct input.
			break
		else:
			print "Invalid Input!!\n\n"
	return name1,name2

def calc():
	flames = "flames"
	name1,name2 = inp()													#Calling the input function 
	
	for c in name1:														#Iterating over name1
		if c in name2: 													#Checking for common characters in name2
			name1 = name1.replace(c,"",1)								
			name2 = name2.replace(c,"",1)
	length = len(name1) + len(name2)									#Final length of uncommon characters.
	while len(flames)!=1:
		if length%len(flames) == 0:										#Exception Handling
			flames  = flames[:len(flames)-1]
		else:
			x = length%len(flames)
			flames = flames[x:] + flames[:x-1]							#Calculation of final result.
	print 
	return flames

def display():
	print result[calc()]												#Calling the calculator function.

display()	
