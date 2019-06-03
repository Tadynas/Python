shopping_list = []


def show_help():
	print("What should we pickup at the store?")
	print("""
Enter "DONE" to stop adding items.
Enter "SHOW" to show all the items in the list.
Enter "HELP" for this help.
""")
	
	
def add_to_list(item):
	shopping_list.append(item)
	print("Added! List has {} items.".format(len(shopping_list)))	
	
def show_list():
	print("Here's your list:")
	i = 1
	for item in shopping_list:
		print("{}. {}".format(i, item))
		i += 1
	
	
show_help()
while True:
	new_item = input("> ")
	
	if new_item == "DONE":
		break
	elif new_item == "HELP":
		show_help()
		continue
	elif new_item == "SHOW":
		show_list()
		continue
	
		
	add_to_list(new_item)
	
show_list()