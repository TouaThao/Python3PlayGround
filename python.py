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