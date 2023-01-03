# try:
#     this block of code will run and throw errors if there are any .

# expect:
#    this will arise the errors.

# else:
#     this will execute if there are no errors.

# finally:
#     this will execute regardless the result of try and expect. 





# try:
#     open("demo.py")
#     try:








#         a=5
# if a<10:
#     raise Exception("Value is less than 5")







# import re
# value="this is a string"
# output=re.search("^This.*string$",value)
# print(output)

# pattern=r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*()_+=-])(?=.{8,})"



# import re                                     
# value ="this is a string"
# output= re.search("^this.*string$",value)
# print(output)






import re

value = "This is a string"
e = "This is a string"
output = re.search("^This.*string$", value)

print(output)

pattern = r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$"

# "" - common use of regular expressions is to validate user input. For example, you could use a regular expression to ensure that a password meets certain criteria, like containing at least one letter, one digit, and one special character.

# ^ - In a regular expression pattern, the caret (^) symbol has a special meaning. When it appears at the start of a character class (a group of characters inside square brackets), it negates the class. This means that it matches any character that is not in the class.

# ? - Zero or one occurrences

# = - the equal sign (=) is used in lookahead and lookbehind assertions. Lookahead and lookbehind assertions are special syntax that allow you to check whether a certain pattern appears before or after the current match, without including it in the actual match.

# . - Any character (except newline character)

# * - 	Zero or more occurrences

# [] - A set of characters

# () - Capture and group

# \ - Signals a special sequence (can also be used to escape special characters)

# {} - 	Exactly the specified number of occurrences

# $ - 	Ends with





# \A	Returns a match if the specified characters are at the beginning of the string	
# \b	Returns a match where the specified characters are at the beginning or at the end of a word
#           (the "r" in the beginning is making sure that the string is being treated as a "raw string")	
# \B	Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
#           (the "r" in the beginning is making sure that the string is being treated as a "raw string")	
# \d	Returns a match where the string contains digits (numbers from 0-9)	
# \D	Returns a match where the string DOES NOT contain digits	
# \s	Returns a match where the string contains a white space character	
# \S	Returns a match where the string DOES NOT contain a white space character	
# \w	Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)		
# \W	Returns a match where the string DOES NOT contain any word characters
# \Z	Returns a match if the specified characters are at the end of the string



# [arn]	        Returns a match where one of the specified characters (a, r, or n) is present	
# [a-n] 	    Returns a match for any lower case character, alphabetically between a and n	
# [^arn]	    Returns a match for any character EXCEPT a, r, and n	
# [0123]    	Returns a match where any of the specified digits (0, 1, 2, or 3) are present	
# [0-9]	        Returns a match for any digit between 0 and 9	
# [0-5][0-9]	Returns a match for any two-digit numbers from 00 and 59	
# [a-zA-Z]	    Returns a match for any character alphabetically between a and z, lower case OR upper case	
# [+]	        In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string






# []	A set of characters
# \	    Signals a special sequence (can also be used to escape special characters)
# .	    Any character (except newline character)
# ^	    Starts with
# $	    Ends with
# *	    Zero or more occurrences
# +	    One or more occurrences
# ?	    Zero or one occurrences
# {}	Exactly the specified number of occurrences
# | 	Either or
# ()	Capture and group
