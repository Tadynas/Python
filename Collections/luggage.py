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