list = []
a = int(input("Meddig?\n"))

sum = 0
avg = 0.0
while len(list) != a:
	list.append(int(input("Szám:")))
print()

for x in range(len(list)):
	min = list[0]
	max = list[0]
	sum += list[x]
	if list[x] < min:
		min = list[x]
	if list[x] > max:
		max = list[x]
	print(x+1,".szám:",list[x])

avg = sum / len(list)
print("\nA megadott számok közül a legkisebb:",min,"legnagyobb:",max,"és az átlaguk:",avg)
