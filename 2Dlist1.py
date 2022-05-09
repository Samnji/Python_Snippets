# 2D array of integers and appending item to a row
d_list = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]

for item in d_list:
	print(item)
row = int(input("Enter row number you would like to display: "))

print(d_list[row])

ans = int(input("Enter a new value to be added to the row: "))

d_list[row].append(ans)

print(d_list[row])
