#Introduction
print(">>>Introduction<<")

course = {"title": "Python Collections"}
print(course)
#{'title': 'Python Collections'}
print(course["title"])
#Python Collections
print(dict([["name", "Ted"]]))
#{'name': 'Ted'}
course = {"title": "Python Collections", "teacher": "Kenneth Love", "videos": 22}
print(course["videos"])
#22
print(course["title"])
#Python Collections
course = {"title": "Python Collections", "teacher": {"first_name": "Kenneth", "last_name": "Love"}, "videos": 22}
print(course)
#{'title': 'Python Collections', 'teacher': {'first_name': 'Kenneth', 'last_name': 'Love'}, 'videos': 22}
print(course["teacher"])
#{'first_name': 'Kenneth', 'last_name': 'Love'}
print(course["teacher"]["first_name"])
#Kenneth

#Coding
player = {"name": "Ted", "remaining_lives": 3, "levels": [1,2,3,4], "items": {"weapon": "sword"}}


#Key management
print(">>>Key management<<<")

ted = {"first_name": "Ted", "job": "Student"}
print(ted)
#{'first_name': 'Ted', 'job': 'Student'}
ted["last_name"] = "Greek"
print(ted)
#{'first_name': 'Ted', 'job': 'Student', 'last_name': 'Greek'}
ted.update({"job": "Python Student", "editor": "Vim"})
print(ted)
#{'first_name': 'Ted', 'job': 'Python Student', 'last_name': 'Greek', 'editor': 'Vim'}
ted["editor"] = "any"
print(ted)
#{'first_name': 'Ted', 'job': 'Python Student', 'last_name': 'Greek', 'editor': 'any'}
del ted["job"]
print(ted)
#{'first_name': 'Ted', 'last_name': 'Greek', 'editor': 'any'}


#Packing and Unpacking dictionaries
print(">>>Packing and Unpacking dictionaries<<<")
