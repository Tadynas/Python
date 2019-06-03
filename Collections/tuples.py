my_tuple = {1, 2, 3}
print(my_tuple)
#{1, 2, 3}

my_second_tuple = 1, 2, 3
print(my_second_tuple)
#(1, 2, 3)

my_third_not_so_tuple = (5)
print(my_third_not_so_tuple)
#{5}

my_third_tuple = (5,)
print(my_third_tuple)
#(5,)

my_fourth_tuple = tuple([1,2,3])
print(my_fourth_tuple)
#(1, 2, 3)

tuple_with_a_list = (1, "apple", [3,4,5])
print(tuple_with_a_list)
#(1, 'apple', [3, 4, 5])

tuple_with_a_list[2][1] = 7
print(tuple_with_a_list)
#(1, 'apple', [3, 7, 5])

a = 5
b = 20
a, b = b, a
print(a, b)
#20 5

a = 5
b = 20
c = b, a
print(c)

#Not so good
def add(*nums):
    total = 0
    for num in nums:
        total += num
    return total

print(add(5,5))
print(add(32))

#Very good
def add(base, *args):
    total = base
    for num in args:
        total += num
    return total

print(add(5, 20))
#25

def multiply(*args):
    total = 1
    for num in args:
        total *= num
    return total

print(multiply(5, 10, 2))

my_dict = {"name:": "Ted", "age": 20}
for key, value in my_dict.items():
    print("{} is {} years old.".format(key, value))

for args in my_dict.items():
    print("{} is {} years old.".format(*args))

my_list = [5, 2, 4, 1, 3]
for index, value in enumerate(my_list, start=1):
    print("{}. {}".format(index, value))

for args in enumerate(my_list):
    print("{}. {}".format(*args))