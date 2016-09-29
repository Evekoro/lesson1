def find_person(name):
	names = ["Вася", "Маша", "Петя", "Валера", "Леша", "Саша", "Даша"]
	while names:
		if name == names.pop():
			print(name + " тут")
			break
	#print(", ".join(names)+" не пришли")

find_person("Петя")
find_person("Маша")
find_person("Эвклид")