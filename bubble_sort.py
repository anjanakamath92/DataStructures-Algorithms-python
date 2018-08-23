lst = [5, 6, 0, 1, 2, 4, 3, 9, 8, 7]

for j in range(0, 9):
	check_swap = False
	for i in range(0, 9):
		if lst[i] > lst[i+1]:
			temp = lst[i]
			lst[i] = lst[i+1]
			lst[i+1] = temp
			check_swap = True

	if check_swap == False:
		break

print(j, lst)


