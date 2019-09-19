def list():
	f_h = open("list.txt","r")
	current = f_h.readlines()
	f_h.close()
	return current

def add():
	count = len(open("list.txt").readlines(  ))
	add = open("list.txt","a")
	ujsor = input("Add an item: ")
	add.write(str(count+1)+"."+"[] "+ujsor+"\n")
	add.close()
	return "Item added."

while True:
	be = input("Please specify a command [list, add, mark, archive]: ")
	if be == "list":
		print("You saved the following to-do items: ")
		tomb = list()
		if len(tomb) == 0:
			print("Yout list is empty!")
		else:
			for i in range(len(tomb)):
				print("\t"+tomb[i],end='')
	elif be == "add":
		print(add())
	elif be == "mark":
		tomb = list()
		uj = open("list.txt","w")
		for i in range(len(tomb)):
			print(tomb[i],end='')
		mark_no = int(input("Which one you want to mark as completed?: "))
		for i in range(len(tomb)):
			if mark_no - 1 == i:
				uj.write(tomb[i][:3]+"X"+tomb[i][3:])
			elif mark_no -1 != i:
				uj.write(tomb[i])		
			else:
				print("err")
		uj.close()

	elif be == "archive":
		tomb = list()
		arch = open("list.txt","w")
		for i in range(len(tomb)):
			print(tomb[i],end='')
		del_no = int(input("Melyiket töröljem?\n"))
		for i in range(len(tomb)):
			if del_no - 1 == i:
				tomb.pop(i)
				for j in range(len(tomb)):
					test = tomb[j]
					test1 = test.replace(test[0:1],str(j+1),1)
					arch.write(test1)
	
		arch.close()

	elif be == "x":
		print("Kilépek!")
		break

	elif be != "list" or be != "add" or be != "mark" or be != "archive":
		print("Nincs ilyen parancs!")
		continue
	
