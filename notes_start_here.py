# Tamara Lynch Study Notes
# Last Update:  10/29/2022

'''***---> General Background and Program Info <---***'''
# 
# Python is a programming language developed in 1991 by Guido Van Rossum and whose namesake is Monty Python's Flying Circus
    # Guido was the BDFL (Benevolent Dictator For Life) until 2018, now the language is maintained by the python software foundation (Python.org)

#   Python is an interpreted, object-oriented (and scripted), high-level programming language with dynamic semantics. 
        # Interpreted - requires an interpreter (large program) installed on the using computer to convert the code to machine language
            # This differes from a compiler, in that it interprets line by line while the code is executed.  Slower than C++. etc
            # REPL - Read Evaluate Print Loop - the actions that occur when using Python in an interactive environnment (e.g. Windows command 
            #   prompt, or the interactive window in IDLE).  Often used to refer in general to any interactive coding shell (vs. scripted coding)
            #   IDLE is the environment that comes with the Python interpreter.
            # online REPLs can be used to avoid downloading the Python interpreter:  e.g. https://replit.com/languages/python3
            #   https://www.pythonanywhere.com/  https://www.python.org/shell/  http://pythonfiddle.com/  https://trinket.io/
            # Scripted - programs can be written ahead, stored in a text file, and run from the file.  File format must be .py 
        # Object-oriented - Python has different "classes" or categories of objects, they are used to build and classify different objects.
        #    Almost everything in Python is an "object" which consist of specific data and code.  Each "object" has its own properties 
        #       and methods.  e.g. "Strings" are "objects" and have their own string methods and properties.
        # High Level - programming languages that are closer to human speech.  Python is popular because it is so "user-friendly"
        # Dynamic Semantics - This means that the variable Type can change over the life of the program, it can be changed
            # in the middle of a program (like from string to integer if it contains numbers, or from one value to another)

# Algorithms: a step by step list of instructions that if followed exactly will solve the problem under consideration.
        # i.e. an answer for a problem

        # Algorithm in English for calculating the area of a circle.
            # Ask for radius
            # Compute area by squaring radius and multiplying the result by pi
            # Display the computed area
        # Algorithm - same thing in pseudocode (closer to a generic programming language)
            # Ask for radius
            # let area = (radius^2) × π
            # Display area
        # Algoritm writtenf in Python
            # radius = int(input("Enter the radius:"))
            # area = (radius * radius) * 3.1415
            # print("The area of a circle with radius", radius, "is:", area)

# Program:  an algorithm expressed in programming language,  an implementation of an algorithm

# Program Elements:  
#   1) input - Get data from the keyboard, a file, or some other device.
#   2) output - Display data on the screen or send data to a file or other device.
#   3) math and logic - Perform basic mathematical operations like addition and multiplication and logical operations like and, or, not.
#   4) conditional execution - Check for certain conditions and execute the appropriate sequence of statements.
#   5) repetition - Perform some action repeatedly, usually with some variation.
#
# Control Structures:
# 
# as a program executes, the interpreter always keeps track of which statement is about to be executed. 
#   We call this the control flow, or the flow of execution of the program. When humans execute programs, 
#   they often use their finger to point to each statement in turn. So you could think of control flow as “Python’s moving finger”. (U of M 7.3)

#   All programs have three basic control structures:  
#       1) sequence - instructions execute consecutively (script)
#       2) iteration - with (for) or without (while) definate stopping points.  For repetition
#       3) conditionals - decision making structures, uses Boolean logic.
# 
# Syntax:
#   formal language: has a strict syntax rules 
#       Syntax definition: the arrangement of words and phrases to create well-formed sentences in a language
#       programming syntax is strict and unambiguous.  It involves 1) tokens (smalles units of code) 2) structure (e.g. use of colons, etc)
#
#       Parsing - is looking at the syntax to determine the semantics (meaning)
#           Natural language - is redundent, ambiguous, full of idiom and metaphor
#               Poetry - uses the word sounds as well as the meanings - very difficult to analyze
#               Prose - words are more literal and structure is used to provide meaning - a little easier to analyze
#           Formal language - is literal, unambiguous, tokens have a precise single definition and use

'''***---> Scripting <---***'''

# One of the three major control structures
#   (Repetition and Conditional control structures are addressed in their own note set)

# Script:  A series of statements 
    # a scripted program is a series of statements saved as a text file that can be executed by the Python interpreter
    # Scripts are written in an editor - such as IDLE or VS Code
    # Use white space to 'chunk' the code for readability
    # must be saved as a python file using the extension  .py

# Statement:  a unit of code that the Python interpreter can execute.  They represent an action or command (e.g. print statement,
#   assignment statements)
#   Statement elements include data types (constants and variables), reserved words, operators, functions, and objects
#   All statements and structures in a program are built with tokens (smallest unit of code)
#   Some kinds of statements that you’ll see: assignment statements, while statements, for statements, if statements, and import statements. 
#       (There are other kinds too!)

# Expression:  a type of statement, or part of a statement, that evaluates and produces a return
    # Python Basics (U of M) - expressions compute and have a 'value' placed in the working memory.  Expressions can be
    # literal, meaning they have the same value in the RAM as in the program
# 3.13 is considered a literal expression with the value 3.13
# 1 + 2 is an expression with the value of 3.  The computing occurs 'behind the scenes' in the interpretor

# 'Hard Coding': When you write an expression that refers to values instead of variable names - cannot be updated

# Value: The computed result of an expression.  Has a type (e.g. integer, float, etc).  The value of a literal is the same in the RAM as in the code.   

'''---> Character Sets <---'''

# A set of valid characters accepted by a programming language.  Python accepts:

# Alphabets:  All A to Z capital letters and a to z lower case letters
# Digits:  All digits 0 to 9
# Special Symbols:   ” ‘ l ; : ! ~ @ # $ % ^ ` & * ( ) _ + – = { } [ ] \ .
# White Spaces
# All ASCII and Unicode symbols

'''---> Tokens <---'''

# A token is the smallest individual unit in a program.

# Python tokens include:  
#   Keywords - or reserved words 
#   Identifier - the names given to any variable, function, class, list, method, etc. for their identification
#   Literals - (aka Constants) the fixed values or data items used in a source code. 
#   Punctuators - These are the symbols that used in Python to organize the structures, statements, and expressions. 
#       Some of the Punctuators are: [ ] { } ( ) @  -=  +=  *=  //=  **==  = , etc.
#   Operators - These are the tokens responsible to perform an operation in an expression. (+ - * / // % or not, etc)
#       
'''---> Reserved Words <---'''

# aka Key Words.  One of the five Python tokens

# reserved words:  and (a logical operator), as (to create an alias), assert (for debugging), break (to break out of a loop), 
#   class (to define a class), continue (to continue to the next iteration of a loop), def (to define a function), del (to delete an object), 
#   else (used in conditional statements), elif (used in conditiona statements, same as else if), 
#   except (used with exceptions, what to do when an exception occurs), False ( Boolean value, result of comparrison operations), 
#   finally (used with exceptions, what to do when an exception occurs), from (to import specific parts of a module), for (to create a loop), 
#   global (to declare a global variable), if (to make a conditional statement), import (to import a module), 
#   in (to check if a value is present in a list, tuple, etc.), is (to test if two variables are equal)
#   lambda (to create an anonymous function), not (a logical operator), nonlocal (to declare a non-local variable), 
#   None (represents the null value), or (a logical operator), pass (a null statement, a statement that will do nothing), 
#   raise (to raise an exception) return (to exit a funtion and return a value)
#   True (boolean value, result of comparison operations), try (to make a try...except statement) 
#   while (to create a while loop) with (use to simplify exception handling)
#   yield (to end a function, returns a generator)

# to get a list of keywords in interactive
help('keywords')

''' ---> Constants <---'''

# Constants:  
#   A "literal" meaning written into the pyton code.  
#   Or a "special" variable assigned at the beginning of the program.  Use all capital letters in the names for variables that will be used as
#       a constant in the program


NUMBER_5 = 5  # is an example of assigning a constant

'''---> Comments <---'''

# Comments:  begin with a hashtag, by convention, start a new line after 72 characters.
#       They can be "in-line" putting # comment next to a statement - keep these minimal and add at least 2 spaces before the #
#       Block comments: comments that start on a new line (such as these) are preferable
#       Using tabbed spaces before lines in a block constant (like I am doing) is not preferable.

# Use comments sparingly and don't explain code whose meaning is apparent (explicit)
#   
# Sections of code can be "commented out" temporarily so that they don't run when the 
#   code is executed.  
#   Shortcut:  highlight the code - in Windows ctrl + / to toggle hash tags  (**** Very Useful!)

# Comments should be written with a single space after the hashtag

# Smelly Comments- Code smells is a term used to indicate any red flags in your codebase. 
#   These red flags or flaws are usually related to the readability, maintainability and scalability issues. 
#   Good code should not need comments to give in depth explanations.
 
# D.R.Y. Comments - don't repeat yourself
# W.E.T. Comments - wrote everything twice (wasted everyone's time)
# Do not use rude comments, even if joking around in team development.

'''---> Variable <---'''

# Variables:  Spots in memory allocated to store some data.  Produced using the assignment statement.
    # The assignment operator takes the value to the right, and assigns it to the name on the left.
    # Both objects and values can be assigned to a variable

variable1 = 1  #  Think of the equal sign as an arrow pointing to the variable name.  1 is the data placed in that spot.

# The = sign does NOT mean 'Equal' everything to the right of the equal sign happens first, then it is stored in that spot ("dynamic").  
#   Expressions on the right CAN contain the variable
# variables can be re-assigned later in the code, and the old value gets wiped out
# the variable can be used in an expression on the right and the new value of this expression is
#    re-assigned to itself - called updating the variable (the new value of the variable depends on the old)
#    this can be simplified using special asignment oprators (e.g. +=) or by using repetition structures
x = 1    # variable has to be initialized before it can be updated
x = x + 3
x += 1
x -= 1

# incrementing means adding to a variable, usually by one.  'bumping' means incrementing by one
# decrementing means subtracting from a variable (usually by one)

variable1 = 2  # now the variable1 spot holds the number 2 instead of 1.  The unused value 2 is removed via "garbage collection" by the interpreter

# variable naming conventions:  Variable names can contain _underslashes, numbers, and letters
    # They are case sensitive and you cannot start with a number.
    # Starting a variable with an underscore_ usually has a special meaning - beginners should avoid this
    # Python treats the underscore character_ as a letter character, so it can be used to indicate spaces in a variable name
    # By convention, start with a lowercase letter, then camelcase or underscore
    # Menomic - use names that make sense to the users of the program (back end programmers keep it short to avoid stack overflow)
        # Three to Four word maximum
    # Recommended not to use the same word with different cases or to start with a capital letter
    # Note: The lower_case_with_underscores naming convention, also known as snake_case, 
    #   is commonly used in Python. It isn’t enforced, but it’s a widely adopted standard.  (found in PEP 8, the official "style guide")
        # PEP is Python Enhancement Proposals maintained by python.org
# Python now offers full Unicode support, so you can also use Unicode characters in your variable names like π.

# Only global variables and named constants should be capitalized. 
#   Ideally, all other variables should be placed in a local function.  (so as not to 'pollute' the global name space)

'''---> Operators <---'''

# Operators: These are the tokens responsible to perform an operation in an expression. 
# The variables on which operation is applied are called operands. 
# Operators can be unary or binary. Unary operators are the ones acting on a single operand e.g. not operator, complement operator, etc. 
# Binary operators need two operands to operate.  (Geeksforgeeks.com, Feb 7)
 
# Operators:  The main types of operators are arithmetic, relational, assigment, logical, membership, identity, and bitwise
         # operators may do different things depending on the data type of the variables fed in. e.g. + concatenates strings, adds integers, 
         # OR combines sequences such as lists
#   Arithmetic operators include:  addition +, subtraction -, multiplication *, division /, exponentiation **, floor division //, and modulus %
#       These are done in PEMDAS order.          
        # + concantenates two strings and does not add spaces
#   Relational operators include: >, <, =, >=, <=, or != (not equal)  These are evaluated as True or False  
#   Assignment operators include:  =, += (increment), -= (decrement), /=, *=, %=, **=, //=, and the new Walrus operator :=
#   Logical operators include:  and, or, not (these are all reserved words).  They return the boolean True or False
#   Membership operators include: in, not in. They return the boolean True or False
#   Identity operators include:  is, not is.  They return the boolean True or False
#   Bitwise operators include: & (Binary AND), | (Binary OR), ^ (Binary XOR), ~ (Binary One's Comlement)
#   <<(Binary Left Shift), >> (Binary Right Shift)
#
# --> Augmented Assignment Operators <--

#  Used to simplify common statements in a program
#
x = 0
index = 0
balance = 1000
withdrawal = 100

x += 5  # is equivalent to x = x + 5
index += 1   # example that increases an index (within iterables, etc)

x -= 5  # is equivalent to x = x - 5
balance -= withdrawal    # example where a withdrawal is subtracted from the balance

x *= 5  # is equivalent to x = x * 5
x /= 5  # is equivalent to x = x / 5
x %= 5  # is equivalent to x = x % 5
#  -+, /=, *=, %=, **=, //=, and the new Walrus operator :=  (because of the 'eyes and tusks')
#  := (only available in python 3.8 or newer) an assignment statement that can be used in the middle of an expression
words = []

while (word := input("Enter word: ")) != "quit":   # the walrus operator is used to assign input to the variable 'word' 
    words.append(word)                                # in the middle of the expression

print(words)


'''---> Data Types <---'''

# the primary Data Types:  text, numeric, sequence, mapping, set, boolean, binary, none type.  The data type is set when you assign a value to the variable
#   strings are considered one of the "fundamental", or "primative" data types in Python, along with boolean, float, and int
#   other data types are known as compound data types, aka data structures, aka abstract data types

type() # a function that tells the class (data type) of a value
print(type("Hello, World!"))    # Returns <class 'str'>
print(type(17))                 # Returns <class 'int'>  
print(type(3.2))                # Returns <class 'float'>

    # Numeric data types:  integer aka int, float, complex
x = 5       # int
x = 20.5    # float
x = 1j      # complex

    # Sequence data types:  list, tuple, range
x = ["apple", "banana", "cherry"]   #list
x = ("apple", "banana", "cherry")   #tuple
x = range(6)  # range

    # Mapping data type: dictionary aka dict
x = {"name" : "John", "age" : 36}   # dict

    # Set data types:  set, frozenset
x = {"apple", "banana", "cherry"}   # set
# x = frozenset(iterable_object_name)  # frozenset accepts an iterable as its argument

    # Boolean data type:  boolean aka bool
x = True                            # bool
x = False                           # bool

    # Binary data types:  bytes, bytearray, memoryview
x = b"Hello"                        # bytes
x = bytearray(5)                    # bytearray
x = memoryview(bytes(5))            # memoryview

    # None data type:  NoneType
x = None                            # NoneType

type(variable1) # type() function to get back the data type

# Built in Types - the standard types in the interpreter accoring to python.org:  numerics, sequences, mappings, classes, instances, and exceptions
#       Truth value testing, Boolean Operations, Comparisons
# Exceptions when raised, produce an object that is the 'exception' data type
# an Instance - is an object of a class that has its own set of data attributes
#   for example, a named turtle is an instnce of the 'turtle' class.  
import turtle
alex = turtle.Turtle()  # is one instance that can have its own attributes, e.g. alex is red
trent = turtle.Turtle() # creates another turtle instance that can have its own attributes, e.g. trent is blue
# >>> type(alex)
# <class 'turtle.Turtle'>

'''---> Functions <---'''

# Function:  code that performs some task and can be invoked by name.  The parantheses "call" the function
# Built In Functions:  These are always available in the python interpreter and can be used
#   without needing an import statement.
#   Argument:  what is placed within the parantheses - differs for each type of function and most have default settings
    #  this is the input that gets sent to the function

# abs()           # returns the absolute value of a number
# any()           # returns True if any items in an iterable object are true
# all()           # returns True if all item in an iterable object is true
# anext()         # when "awaited" returns the next item from the given asynchronous iterator
# aiter()         # returns an asynchronous iterator for an asynchronous iterable
# ascii()         # returns a string containing a printable/readable version of an object
# bytes()         # returns a bytes object
# bytearray()     # returns an array of bytes
# bool()          # returns the boolean value of a specified object
# breakpoint()    # drops you into a debugger at a call site
# bin()           # returns the binary version of a number
# chr()           # returns a character from the specifid Unicode code
# classmethod()   # converts a method into a class method
# complex()       # returns a complex number
# compile()       # returns the specified source as an object, ready to be executed
# callable()      # returns True if the specified object is callable
# dict()          # returns a dictionary (array)
# dir()           # returns a list of the specifiec object's properties and methods
# delattr()       # deletes the specified attribute (property or method) from the specified object
# divmod()        # returns the quotiont and the remainder when argument 1 is divided by argument 2
# enumerator()    # takes a collection (e.g. tuple) and returns it as an enumerate object
# eval()          # evaluates and executes an expression
# exec()          # executes the specified code or object
# filter()        # use a filter function to exclude items in an iterable object
# float()         # returns a floating point number
# format()        # formats a specified value
# frozenset()     # returns a frozenset object
# getattr()       # returns the value of a specified attribute (property or method)
# globals()       # returns the current global symbol table as a dictionary
# hasattr()       # returns True if the specified object has the specified attribute (property or method)
# hash()          # returns the hash value of a sepcified object
# help()          # executes teh built-in help system
# hex()           # converts a number into a hexadecimal value
# id()            # returns the id of an object
# input()         # allowing user input
# int()           # returns an integer number
# isinstance()    # returns True if a specified object is an instance of a specified object
# issubclass()    # returns True if a specified class is a subclass of a specified object
# iter()          # returns an iterator object
# len()           # returns the length of an object
# list()          # returns a list
# locals()        # returns an updated dictionary of the current local symbol table
# map()           # returns the specified iterator with the specified function applied to each item
# max()           # returns the largest item in an iterable
# memoryview()    # returns a memory view object
# min()           # retuns the smallest item in an iterable
# next()          # returns the next item in an iterable
# object()        # returns a new object
# oct()           # converts a number into an octal
# open()          # opens a file and returns a file object
# ord()           # convert an integer representing the Unicode of the specified character
# pow()           # returns the value of x to the power of y
# print()         # prints to the standard output device, typically the screen
# property()      # gets, sets, deletes a property
# range()         # returns a sequence of numbers, starting from 0 and increments by 1 (by default)
# repr()          # returns a readable version of an object
# reversed()      # returns a reversed iterator
# round()         # rounds a number
# set()           # returns a new set object
# setattr()       # sets an attribute (property/method) of an object
# slice()         # returns a slice object
# sorted()        # returns a sorted list
# staticmethod()  # converts a method into a static method
# str()           # returns a string object
# sum()           # sums the items of an iterator
# super()         # returns an object that represents the parent class
# tuple()         # returns a tuple
# type()          # returns the type of an object
# vars()          # returns the _dict_property of an object
# zip()           # returns an iterator, from two or more iterators   


'''---> Objects <---'''

# Object-oriented - Python has different "classes" or categories of objects, they are used to build and classify different objects.
        #    Almost everything in Python is an "object" which consist of specific data and code.  Each "object" has its own properties 
        #       and methods.  e.g. "Strings" are "objects" and have their own string methods and properties.

# Objects:  strings, list/arrays, dictionary, tuples, sets, files, modules (random, statistics, math, cmath...turtle, etc)

'''---> Methods <---'''

# methods are object specific functions, they only work with that particular object and use dot notation.

# Python String Methods: capitalize(), casefold(), center(), count(), encode(), endswith(), expandtabs(), find(), format(), format_map()
#       index(), isalnum(), isalpha(), isascii(), isdecimal(), isdigit(), isidentifier(), islower(), isnumeric(), isprintable(), isspace()
#       istitle(), isupper(), join(), ljust(), lower(), lstrip(), maketrans(), partition(), replace(), rfind(), rindex(), rjust(), rpartition()
#       rsplit(), rstrip(), split(), splitlines(), startswith(), strip(), swapcase(), title(), translate(), upper(), zfill().

# Python List/Array Methods:  append(), clear(), copy(), count(), extend(), index(), insert(), pop(), remove(), reverse(), sort()

# Python Dictionary Methods:  clear(), copy(), fromkeys(), get(), items(), keys(), pop(), popitem(), setdefault(), update(), values()

# Python Tuple Methods:  count(), index()

# Python Set Methods:  add(), clear(), copy(), difference(), difference_update(), discard(), intersection(), intersection_update(), isdisjoint()
#       issubset(), issuperset(), pop(), remove(), symmetric_difference(), symmetric_difference_update(), union(), update()

# Python File Methods:  close(), detach(), filno(), flush(), isatty(), read(), readable(), readline(), readlines(), seek(), seekable(), tell()
#       truncate(), writable(), whitelines()

''' --> Modules <-- '''

# Module: a file of Python code, usually defining one or more related new types of 'things' (classes)

# Python has a set of modules that are downloaded with the interpreter and are available for import - part of the 'standard library'
    # Modules are located in a unique 'namespace'.  Methods can have the same name as other modules but names cannot be repeated within a module.

# Global standard library module index at:  https://docs.python.org/3.6/py-modindex.html

# import.module_name is the statement used to open the module to the Python program.  The Module's name is used and is case sensitive.
# Caution!  do not name files using standard module names - it can overwrite the standard python library

# ways to import a module:
import turtle   #  using this type of import, all of the turtle methods must be prefaced with turtle dot (e.g. turtle.method)
# t = turtle.Turtle()  # this is a shortcut method, by assigning turtle to a variable, you can now use t instead of turtle for all of the methods
    # e.g. t.right(90)

from turtle import* # this allows the methods to be used without a preface.  This can get confusing if there is more than
    # one module open in a single program.


# Python Random Module - used to make random numbers.  Methods:  seed(), getstate(), setstate(), getrandbits(), randrange(), randint(), choice(), choices()
#       shuffle(), sample(), random(), uniform(), triangular(), betavariate(), expovariate(), gammavariate(), gauss(), lognormvariate()
#       mormalvariate(),vonmisesvariate(), paretovariate(), weibullvariate()

# Python Requests Module - make a request to a web page and print the response.  Methods: del(), get(), head(), patch(), post(), put(), request()

# Python Numbers Module - numbers.complex(), abstract method conjugate(), numbers.real(), numbers.rational(), numbers.integral()

# Python Statistics Module - built in module that you can use to calculate math statistics of numerical data.  Methods:   statistics.harmonic_mean()
#       statistics.mean(), statistics. median(), statistics.median_grouped(), statistics.median_high(), statistics.median_low(), statistics.mode()
#       statistics.pstdev(), statistics.stddev(), statistics.pvariance(), statistics.variance()

# Python Math Module - built in module used for mathmatical tasks.  Methods:  math.acos(), math.acosh(), math.asin(), math.asinh(), math.atan()
#       math.atanh(), math.cell(), math.comb(), math.copysign(), math.cos(), math.cosh(), math.degrees90, math.dist(), math.erf(), math.erfc()
#       math.exp(), math.expm1(), math.fabs(), math.factorial(), math.floor(), math.fmod(), math frexp(), math.fsum(), math.gamma(), math.gcd()
#       math.hypot(), math.isclose(), math.isfinite(), math.isinf(), math.isnan(), math.isqrt(), mth.ldxp(), math.lgamma(), math.log(), math.log10()
#       math.log1p(), math.log2(), math.perm(), math.pow(), math.prod(), math.radians(), math.remainder(), math.sin(), math.sinh() math.sqrt(), math.tan(), math.tanh()
#       math.trunc()
#       
#       Math Constants:  math.e (euler's number 2.7182...),  math.inf (returns a floating-point positive infinity), math.nan (returns a floating point NaN not a number value)
#                       math.pi (returns pi 3.1415...), math.tau (returns tau 6.2831...)

# Python cMath Module - built in module for working with complex numbers. Methods:  cmath.acos(x), cmath.acosh(x), cmath.asin(x), cmath.asinh(x), cmath.atan(x)
#       cmath.atanh(x), cmath.cos(x), cmath.cosh(x), cmath.exp(x), cmath.isclose(x), cmath.isfinite(x), cmath.isinf(x), cmath.isnan(x), cmath.log(x[base]), cmath.log10(x)
#       cmath.phase(), cmath.polar(), cmath.rect(), cmath.sin(x),cmath.sinh(), cmath.sqrt(x), cmath.tan(x), cmath.tanh(x)
#       math.trunc()
#
#       cMath Constants:  cmath.e (euler's number 2.7182...),  cmath.inf (returns a floating-point positive infinity), cmath.infj (returns a complex infinity value)
#           cmath.nan (returns a floating point NaN not a number value), cmath.nanj(returns a comlex NaN value), cmath.pi (returns pi 3.1415...), cmath.tau (returns tau 6.2831...)

'''---> Exceptions <---'''

# One of three types of bugs found in code (1. syntax errors, 2. exceptions, 3. logic errors)
# Exceptions occur (are 'raised') during the execution of the program.
# An exception raised creates an 'exception object' and stops the program flow

# Exceptions:  
#   ArithmeticError (raised when an error occurs in mumeric calculation)
#   AssertionError (raised when an assert statement fails)
#   AttributeError (raised when attribute refernce or assignment fails)
#   Exception (base class for all exceptions)
#   EOFError (raised when the input() method hits an "end of filer" condition (EOF))
#   FloatingPointError (raised when a floating point calculation fails)
#   GeneratorExit (raised when a generator is closed (with the close() method)
#   ImportError (raised when an imported module does not exist)
#   IndentationError (raised when indentation is not correct)
#   IndexError (raised when an index of a swquence does not exist)
#   KeyError (raised when a key does not exist in a dictionary)
#   KeyboardInterrupt (raised when the user presses Ctrl+c, Crtrl+z, or Delete)
#   LookupError (raised when errors raised cannot be found)
#   MemoryError (raised when a program runs out of memory)
#   NameError (raised when a variable does not exist)
#   NotImplementedError (raised when an abstract method requires an inherited class to overide this method)
#   OSError (raised when a sysrtem related operation causes an error)
#   OverflowError (raised when the result of a numeric calculation is too large)
#   ReferenceError (raised when a weak reference object does not exist)
#   RuntimeError (raised when an error occurs that do not belong to any specific exceptions)  ** Main Type**
#   StopIteration   (raised when the next() method of an iterator has no further values)
#   SyntaxError (raised when a syntax error occurs)  *** Main Type ***
#   TabError (raised when indentation consists of tabs or spaces)
#   SystemError (raised when the sys.exit() function is called)   
#   TypeError (raised whn two different types are combined)
#   UnboundLocalError (raised when a local variable is referenced before assignment)
#   UnicodeError (raised when a unicode problem occurs)
#   UnicodeEncodeError (raised when a unicode encoding problem occurs)
#   UnicodeDecodeError (raised when a unicode decoding problem occurs)  
#   UnicodeTranslateError (raised when a unicode translation problem occurs)
#   ValueError (raised when there is a wrong value in a specified data type)
#   ZeroDivisionError (raised when the second operator in a division is zero)

# Python will stop executing and give a "Traceback" 
    # Tracebacks are best read from the bottom up.  The last line gives the error, 
    #   the second to the last line gives the code that produced the error
    #   the third to the last line gives the file name and line number

'''---> References:<---'''
#
# Amos, D., Bader, D., Jablonski, J., Heisler, F. (2022). Python Basics:  A Practical Introduction to Python 3. (4th ed.).
#       USA: Real Python.  www.realpython.com.

# Gaddis, T. (2018). Starting out with Python (4th Ed) New York, NY: Pearson Educational.  pp 1-74
#
# Geeksforgeeks.com (2022, 16 Feb). Python Programming Language.
#   https://www.geeksforgeeks.org/python-programming-language/ 

# Geeksforgeeks.com (2022, 07 Feb). Python Tokens and Character Sets.
#   https://www.geeksforgeeks.org/python-tokens-and-character-sets/
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
#   https://www.py4e.com/book
#
# Tagliaferri, L. (2018).  How to Code in Python.  New York, NY: Digital Ocean.  
#   download:  https://assets.digitalocean.com/books/python/how-to-code-in-python.pdf
#
# University of Michigan (2017). Python Basics. Foundations of 
#   Python Programming. [Digital Textbook copyright 2017 bradleymiller]. Coursera.
#
# w3schools.com (2022, 16 June). Python Tutorial. https://www.w3schools.com/python/default.asp
#
# Zhane, J. (2018, 05 Nov). Writing Comments in Python (Guide). From RealPython.com.
#   https://realpython.com/python-comments-guide/ 
