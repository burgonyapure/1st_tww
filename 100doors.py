ajtok = [False] * 101

for i in range(100):
	for j in range(0,len(ajtok),i+1):
		ajtok[j] = not(ajtok[j])

print("Nyitott ajtók:")
for i in range(len(ajtok)):
	if ajtok[i] == True:
		print(i)
