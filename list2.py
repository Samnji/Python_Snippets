# Display the position of the number entered
nums = [233, 643, 647, 347]

for num in nums:
	print(num)

typed = int(input("Enter the number you want the position: "))

if typed in nums:
	print(nums.index(typed))

else:
	print("That is not in the list!!!!")