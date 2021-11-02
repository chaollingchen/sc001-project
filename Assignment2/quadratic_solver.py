"""
File: quadratic_solver.py
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math


def main():
	"""
	This program first use y to determine how many roots will the equation have.
	Then, it can calculate the roots of the equation.
	"""
	print('stanCode Quadratic Solver! ')

	a = int(input('Enter a :'))
	b = int(input('Enter b :'))
	c = int(input('Enter c :'))
	y = b*b-4*a*c


	if y<0:
		print('No real roots')
	elif y==0:
		x1 = (b * (-1) + math.sqrt(y)) / 2
		print('One root:' + str(x1))
	else:
		x1 = (b * (-1) + math.sqrt(y)) / 2
		x2 = (b * (-1) - math.sqrt(y)) / 2
		print('Two roots:' + str(x1) + ',' + str(x2))





###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
