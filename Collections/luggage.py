def packer(**kwargs):
    print(kwargs)

packer(name="Ted", num=42, has_money=None)
#{'name': 'Ted', 'num': 42, 'has_money': None}

def packer(name=None, **kwargs):
    print(kwargs)

packer(name="Ted", num=42, has_money=None)
#{'num': 42, 'has_money': None}

def unpacker(first_name=None, last_name=None):
    if first_name and last_name:
        print("Hi {} {}!".format(first_name,last_name))
    else:
        print("Hi no name!")

unpacker(**{"last_name": "Gringo", "first_name": "Ted"})
#Hi Ted Gringo!

print("Hi, I'm {name} and I love to eat {food}!".format(name="Ted", food="pizza"))
#Hi, I'm Ted and I love to eat pizza!

def favorite_food(dict):
    return "My favorite food is: {food}".format(**dict)

print(favorite_food({"food":"Taco"}))
#My favorite food is: Taco

course_minutes = {"Python Basics": 232, "Django Basics": 237, "Flask Basics": 189, "Java Basics": 133}

for course, minutes in course_minutes.items():
    print("{} is {} minutes long".format(course, minutes))
#Python Basics is 232 minutes long
#Django Basics is 237 minutes long
#Flask Basics is 189 minutes long
#Java Basics is 133 minutes long

print(list(enumerate("abc")))
#[(0, 'a'), (1, 'b'), (2, 'c')]

for index, letter in enumerate("ABCDEFK"):
    print("{}: {}".format(index+1, letter)) #or start=1 and no index+1
#1: A
#2: B
#3: C
#4: D
#5: E
#6: F
#7: K