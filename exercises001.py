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


# 3. Write a Python program to display the current date and time.

# Sample Output
# Current date and time
# 2014-07-05 14:34:14

# My solution
import datetime

time_now = datetime.datetime.now()
print(time_now.strftime('%y-%m-%d %H:%M:%S'))
print()

# Output of my solution is: 19-12-04 06:37:55
# the datetime module is probably one that is going to be used a lot. I have used it 
# in some occasions but that does not mean I know it well. My solution is slightly different
# from what was asked. 

# Solution as given on the site
# I won't import datetime again
# import datetime
now = datetime.datetime.now()
print('Current date and time : ')
print(now.strftime('%Y-%m-%d %H:%M:%S'))
print("\n")

# To find more information about the datetime module have a look at the official site
# https://docs.python.org/3.7/library/datetime.html or maybe at this one
# https://www.w3schools.com/python/python_datetime.asp or this which has even more examples
# https://www.programiz.com/python-programming/datetime


# 4. Write a Python program which accepts the radius of a circle from the user and compute
# the area.

# Now to get the area of a circle you can simply search for that on the internet should you
# not remember how to compute that. No biggy.
# Or use this radius (r) to the power of 2 (**2) times pi (π)
# Or short r**2 * π

# My solution
import math  # I import math to get the value for pi (π)

radius = float(input("Please enter the radius: "))
print(radius**2 * math.pi)

# The output is 3.8013271108436504 which is the same as given by the site
# The math module is very important if you have to make computations with
# higher precision and you can import constants to use for your programs

# Solution as given by the site
from math import pi
r = float(input("Input the radius of the circle : "))
print("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))
print("\n\n")

# To find more information about the math module look up the official site
# https://docs.python.org/3.7/library/math.html or this one if this helps
# https://www.programiz.com/python-programming/modules/math

