"This is hello world"
print("Hello World")

"This is my first shape"
print("|---/")
print("|  /")
print("| /")
print("|/")

" This is to change character name and age with a variable "
"note: This allow us to change character name and age just with the variable instead of going line by line"
"note: this will save time and effort"
character_name = "Jonny"
character_age = "19"
print("There once was a man name " + character_name +",")
print("He was "+ character_age +  " years old")
print("He really like the name "+ character_name +",")
print("But he didn't like being "+ character_age)

"Working with string"
"adding a new line into the string. Adding a backslash in python mean an escape"
print("Coding is\n life")
print("Coding is\" life")
phrase = "Coding is life"
print(phrase.upper())
print(phrase.lower())
print(phrase.upper().isupper())
print(len(phrase))
print(phrase[0])
print(phrase.index('C'))
print(phrase.replace('Coding','Learning'))


"working with number"
"we could use negative number, and decimal. We could also do basic arithmetic, order operation"
print( 3+ 6)
print(4 - 2)
print( 5 * ( 9 * 3))
" we could also change number to string"
my_num = 6
print(my_num)
print(str( my_num ) + " is my favorite")
" Here we're going to round the number"
print(round(3.7))
" next we're going import more math to python"
from math import*
print(floor(3.2))
print(ceil(4.2))
print(sqrt(64))

# "Storing user input"
# name = input('enter your name ')
# age = input('enter your age ')
# print('hello ' + name + ' and your age is ' +age)

# color = input("Enter a color:")
# pluralNoun = input("Enter a pluralNoun:")
# celebrity = input("Enter a celebrity:")

# print("Rose are " + color)
# print(pluralNoun +" are blue")
# print("I love "+ celebrity)
# print('hello '+ celebrity + ' favorite Color is ' + color+' And you like '+ pluralNoun)

"Now we're going to built a list"
friends = ['Toua','Thor','Trigun']
"we could change the data inside of the friend array"
friends[1]= 'Tass'
print(friends)
print(friends[1])

"list function"
Lucky_numbers = [7,14,21,28]
my_friends = ['Thor','IronMan','CaptainAmerica','Thor']
"We could extend list to another list. It's like attaching them togather"
my_friends.extend(Lucky_numbers)
"we could append. which mean to add something to the list. it's like a .push"
my_friends.append('Hawkeye')
'We could do insert. insert is to put in exactly what it mean. We need to put a number or postion of the new'
'And the new data'
my_friends.insert(1,'BlackWidow')
'we could do remove. remove and we could select which we remove by typing in the name of the data'
my_friends.remove('IronMan')
'We could do a clear. This will clear the list'
'we going to comment the clear out'
'my_friends.clear()'
'Pop will remove the last one'
'my_friends.pop()'
'print(my_friends)'
'we going find a specifc value'
print(my_friends.index('BlackWidow'))
'Now we could also find out how many time it show up on our array'
print(my_friends.count('Thor'))
'Reverse'
print(my_friends.reverse())

coordinates = [(4,5),(6,7),(80,34)]
