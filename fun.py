lol = [87, 84, 60, 76, 12, 35, 90, 92, 82, 33, 96, 80, 95, 33, 71, 36, 63, 12, 28, 75, 72, 58, 77, 79, 41]

for i in range(len(lol)):
	min_val = lol[i]
	for j in range(len(lol)):
		if min_val < lol[j]:
			temp = lol[i]
			lol[i] = lol[j]
			lol[j] = temp

print("SORTED")
print(lol)
