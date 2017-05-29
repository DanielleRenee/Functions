"""
Skills function assessment.

Please read the the instructions first (separate file). Your solutions should
go below this docstring.

"""

###############################################################################

# PART ONE: Write your own function declarations.

# NOTE: We haven't given you function signatures or docstrings for these, so
# you'll need to write your own.

#    (a) Write a function that takes a town name as a string and evaluates to
#        `True` if it is your hometown, and `False` otherwise.

#    (b) Write a function that takes a first and last name as arguments and
#        returns the concatenation of the two names in one string.

#    (c) Write a function that takes a home town, a first name, and a last name
#        as arguments, calls both functions from part (a) and (b) and prints
#        "Hi, 'full name here', we're from the same place!", or "Hi 'full name
#        here', I'd like to visit 'town name here'!" depending on what the function
#        from part (a) evaluates to.


def is_hometown(townname):
    """Determines if hometown

    >>> is_hometown("houston")
    True

    >>> is_hometown("dallas")
    False

    """
    if townname == "houston":
        return True

    else:
        return False


def full_name(first, last):
    """Returns the concatenation of first and last names
       in one string.

    >>> full_name("danielle", "russell")
    'danielle russell'

    """
    name = "{} {}".format(first, last)
    return name



def greeting(first, last, townname):
    """Calls both functions from part (a) and (b)
    creates greeting message accordinly.

    >>> greeting("james", "taylor", "houston")
    Hi, james taylor, we're from the same place!

    >>> greeting("ticia", "gerber", "geneva")
    Hi, ticia gerber, I'd like to visit geneva!

    """

    if is_hometown(townname):
        print "Hi, {}, we're from the same place!".format(full_name(first,last))
        return

    else:
        print ("Hi, {}, I'd like to visit {}!".format(full_name(first, last),(townname)))
        return

###############################################################################

# PART TWO

#    (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "raspberry", or
#        "blackberry."

#    (b) Write another function, shipping_cost(), which calculates shipping
#        cost by taking a fruit name as a string and calling the `is_berry()`
#        function within the `shipping_cost()` function. Your function should
#        return 0 if is_berry() == True, and 5 if is_berry() == False.

#    (c) Make a function that takes in a number and a list of numbers. It should
#        return a new list containing the elements of the input list, along with
#        given number, which should be at the end of the new list.

#    (d) Write a function calculate_price to calculate an item's total cost by
#        adding tax, and any fees required by state law.

#        Your function will take as parameters (in this order): the base price of
#        the item, a two-letter state abbreviation, and the tax percentage (as a
#        two-digit decimal, so, for instance, 5% will be .05). If the user does not
#        provide a tax rate it should default to 5%.

#        CA law requires stores to collect a 3% recycling fee, PA requires a $2
#        highway safety fee, and in MA, there is a Commonwealth Fund fee of $1 for
#        items with a base price under $100 and $3 for items $100 or more. Fees are
#        added *after* the tax is calculated.

#        Your function should return the total cost of the item, including tax and
#        fees.


def is_berry(fruit):
    """Determines if fruit is a berry

    >>> is_berry("blackberry")
    True

    >>> is_berry("durian")
    False

    """
    if fruit in ('blackberry', 'raspberry', 'strawberry'):
        return True

    else:
        return False

is_berry("blackberry")

def shipping_cost(fruit):
    """Calculates shipping cost of fruit

    >>> shipping_cost("blackberry")
    0

    >>> shipping_cost("durian")
    5

    """
    if is_berry(fruit):
        return 0
    else:
        return 5

shipping_cost("blackberry")
shipping_cost("durian")


def append_to_list(lst, num):
    """Returns a new list consisting of the old list with the given number
       added to the end.

    >>> append_to_list([3, 5, 7], 2)
    [3, 5, 7, 2]

    """
    new_lst = lst + [num]
    return new_lst

append_to_list([3, 5, 7], 2)


def calculate_price(FILL_ME_IN):
    """Calculate total price of an item, figuring in state taxes and fees.

    >>> calculate_price(40, "CA")
    43.26

    >>> calculate_price(400, "NM")
    420.0

    >>> calculate_price(150, "OR", 0.0)
    150.0

    >>> calculate_price(60, "PA")
    65.0

    >>> calculate_price(38, "MA")
    40.9

    >>> calculate_price(126, "MA")
    135.3

 
    """
CA_TAX_RATE = .08

def calculate_price(base_price, state, tax_rate=.05):
    
    if state == "CA":
        tax_rate = CA_TAX_RATE
        return
    
    if state == "PA":
        base_price = base_price + 2
        return
   
    total = base_price + (base_price * tax_rate)

    #if state == "MA":
        #pass
        #return

    return ("%.2f" % round(total, 2))
    print ("%.2f" % round(total, 2))
    
calculate_price(40, "CA")
calculate_price(60, "PA")
calculate_price(400, "NM")
calculate_price(150, "OR", 0.0)
calculate_price(38, "MA")
calculate_price(126, "MA")

###############################################################################

# PART THREE: ADVANCED

# NOTE: We haven't given you function signatures and docstrings for these, so
# you'll need to write your own.

#    (a) Make a new function that takes in a list and any number of additional
#        arguments, appends them to the list, and returns the entire list. Hint: this
#        isn't something we've discussed yet in class; you might need to google how to
#        write a Python function that takes in an arbitrary number of arguments.

#    (b) Make a new function with a nested inner function.
#        The outer function will take in a word.
#        The inner function will multiply that word by 3.
#        Then, the outer function will call the inner function.
#        Print the output as a tuple, with the original function argument
#        at index 0 and the result of the inner function at index 1.

#        Example:

#        >>> outer("Balloonicorn")
#        ('Balloonicorn', 'BalloonicornBalloonicornBalloonicorn')

def make_list(list_values, *args):

     # loop to iterate through length of args parameter
     for i in range(len(args)):
          # append the args at each index to the existing list
          # listValues
          list_values.append(args[i])

     # return the appended list
     return list_values

# outterFunction() function accepts a word as argument and returns a tupple.
def outter_function(word):
     # innerFunction() function accepts a word and the count to multiple
     # the word to count times and returns the multiplied word
     def inner_function(word, count):
          # if count is 1 return the word
          if count == 1:
               return word
          #otherwise, just return by appending the word with recursive call
          # to the inner function
          else:                              
               return str(word) + str(inner_function(word, count-1))

     # return the tuple where the tuple at index[0] holds the word
     # and the index[1] holds the resulant of the innerFunction()
     return (word, inner_function(word, 3))

# test cases:
# test for the makeList() by passing the integer list with some unknown arguments
print(make_list([1, 2, 3, 4, 5, 6], 8, 6, 3, 2, 10))

# test for the makeList() by passing the string with some unknown string arguments
print(make_list(["sunday", "python", "funday"], "Danielle", "ice cream", "birthday", "pizza"))




###############################################################################

# END OF ASSESSMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
