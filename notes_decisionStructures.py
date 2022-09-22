# --> Conditionsals <-- aka Decisions structures:  A type of Python control Structure

# Control Structure (i.e. constructs): a.k.a. control flow or flow control: a logical design that controls the order in which 
# a set of statemtns execute.
#   Python has different control structures:  including Sequenc Structures(normal script), Selection Structures(decision), 
#       and Repitition Structures(loops)

#   Sequence Structure:  A set of statements that execute in the order which they appear.

#   Selection Structure (i.e. Decision Structure or Branching structure):  Decision making using Boolean Logic
    # Actions are conditionally executed.  The related code only runs if the conditional is True

#   Repetition:  (iteration) Loops

# --> Boolean Expressions and Relational Operators <--

    # Boolean expressions are tested to be either True (1) or False (0)
            # George Boole created a system of math to use the abstract concept of True or False in computations
    # Relational operators are used in Boolean expressions to determine if a reltionship exists between two specific values
    #   > Greater Than
    #   < Less Than
    #   >= Greater Than or Equal To
    #   <= Less Than or Equal To
    #   == Equal To
    #   != Not Equal To

x = 5
y = 8
print("x == y:", x == y)    # returns False
print("x != y:", x != y)    # returns True  
print("x < y:", x < y)      # returns True
print("x > y:", x > y)      # returns False
print("x <= y:", x <= y)    # returns True
print("x >= y:", x >= y)    # returns False

    #  bool is a fundamental data type in Python, short for Boolean and tests True or False (Amos et. al p. 187)
    # >>> type(True)
        # <class 'bool'>

    # >>> type(False)
        # <class 'bool'>

# Boolean Variables:  can reference one of two values:  True or False. (bool data types)
    # Commonly used as flags, which indicate whether specific conditions exist.
    # flag: a variable that signals when some condition exists in a program
        # If the flag is set to False, the condition does not exist
        # If the flag is set to True, the condition exists  (Gaddis ppt)

sales = float(input('Please enter the amount you sold this year.  Do not include dollar signs or commas'))
if sales >= 50000.00:
    sales_quota_met = True
if sales < 50000.00
    sales_quota_met = False

# Any object can be tested for Truth.  Most are True by default except:  (e.g. any integer, like 17, will return True if tested)
        # constants defined to be false: None and False.
        # zero of any numeric type: 0, 0.0, 0j, Decimal(0), Fraction(0, 1)
        # empty sequences and collections: '', (), [], {}, set(), range(0)

# Do not compare values to bools, most objects are by default True and you may get unexpected returns
name = 'sammy'
name == True    # returns True


# --> Logical Operators <--

#  The and  or  logical operators allow boolean expressions to be combined into compound expressions

    # and   : connects two Boolean expressions into one compound expression.  
            #   Both subexpressions must be true for the compound expression to be True
            #  T and T returns True, T and F, F and T, F and F all return False

    # or    : connects two Boolean expressions into one compound expression.
            # One or the other subexpression must be true for the compound expression to be True
            # T or T, T or F, F or T all return True.  F or F returns False

    # not   : reverses the truth of a boolean expression
            # returns True only if the expression is False.  
            # 'unary' operator, meaning it only works with one operand.  The operand must be a Boolean expression.
            # The operator (not) reverses the truth of its operand (boolean expression).  
            # If it is applied to an expression that is True, it returns False
            # If it is applied to an expression that is False, it returns True.
    
    # and or  operators both "short circuit" after the first expression (if it tests False for and ), (if it tests True for or)
        # read left to right

print((9 > 7) and (2 < 4)) # Both original expressions are True     returns True
print((8 == 8) or (6 != 6)) # One original expression is True       returns True
print(not(3 <= 1)) # The original expression is False               returns True

print((-0.2 > 1.4) and (0.8 < 3.1)) # One original expression is False      returns False
print((7.5 == 8.9) or (9.2 != 9.2)) # Both original expressions are False   returns False
print(not(-5.7 <= 0.3)) # The original expression is True                   returns False

# An example of a compound satement with multiple expressions using  and, or, and not:

not((-0.2 > 1.4) and ((0.8 < 3.1) or (0.1 == 0.1)))    # returns True
# Python does accept   0 < 10 < 20 (compound inequalities)

# F or T returns True,  F and T returns False,  not F returns True

# *** Relational and Logical Operators have an order of precedence:
#  (), <, <=, ==, >=, > not and or

True and False == True and False  # Returns False, because the == has a higher precedence then and
    # Python interprets this as True and (False == True) and False
    # you can use parantheses to avoid this

# Testing a variable to see if it is within a range of numbers:  use logical operators
x = 5
if x >= 20 and x <= 40:
    print('The value is in the exceptable range')
if x < 20 or x > 40:
    print('The value is outside the acceptable range')

# --> Decision Structures <--
#   On the flow chart, True/False statements are prepresented by a diamond
#   Futher actions are conditionally executed base on the boolean result
#   Decision structures can test strings.  Letter characters are compared by their ASCII code, z>a
#   If one string is shorter than the other, only the corresponding characters will be compared, but the shorter string
#       is considered < the longer string.

# Types of Decision Structures: if, if-else, if-elif-else

# --> if <-- 
#   Single Alternative (branch) decision structure:  Uses only an if statement and offers only one alternative path of execution, only executes if True
#   The body must have at least one statement, but can have multiple.  The reserved word 'pass' can be used to skip the block.
#   This is the simpilest form of a decision structure (conditional statement)
x = -5
if x < 0:
    pass   # need to handle negative numbers

grade = 95                          # (Amos et.al, pp 199-200)
if grade >= 70:
    print("You passed the class!")
print("Thank you for attending.")  # Returns:  You passed the class!   Thank you for attending.

grade = 40
if grade >= 70:
    print("You passed the class!")
print("Thank you for attending.")   # Returns:  Thank you for attending.  This executes as a normal sequence script
    # since it is outside the block of code that goes with the if compound statement.

# You can stack if statements:
grade = 40
if grade >= 70:
    print("You passed the class!")
if grade < 70:  
    print("You did not pass the class :(")
print("Thank you for attending")  # Returns:  You did not pass the class :(    Thank you for attending.

# Stacked if statements can return multiple Trues.  Python doesn't quit after the first True statement.
variable = 5
if variable > 1:
    print('This is True')
if variable == 5:
    print('This is True')
if variable <10:
    print('This is True')

# If statements can also be nested, but execution stops where there is a False
if variable > 1:
    print('This is True')
    if variable == 5:
        print('This is True')
        if variable <10:
            print('This is True')
print('All three were true, so the entire nest executed')

# Decision structures are considered a compound statement 
# A compound statement consists of one or more ‘clauses.’  
# A clause consists of a header and a ‘suite.’  # The header has a keyword (e.g. if) and a conditional followed by a colorn
# The clause headers of a particular compound statement are all at the same indentation level. 
# Each clause header begins with a uniquely identifying keyword and ends with a colon. 
    # In decision structures, the clause contains the condition 
# A suite is a group of statements controlled by a clause.  (Digital Ocean refers to the suite as a 'clause', error?)
    # (Severence refers to the suite as a 'block', the glossary calls it "body")
# A suite can be one or more semicolon-separated simple statements on the same line as the header, following the header’s colon, 
#   or it can be one or more indented statements on subsequent lines. 
# Only the latter form of a suite can contain nested compound statements 
# (Python.org)

if x < y < z: print(x); print(y); print(z)numberChoice = int(input('Please enter a number between 1 and 10: '))
if numberChoice == 5:  # This is the if clause statement.  A clause is started with if, followed by a condition ("boolean expression"), then a colon:
    # There is a condition
    print('Your number', numberChoice, 'is correct!')  # this is the block (group) of code that follows the clause, 
                # indicated by the 4 space indentation.  This is known as compound statements because it takes more than one line.
                # If the condition in the clause tests True, the block will be executed
                # If the condition in the clause tests False, the block will be skipped
    # Then there is an action
                

#**********************************************(Gaddis, test_average.py)
# This program gets three test scores and displays
# their average.  It congratulates the user if the
# average is a high score.

# The high score variable holds the value that is
# considered a high score.
high_score = 95
 
# Get the three test scores.
test1 = int(input('Enter the score for test 1: '))
test2 = int(input('Enter the score for test 2: '))
test3 = int(input('Enter the score for test 3: '))

# Calculate the average test score.
average = (test1 + test2 + test3) / 3

# Print the average.
print('The average score is', average)

# If the average is a high score,
# congratulate the user.
if average >= high_score:
    print('Congratulations!')
    print('That is a great average!')
#**************************************************

# --> if-else <--
    # A Dual Alternative (multi-branch) decision structure.  Has two execution blocks (aka branches), one that occurs if the clause tests True, 
    # the other only executes if the clause tests False
    # indentation:  make sure the if clause and else clause are aligned.
        #  Each block of statements to be executed following the clause must be indented and identically indented,
        #       by 4 spaces, by convention.  Don't use tabs in text apps, the indentations are not always accurate
    # There can only be one else statement (whereas there can be multiple elif - see below)
grade = 40
if grade >= 70:
    print("You passed the class!")
else:
    print("You did not pass the class :(")
print("Thank you for attending.")  # Returns:  You did not pass the class :(    Thank you for attending.

# Determine if a number is even or odd (Codio)
number = input('Please enter a number')
if number %2 == 0:
    print(str(number) + ' is even')
else:
    print(str(number) + ' is odd')

#**************************************************(Gaddis, auto_repair_payroll.py)
# Variables to represent the base hours and
# the overtime multiplier.
base_hours = 40       # Base hours per week
ot_multiplier = 1.5   # Overtime multiplier

# Get the hours worked and the hourly pay rate.
hours = float(input('Enter the number of hours worked: '))
pay_rate = float(input('Enter the hourly pay rate: '))

# Calculate and display the gross pay.
if hours > base_hours:
    # Calculate the gross pay with overtime.
    # First, get the number of overtime hours worked.
    overtime_hours = hours - base_hours

    # Calculate the amount of overtime pay.
    overtime_pay = overtime_hours * pay_rate * ot_multiplier

    # Calculate the gross pay.
    gross_pay = base_hours * pay_rate + overtime_pay
else:
    # Calculate the gross pay without overtime.
    gross_pay = hours * pay_rate

# Display the gross pay.
print('The gross pay is $', format(gross_pay, ',.2f'), sep='')
#***************************************************************

# If there are multiple decisions to be made (multiple branches), two ways to handle this:
    # 1) Nested If Else statements
    # 2) Elif statements, aka Chained conditionals

# Chained conditional example
choice = 'b'
if choice == 'a':
    print('Bad guess')
elif choice == 'b':
    print('Good guess')
elif choice == 'c':
    print('Close, but not correct')

# Nested conditionals accomplish the same thing, but can get bulky.
choice = 'b'
if choice == 'a':
    print('Bad guess')
else:
    if choice == 'b' :
        print('Good guess')
    else:
        print('Close, but not correct')


#**********************************************************(Gaddis, loan_qualifier.py)
# This program determines whether a bank customer qualifies for a loan.
#  It uses nested decision structures to test more than one condiition.

min_salary = 30000.0  # The minimum annual salary
min_years = 2         # The minimum years on the job

# Get the customer's annual salary.
salary = float(input('Enter your annual salary: '))

# Get the number of years on the current job.
years_on_job = int(input('Enter the number of ' +
                         'years employed: '))

# Determine whether the customer qualifies.
if salary >= min_salary:
    if years_on_job >= min_years:
        print('You qualify for the loan.')
    else:
        print('You must have been employed', \
              'for at least', min_years, \
              'years to qualify.')
else:
    print('You must earn at least $', \
          format(min_salary, ',.2f'), \
          ' per year to qualify.', sep='')
#***************************************************(Gaddis, loan_qualifier2.py)

# This version of the same program  but uses logical operators to simplify the code.
# It still determines whether a bank customer qualifies for a loan.

min_salary = 30000.0  # The minimum annual salary
min_years = 2         # The minimum years on the job

# Get the customer's annual salary.
salary = float(input('Enter your annual salary: '))

# Get the number of years on the current job.
years_on_job = int(input('Enter the number of ' +
                         'years employed: '))

# Determine whether the customer qualifies.
if salary >= min_salary and years_on_job >= min_years:
    print('You qualify for the loan.')
else:
    print('You do not qualify for this loan.')
#*****************************************************

# Testing a series of conditions --- Uses nesting of if-else statements

#******************************************************
# This program gets a numeric test score from the
# user and uses nested conditionals to display the corresponding letter grade.

# Variables to represent the grade thresholds
A_score = 90
B_score = 80
C_score = 70
D_score = 60

# Get a test score from the user.
score = int(input('Enter your test score: '))
 
# Determine the grade.
if score >= A_score:
    print('Your grade is A.')
else:
    if score >= B_score:
        print('Your grade is B.')
    else:
        if score >= C_score:
            print('Your grade is C.')
        else:
            if score >= D_score:
                print('Your grade is D.')
            else:
                print('Your grade is F.')
#****************************************************************

# --> if-elif-else <--

#   Multi-Alternative decision structures
#   elif is short for else if, and can be used to add additional conditionals.
#   elif clauses are similar to if clauses.  There is a key word, a conditional, then a colon,
#       This is followed by a block of code that executes if the elif tests True
#   once an elif statement tests True, its block of code executes and all other elifs and else is skipped.
#   
#   You can have multiple elifs 
#   Using elif is a better way to handle the program above
#       The if, elif, and else commands are aligned.  This is easier to follow than the nested if else statements."="
#   Order Matters!  Exits at a True, it does not check them all.
#   The else statement is not required, but if used, must be placed at the end.

grade = 85  

if grade >= 90:  # This tests False, so it is skipped
    print("You passed the class with an A.")
elif grade >= 80: # This tests True, so its block of code executes.
    print("You passed the class with a B.")
elif grade >= 70:  # This is skipped
    print("You passed the class with a C.")
else:               # This is skipped
    print("You did not pass the class :(")

print("Thanks for attending.")   # Amos (p. 203)
# returns:  You passed the class with a B.  Thanks for attending.

#***************************************************************
# Variables to represent the grade thresholds
A_score = 90
B_score = 80
C_score = 70
D_score = 60

# Get a test score from the user.
score = int(input('Enter your test score: '))

if score >= A_score:
    print('Your grade is an A. ')
elif score >= B_score:
    print('Your grade is a B. ')
elif score>= C_score:
    print('Your grade is a C. ')
elif score>= D_score:
    print('Your grade is a D. ')
else:
    print('Your grade is an F')
#*******************************************************************

# Nested if-elif-else statements - to handle more complex logic problems.

sport = input("Enter a sport: ")
p1_score = int(input("Enter player 1 score: "))
p2_score = int(input("Enter player 2 score: "))

if sport.lower() == "basketball":    # High score wins
    if p1_score == p2_score:
        print("The game is a draw.")
    elif p1_score > p2_score:
        print("Player 1 wins.")
    else:
        print("Player 2 wins.")
elif sport.lower() == "golf":       # Low score wins
    if p1_score == p2_score:
        print("The game is a draw.")
    elif p1_score < p2_score:
        print("Player 1 wins.")
    else:
        print("Player 2 wins.")
else:
    print("Unknown sport")    # (Amos et. al, p. 205)

# note the .lower method is used in order to compare strings with more accuracy

# This code allows for seven different possible outcomes (execution paths):
#       Sport             Score values 
#   "basketball"    p1_score == p2_score 
#   "basketball"    p1_score > p2_score 
#   "basketball"    p1_score < p2_score 
#   "golf"          p1_score == p2_score     
#   "golf"          p1_score > p2_score 
#   "golf"          p1_score < p2_score 
#   everything else     any combination

# nested if statements are discouraged because it can make it difficult to know how to predict
#   how the program will behave under certain conditions.
# 
# to simplify the above code, make fewer "nests"  - this leads to only 6 possible outcomes

sport = input("Enter a sport: ")
p1_score = int(input("Enter player 1 score: "))
p2_score = int(input("Enter player 2 score: "))

if p1_score == p2_score:
    print("The game is a draw.")
elif sport.lower() == "basketball":
if p1_score > p2_score:
        print("Player 1 wins.")
    else:
        print("Player 2 wins.")
elif sport.lower() == "golf":
    if p1_score < p2_score:
        print("Player 1 wins.")
    else:
        print("Player 2 wins.")
else:
    print("Unknown sport.")


# to further simplify it, use compound conditionals that incorporate logical operatators

sport = input("Enter a sport: ")
p1_score = int(input("Enter player 1 score: "))
p2_score = int(input("Enter player 2 score: "))

sport = sport.lower()

p1_wins_bball = (sport == "basketball") and (p1_score > p2_score)
p1_wins_golf = (sport == "golf") and (p1_score < p2_score)
p1_wins = player1_wins_basketball or player1_wins_golf

sport = sport.lower()
if p1_score == p2_score:
    print("The game is a draw.")

elif (sport == "basketball") or (sport == "golf"):
    p1_wins_bball = (sport == "basketball") and (p1_score > p2_score)
    p1_wins_golf = (sport == "golf") and (p1_score < p2_score)
    p1_wins = p1_wins_bball or p1_wins_golf
    if p1_wins:
        print("Player 1 wins.")
    else:
        print("Player 2 wins.")
else:
    print("Unknown sport")   # (Amos et. al, p. 205)


#--> String Comparisons <--

# Comparing strings for equality using the == operator
# String comparisons are case sensitive, e.g. Saturday and saturday are not equal

# ************************************************************(Gaddis, password.py)
# This program compares two strings.
# Get a password from the user. (in this case the password entered should be prospero)

password = input('Enter the password: ')

# Determine whether the correct password
# was entered.
if password == 'prospero':
    print('Password accepted.')
else:
    print('Sorry, that is the wrong password.')
#****************************************************

# Other String Comaprisons:

# Strings can be tested equal or not-equal, they can also be tested as > or <
    # This allows strings to be sorted in some order (a<z, small letters < capital letters)
        # Shorter strings are considered less than longer strings:  Hi < High
    # Python does this by comparing the Unicode Code Point (prev. ASCII code) for each character.
# e.g. Character codes for Mary 77 97 114 121,  Character codes for Mark  77 97 114 107
name1 = 'Mary'
name2 = 'Mark'
if name1 > name2:
    print('Mary is greater than Mark')
else:
    print('Mary is not greater than Mark')  # returns Mary is greater than Mark  (the y character, 121 is > the k character 107)

# "In Python, strings are ordered lexicographically, which is a fancy way of saying they’re ordered 
#   as they would appear in a dictionary. So you can think of "a" < "b" as asking whether the 
#   letter a comes before the letter b in the dictionary."" (Amos et.al, p.188)

#**********************************************(Gaddis, sort_names.py)
# This program compares strings with the < operator.
# Get two names from the user.
name1 = input('Enter a name (last name first): ')
name2 = input('Enter another name (last name first): ')
    
# Display the names in alphabetical order.
print('Here are the names, listed alphabetically.')

if name1 < name2:
    print(name1)
    print(name2)
else:
    print(name2)
    print(name1)
#*****************************************************************

# --> try/except Structure <--

# Catching Errors using Try and Except (Without stopping the program - this is critical)
    # When asking for input, and the user doesn't put in the correct type of answer, 
        # for example, the user is supposed to put in a numeral which becomes a string, but 
        # instead puts in alphabetical characters.  Trying to convert and calculate with the 
        # input will cause an error.     (Severance p. 36)

prompt = "What is the air velocity of an unladen swallow?\n"
speed = input(prompt)
    # The prompt shows:  What is the air velocity of an unladen swallow?
    # The user types: 'What do you mean, an African or a European swallow?'
int(speed)
# This will throw a traceback error:  ValueError: invalid literal for int() with base 10:
#   An alphabetical string cannot be converted to an integer.

inp = input('Enter Fahrenheit Temperature:')
try:
    fahr = float(inp)
    cel = (fahr - 32.0) * 5.0 / 9.0
    print(cel)
except:
    print('Please enter a number')
# Code: http://www.py4e.com/code3/fahren2.py
# The except block is ignored unless something goes wrong.
# Don't put multiple statements in the try block:  if one blows up, the rest are skipped.
-
# Short Circuit Evaluation of Logical Expressions
'''When Python is processing a logical expression such as x >= 2 and (x/y) > 2, it evaluates the expression from left to right. 
Because of the definition of and, if x is less than 2, the expression x >= 2 is False and so the whole expression is False 
regardless of whether (x/y) > 2 evaluates to True or False.
When Python detects that there is nothing to be gained by evaluating the rest of a logical expression, 
it stops its evaluation and does not do the computations in the rest of the logical expression. 
When the evaluation of a logical expression stops because the overall value is already known, it is called short-circuiting the evaluation.
While this may seem like a fine point, the short-circuit behavior leads to a 
clever technique called the ''' # guardian pattern.     (Severance, pp37-38)

# Consider the following code sequence in the Python interpreter:
x = 6
y = 2
x >= 2 and (x/y) > 2   # returns True   no error

x = 1
y = 0
x >= 2 and (x/y) > 2   # retirms False   no error

x = 6
y = 0
x >= 2 and (x/y) > 2
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# ZeroDivisionError: division by zero     Causes an error because you're trying to divide with zero

x >= 2 and y != 0 and (x/y) > 2  # Solves this with y != 0 acgting as a guard.
# This doesn't work if the y != 0 is placed in the wrong spot.  e.g. x >= 2 and (x/y) > 2 and y != 0
    # This will error, because it is executed left to right and the zero division occurs first, stopping the program.

# References:
#
# Amos, D., Bader, D., Jablonski, J., Heisler, F. (2022). Python Basics:  A Practical Introduction to Python 3. (4th ed.).
#       USA: Real Python.  www.realpython.com.

# Codio. /unit-2---python-decision-structures/tree/code%2Fselection%2Fif-else-statement.py
#   (student access only)

# Gaddis, T. (2018). Starting out with Python. (4th Ed).  Chapter 3:  Decision Structures and Boolean Logic 
#   New York, NY: Pearson Educational.  pp 109-140. and ppt cpt 3

# Python.org(2022). Compound Statements
#   https://docs.python.org/3/reference/compound_stmts.html

# Severance, C.R. (2009). Python for Everybody: Exploring Data Using Python 3. 
#   Chapter 3. Conditional executios.  Creative Commons.  
#   Available for download at www.py4e.com.  

# Tagliaferri, L. (2018).  How to Code in Python.  New York, NY: Digital Ocean.  
#   download:  https://assets.digitalocean.com/books/python/how-to-code-in-python.pdf
