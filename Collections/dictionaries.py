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

#Dictionary iteration
course_minutes = {"Python Basics": 232, "Django Basics": 237, "Flask Basics": 189, "Java Basics": 133}

for course in course_minutes:
    print(course)
#Python Basics
#Django Basics
#Flask Basics
#Java Basics

for course in course_minutes:
    print(course_minutes[course])
#232
#237
#189
#133

for key in course_minutes.keys():
    print(key)
#Python Basics
#Django Basics
#Flask Basics
#Java Basics    

for value in course_minutes.values():
    print(value)
#232
#237
#189
#133

for item in course_minutes.items():
    print(item)
#('Python Basics', 232)
#('Django Basics', 237)
#('Flask Basics', 189)
#('Java Basics', 133)

def word_count(text):
    text = text.lower()
    words = text.split()
    print(words)
    dictionary = {}
    for word in words:
        dictionary[word] = 0
    for word in words:
        dictionary[word] += 1
    return dictionary

print(word_count("I love the way I am"))
#{'i': 2, 'love': 1, 'the': 1, 'way': 1, 'am': 1}

def word_count_second(text):
    words = text.lower().split()
    dictionary = {}
    for word in words:
        dictionary[word] = words.count(word)
    return dictionary


print(word_count_second("As soon as possible"))
#{'as': 2, 'soon': 1, 'possible': 1}