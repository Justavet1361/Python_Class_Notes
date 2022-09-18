# string:  a collection of text in Python
    # strings are considered one of the "fundamental", or "primative" data types in Python, along with boolean, float, and int
    # strings are "immutable", they cannot be changed once created.  An existing character cannot be replaced with a new character.
    # examples of other programs that manipulate strings - word processing, e-mail, etc

type('Hello World')   # returns:  <class 'str'>

# a string literal: any string written into the source code and includes the quotation marks.  The characters in the quotes is the "value"
    # strings input by a user or obtained from a file are not considered string literals
# e.g. "Hello World"  is the string literal and Hello World is the value that will display when using print("Hello World")

# strings have three properties
    # characters:  the individual letters and characters that make up the string, these can be any valid Unicode character
    # length:  the number of characters a string contains
    # sequence:  each character has a numbered position in the string
        # A sequence is a python object that supports accessing its elements by index
        # because a string is a sequence, you can iterate over it with a for loop
name = 'Juliet'
for ch in name:
    print(ch)

# Returns (after six iterations)
'''
J
u
l
i
e
t'''

#*****************************************************************(Gaddis, count_Ts.py)
# This program counts the number of times
# the letter T (uppercase or lowercase)
# appears in a string. (Gaddis)  It is doing this by creating a new function called main()

def main():
    # Create a variable to use to hold the count.
    # The variable must start with 0.
    count = 0
    
    # Get a string from the user.
    my_string = input('Enter a sentence: ')

    # Count the Ts.
    for ch in my_string:
        if ch == 'T' or ch  == 't':
            count += 1

    # Print the result.
    print('The letter T appears', count, 'times.')

# Call the main function.
main()

#***********************************************************************
#  Note:  It is easier to access the characters in a string using an index, see below


len('Hello World')   # returns the length of the string - 11
    # The argument can also be a variable that contains a string
letters = 'abc'
len(letters)   # returns 3
# len is useful to prevent loops from iterating beyon the end of a string (Gaddis)
city = 'Boston'
index = 0
while index < len(city):
    print(city[index])
    index += 1  # adds 1 to each iteration

input() # is a function that collects a string from a user (typically via keyboard)
response = input('What should I shout?')   # (Amos et. al p 89)
shouted_response = response.upper()
print('Well, if you insist ' + shouted_response)

# --> Delimiters <--

    # the quotes used to indicate the beginning and end of a string.  Can be single or double as long as both ends match
    # You cannot use the same types together without an error (e.g. you cannot place double quotes inside a string delimited 
    #   by double quotes unless you use an escape character - see below)
    # use either single quotes or double quotes throughout your program - BE Consistent!

# Quotes and Apostrophes:  use one type of quote to enclose another

    # Printing a string literal using a double quote
print("This is a string of text")

    # Printing a string literal using a single quote
print('This is a string of text')


    # printing a string literal that contains a single quote
print("This is a 'string' of text")

    # printing a string literal that contains a double quote
print('This is a "string" of text')

    # printing a string literal that contains a single and double quotes, using triple quotes
print('''This is a "string of 'text'" with different types of quotes''')


some_variable = "This is a string of text" # Using double quotes
some_other_variable = 'This is another string of text' # Using single quotes

print(some_variable)
print(some_other_variable)

# --> Multiple Lines <--

#  - PEP 8 recommends a max programming line of 79 characters, therefore long strings should be broken up
print('''Triple quotes can be used
to print line breaks and formating
as ***typed***
;)''')  #"""" or ''' can be used as triple quotes.  Triple quoted lines preserve white space

paragraph = "This planet has—or rather had—a problem, which was \
this: most of the people living on it were unhappy for pretty much \
of the time. Many solutions were suggested for this problem, but \
most of these were largely concerned with the movements of small \
green pieces of paper, which is odd because on the whole it wasn't \
the small green pieces of paper that were unhappy."  # (Amos, et.al.)   Uses \ at the end of each line except for the last, to insert line breaks.

print("""\
This multi-line string
has no space at the
top or the bottom
when it prints.\
""")        # the backslash is used to remove the space at the beginning and end

# --> Escape Characters <--

#   Backslash \ is used to escape the quotes.  When used inside a string literal it is executed like a command.

    # \n is the new line character.
print('One\nTwo\Three')  # The output of this print statement will be
    # One
    # Two
    # Three

    # \t causes output to skip to the next horizontal tab position
print("Mon\tTues\tWed")
print("Thur\t/Fri\tSat") # the output of this is
# Mon   Tue     Wed
# Thurs Fri     Sat

    # \' causes a single quote mark to be printed
print('Sammy\'s balloon is red.') # backslashes were used to add an apostrophe
# output:  Sammy's balloon is red

    # \" causes a double quote mark to be printed
print("Sammy says, \"Hello!\"") # backslashes were included so that "" could be used inside a "".  The output:
#  Sammy says, "Hello!"

    # \\ causes a backslash character to be printed
print("The path is C:\\temp\\data")  # The output will be:
# The path is C:\temp\data


# Raw strings:  placing a small r in front of a string causes the interpreter to ignore any escape characters
print(r"Sammy says, \" The balloon\'s color is red\"")  #The output will be:
    # Sammy says, \"The balloons\'s color is red\

# --> String Operators <--

#   + can be used to concatenate two strings and does not add space
#   *   integer * a string will reproduce the string "integer" times

print(some_variable + some_other_variable)
# ouput This is a string of textThis is another string of text

print(some_variable + " " + some_other_variable) # adds a space
# ouput This is a string of text This is another string of text

number_5 = '5'

print("This is some" + "text" + "to print" + number_5) #this will produce a runtime error if the variable number_5 is not a string
#   You cannot concantate strings and integers

# You can also use the += operator to perform concatenation
letters = 'abc'
letters += 'def'
print(letters)  # ouput abcdef

print(25 * "#") # output ########################3

# print a different variable type
#   print the number 5
number_5 = 5.0
print(number_5)  # output:  5.0  a float

number_5 = 5
print(number_5)  # output: 5  an int

number_5 = "five"
print(number_5) # output: five      a string

# Changing the variable type
number_5 = str(number_5)

# other available functions for changing data type include int() and float()

# keyword operators    in  not in   general format str1 in/not in str2
text = 'Four score and seven years ago'
if 'seven' in text:
    print('The string "seven" was found.')
else:
    print('The string "seven" was not found')  # Returns The string "seven" was found.

names = 'Bill Joanne Susan Chris Juan Katie'
if 'Pierre' not in names:
    print('Pierre was not found.')
else:
    print('Pierre was found')  # Returns  Pierre was not found.



# --> String Interpolation <--

#   Adding variables in and amongst strings
name = 'Zaphead'
heads = 2
arms = 3
print(name + ' has ' + str(heads) + '  heads and ' + str(arms) + ' arms')   
#   Returns:  Zaphead has 2 heads and 3 arms
# a better way to do this is using f-strings, or formatted strings
print(f"{name}has{heads}heads and{arms}arms")  # Returns Zaphead has 2 heads and 3 arms.  Spaces added.
    # Variable names are surrounded by curley braces {}.  Expressions can also be used in the curly braces, but keep them short.
    # in older versions (earlier than 3.6) the .format method would need to be used to accomplish this.

# printing multiple strings with one print function
print("This is some","text","to print", number_5)  # output:  This is some text to print five

# or you can nest the functions
print("This is some" + "text" + "to print" + str(number_5))

# --> String Indexing <--

#   # each character in a string is assigned a number from 0, 1, ... , n
    # place the n in square brackets [] and that character is returned.
    # forgetting to start at zero results in a lot of "off-by-one" errors
flavor = 'fig pie'
len(flavor)  # returns 7
flavor[3]  # returns ' '
'''flavor[9]  # causes and index error because there are only 7 characters in this string'''
my_string = 'Roses are red'
print(my_string[0], my_string[6], my_string[10])  # output:  R a r
print(my_string[-1], my_string[-2], my_string[-13])  # ouput:  d e R
    # negative indices are also supported.  -1 is the last character in the string
flavor[-1]  # returns e

my_string = 'Roses are red'
print()

# --> String Slicing <--

# general format is string[start:end:step], returns up to but Not including the "end"
#  You could access each character by index and concatenate them like this: (Amos et. el.  p 76)
flavor = 'fig pie' 
first_three_letters = flavor[0] + flavor[1] + flavor[2]

print(first_three_letters)   # returns fig

full_name = 'Patty Lynn Smith'
middle_name = full_name[6:10]   # returns Lynn
first_name = full_name[:5]  # returns Patty,  0 is the default first character
last_name = full_name[11:]  # returns Smith, the last character of the string is the default for the empty space
my_string = full_name[:]    # returns Patty Lynn Smith
my_string = full_name[0:len(full_name)] # does the same thing
# If the start index is greater than the end index, Python returns an empty string

# slicing arguments can also include step values
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(letters[0:26:2])   # returns ACEGIKMOQSUWY

# Substring:  a part of a string.  An easier way to get this...use a colon to designate a range (i.e. slice boundries)
flavor[0:3]   # returns fig  note: The first number in the range is returned (as f), the second
    # number in the range is not returned.  g has an index n = 2
flavor[:3]  # returns the same as above, 0 is the default first index
flavor[3:]  # returns pie, the second number in the range is the last index by default
flavor[:]   # returns fig pie
# Slice boundries can be placed outside the index range without producing an error
flavor[1:14]    # returns  ig pie
flavor[12:16]   # returns ''       an empty string.  Note ' ' is not "empty" because it includes a space.

# Slicing can be done with negative numbers.  Caution, the right most character doesn't have a slicable index number
# flavor[-7,-1]   # returns fig pi
flavor[-7:0]    # returns ''
flavor[-7:]     # is the proper syntax to return the entire string
flavor[-3:]     # returns pie
'''flavor[-3] = a  # causes an error because string characters cannot be re-assigned.  Strings are immutable'''
new = "sweetie" + flavor[-3:]  
print(new)      # returns  sweetiepie

#*************************************************** (Gaddis, login.py)
# The get_login_name function accepts a first name,
# last name, and ID number as arguments. It returns
# a system login name.

def get_login_name(first, last, idnumber):
    # Get the first three letters of the first name.
    # If the name is less than 3 characters, the
    # slice will return the entire first name.
    set1 = first[0 : 3]

    # Get the first three letters of the last name.
    # If the name is less than 3 characters, the
    # slice will return the entire last name.
    set2 = last[0 : 3]

    # Get the last three characters of the student ID.
    # If the ID number is less than 3 characters, the
    # slice will return the entire ID number.
    set3 = idnumber[-3 :]

    # Put the sets of characters together.
    login_name = set1 + set2 + set3

    # Return the login name.
    return login_name

# The valid_password function accepts a password as
# an argument and returns either true or false to
# indicate whether the password is valid. A valid
# password must be at least 7 characters in length,
# have at least one uppercase letter, one lowercase
# letter, and one digit.

def valid_password(password):
    # Set the Boolean variables to false.
    correct_length = False
    has_uppercase = False
    has_lowercase = False
    has_digit = False

    # Begin the validation. Start by testing the
    # password's length.
    if len(password) >= 7:
        correct_length = True

        # Test each character and set the
        # appropriate flag when a required
        # character is found.
        for ch in password:
            if ch.isupper():
                has_uppercase = True
            if ch.islower():
                has_lowercase = True
            if ch.isdigit():
                has_digit = True

    # Determine whether all of the requirements
    # are met. If they are, set is_valid to true.
    # Otherwise, set is_valid to false.
    if correct_length and has_uppercase and \
       has_lowercase and has_digit:
        is_valid = True
    else:
        is_valid = False

    # Return the is_valid variable.
    return is_valid

#****************************************************** (Gaddis, generate_login.py)
# This program gets the user's first name, last name, and
# student ID number. Using this data it generates a
# system login name.

import login

def main():
    # Get the user's first name, last name, and ID number.
    first = input('Enter your first name: ')
    last = input('Enter your last name: ')
    idnumber = input('Enter your student ID number: ')

    # Get the login name.
    print('Your system login name is:')
    print(login.get_login_name(first, last, idnumber))
    
# Call the main function.
main()
#**************************************************************

# --> Python String Methods <-- 

    # Since strings are immutable, the return on most methods is a copy of the original string, and if you want to keep it
        # it has to be assigned to a new variable.
        # basic methods include 1) testing the values in strings, 2) performing various modifications, 3) searching
            # for substrings and replacing sequences of characters
        # general format stringvariable.method(arguments)

# String Modification Methods

# str.lower()  # converts all of the characters in a string to lower case
ss = "Sammy Shark"
print(ss.lower())
    # output:  sammy shark    # note:  the dot character indicates a method (as compared to a function)
    # a method has to be used in conjunction with a string and incorporates the dot.  They do not exist as independent funcions
    # a stand alone function doesn't have to be associated with a given string.  e.g. len
len(ss)  # is a function, not a method, the argument can be a variety of data types

# str.upper()  Converts to all upper case
ss= " Sammy Shark "
print(ss.upper())  # Output:  SAMMY SHARK
# to keep the changes, must be assigned to a new variable, or overwrite the old string
name = 'picard'
name = name.upper()  # PICARD overwrites picard

# The str.upper() and str.lower() methods make it easier to evaluate and compare strings by making case consistent throughout.

# Removing white space from a string
print(ss.lstrip)  # Returns  Sammy Shark with no spaces on the left side
print(ss.rstrip)    # Returns   Sammy Shark with no spaces on the right
print(ss.strip)     # Returns Sammy Shark with no spaces on the left or right.  It does not remove the center white spaces

# The strip methods can be used to remove characters from the beginning and/or end of a string.
print(ss.lstrip('S'))   # Returnds  ammy Shark

# Searching and Replacing Methods

# Determine if a string begins or ends with a particular character.  Returns boolean True or False
print(ss.startswith('S'))   # Returns True   Note:  .startswith and .endswith are CASE Sensitive
print(ss.endswith('K'))     # Returns False because it ends with a lower case k
print(ss.endswith('ark'))   # Returns True

# .find()  method
# one of the most useful string methods.  Used to find particular substrings
ss.find('Shark')    # returns 7 which is the index of the first occurance of the substring
        # if the substring occurs more than once, only the index of the first occurance is returned
    # matching is done character by character and is case sensitive
    # if the substring is not found, the method returns -1
    # only a string is accepted as an argument, numbers must be '5' put in quotes
phrase = 'The surprise is a surprise that is located in here somewhere'
print(phrase.find('surprise'))  # returns 4   The second occurance, at index 18, is not returned
print(phrase.find('wuolaiht;')) # returns -1
print(phrase.find('SURPRISE'))  # returns -1

# .replace() method.  Finds all occurances of a substring and replaces them with a different string.  
# the original string is not changed (its immutable), unless it is saved as a new variable or overwritten
my_story = "I'm telling you the truth and nothing but the truth"
print(my_story.replace('the truth','lies'))  # Returns  I'm telling you lies and nothing but lies
    # The argument has two parts:  The substring to be found, and the string to replace it
print(my_story)  # Returns I'm telling you the trught and nothing but the truth
my_story = my_story.replace('the truth','lies')
print(my_story)  # Returns   I'm telling you lies and nothing but lies

# String testing Methods  Note:  Returns True only if the string is at least one character in length, in addition to:

# str.isalnum()         # Returns True if the string is all alphanumeric characters (no symbols)
# str.isalpha()         # Returns True if the string is all alphabetic characters (no symbols)
# str.isdigit()         # Returns True if the string contains only numeric digits
# str.islower()         # Returns True if all of the alphabetic letters in the string are in lowercase.
                            # And the string contains at least one alphabetic character
# str.isspace()         # Returns True if the string contains only whitespace characters
# str.isupper()         # Returns True if all the alphabetic letters in the string are in uppercase. 
#                           # And the string contains at least one alphabetic character   
# str.isnumeric()       # Evaluates to True if the string contains only numerals
# str.istitle(),        # Evaluates to True if the string is in Title case

#********************************************************(Gaddis, string_test.py)
# This program demonstrates several string testing methods.

def main():
    # Get a string from the user.
    user_string = input('Enter a string: ')

    print('This is what I found about that string:')
    
    # Test the string.
    if user_string.isalnum():
        print('The string is alphanumeric.')
    if user_string.isdigit():
        print('The string contains only digits.')
    if user_string.isalpha():
        print('The string contains only alphabetic characters.')
    if user_string.isspace():
        print('The string contains only whitespace characters.')
    if user_string.islower():
        print('The letters in the string are all lowercase.')
    if user_string.isupper():
        print('The letters in the string are all uppercase.')

# Call the main function.
main();

#*****************************************************************(Gaddis, validate_password.py)
# This program gets a password from the user and
# validates it.

import login

def main():
    # Get a password from the user.
    password = input('Enter your password: ')

    # Validate the password.
    while not login.valid_password(password):
        print('That password is not valid.')
        password = input('Enter your password: ')

    print('That is a valid password.')

# Call the main function.
main()
#**********************************************************************

# String Splitting  returns a list containing the words in the string
    # str.split()         uses spaces as separators

#***************************************************************(Gaddis, string_split.py)
# This program demonstrates the split method.

def main():
   # Create a string with multiple words.
   my_string = 'One two three four'

   # Split the string.
   word_list = my_string.split()

   # Print the list of words.
   print(word_list)

# Call the main function.
main()   # returns:  ['One', 'two', 'three', 'four']
#**********************************************************************
#****************************************************************(Gaddis, split_date.py)
# This program calls the split method, using the
# '/' character as a separator.

def main():
    # Create a string with a date.
    date_string = '11/26/2012'

    # Split the date.
    date_list = date_string.split('/')

    # Display each piece of the date.
    print('Month:', date_list[0])
    print('Day:', date_list[1])
    print('Year:', date_list[2])

# Call the main function.
main()
#*************************************************************************

    # str.capitalize(), 
    # str.casefold(), 
    # str.center(), 
    # count(), 
    # encode(), 
    # expandtabs(), 
# format(), 
# format_map()
# index(), 
#
# isascii(), 
# isdecimal(), 

# isidentifier(), 


# isprintable(), 



# join(), 
# ljust()




# maketrans(), 
# partition(), 
# rfind(), 
# rindex(), 
# rjust(), 
# rpartition()
# rsplit(),  
# plit(), 
# plitlines(), 
# startswith(), 
# trip(), 
# wapcase(), 
# title(), 
# ranslate()



# zfill().




# Python has some string methods that will evaluate to a Boolean value.  These methods are useful when we are creating forms for users to fill in,
# for example, if we are asking for a post code we will only want to accept a numeric string, but when we are asking for a name, we will only want
# to accept an alphabetic string.

# References:
#
# Amos, D., Bader, D., Jablonski, J., Heisler, F. (2022). Python Basics:  A Practical Introduction to Python 3. (4th ed.).
#       USA: Real Python.  www.realpython.com.

# Gaddis, T. (2018). Starting out with Python.  Chapter 8:  More About Strings (4th Ed) New York, NY: Pearson Educational.  pp 407-431
#
# Geeksforgeeks.com (2022, 16 Feb). Python Programming Language.
#   https://www.geeksforgeeks.org/python-programming-language/ 
#
# Myers, M. (2017).  A Smarter Way to Learn Python. Monee, IL: Mike Myers
#   Reference http://www.asmarterwaytolearn.com
#
# Python.org (2022). What is Python?: Executive Summary. 
#   https://www.python.org/doc/essays/blurb/
#
# Python.org(2022). Built in Functions.
#   https://docs.python.org/3/library/functions.html    
#
# Ramos, L.P. (2021, 25 Jan). How to Use Python: Your First Steps. From RealPython.com
#   https://realpython.com/python-first-steps/
#
# Severance, C.R. (2009). Python for Everybody: Exploring Data Using Python 3. Creative Commons.  
#   Available for download at www.py4e.com.
#
# Tagliaferri, L. (2018).  How to Code in Python.  New York, NY: Digital Ocean.  
#   download:  https://assets.digitalocean.com/books/python/how-to-code-in-python.pdf
#
# w3schools.com (2022, 16 June). Python Tutorial. https://www.w3schools.com/python/default.asp
