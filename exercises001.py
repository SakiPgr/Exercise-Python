# 1. Write a Puthon program to print the following string in a specific format

# Sample String
"Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are"

# The output
'''
Twinkle, twinkle, little star,
	How I wonder what you are! 
		Up above the world so high,   		
		Like a diamond in the sky. 
Twinkle, twinkle, little star, 
	How I wonder what you are
'''

# 1.1 My solution. This is also the one that is sited as solution on the page
text = "Twinkle, twinkle, little star,\n\tHow I wonder what you are!\n\t\tUp above the world so high,\n\t\tLike a diamond in the sky.\nTwinkle, twinkle, little star,\n\tHow I wonder what you are"

print(text)
print('\n\n')

# Explanation of the solution.
# Python as all(?) programming languages has escape characters. In this case we use
# \n which is the newline escape and the \t which is the escape for the tab character.
# A list of escape characters can be found here
# https://python-reference.readthedocs.io/en/latest/docs/str/escapes.html


# 2. Write a Python program to get the Python version you are using.

# My solution. I put it on purpose in a string so only the complete solution as given by the site
# is shown
'''
import sys
print(sys.version)
'''

# Solution given on the site
import sys
print('Python version')
print(sys.version)
print('Version info')
print(sys.version_info)
print('\n\n')

# Solution explanation. The sys module is quite useful. If you want to learn about it look up
# the official python documentation at https://docs.python.org/3/library/sys.html for Python 3
# or this resource https://www.python-course.eu/sys_module.php if this is easier for you. Although
# written in python 2 there shouldn't be any major difference in using the sys module.


# 3. 