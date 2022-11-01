
"""
Write a program to find all of the roots of the quadratic.

Note: The output should be up to 2nd decimal place (round off if needed) and in case of a recurring decimal use braces i.e. for eg: 0.33333..... => 0.33.

Note: Use Shri Dharacharya's Method to solve i.e. X = {-b + √(b² - 4ac) } / 2a & {-b-√(b² -4ac)} / 2a

Input Description:
Three numbers corresponding to the coefficients of x(squared), x and constant are given as an input in that particular order

Output Description:
Print the two values of X after rounding off to 2 decimal places if required.

Sample Input :
1 5 6
Sample Output :
-2.00
-3.00

"""

#Program

import math
a,b,c = [int(a) for a in input().split()]
d = float(math.sqrt((b*b)-(4*a*c)))
X = float((-b+d)/(2*a))
Y = float((-b-d)/(2*a))
print('{:.2f}'.format(round(X, 2)))
print('{:.2f}'.format(round(Y, 2)))
