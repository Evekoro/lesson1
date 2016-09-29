names = ["Вася", "Маша", "Петя", "Валера", "Леша", "Саша", "Даша"]
while names:
	name = names.pop()
	if name == "Леша":
		print("Леша тут")
		break
print(", ".join(names)+" не пришли")