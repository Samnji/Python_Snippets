# Enter num to divided items in an float array
from array import *
import math

nums = array('f', [ 65.27, 36.36, 28.62, 23.82, 37.23 ])

while True:
	num = int(input("Enter a number between 2 and 5: "))
	
	if num > 2 and num < 5:
		for item in nums:
			ans = item / num
			print(round(ans,2))

		break
	else:
		print("Number out of range!!!!")
		continue	