print(set([1, 3, 5]))
#{1, 3, 5}

print({1,3,5})
#{1, 3, 5}

print({1, 11, 13, 7, 5, 3})
#{1, 3, 5, 7, 11, 13} But not always right order

low_primes = {1, 3, 5, 7, 11, 13}
low_primes.add(17)
print(low_primes)
#{1, 3, 5, 7, 11, 13, 17}
low_primes.update({19, 23}, {2, 29})
print(low_primes)
#{1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29}
low_primes.add(15)
low_primes.remove(15)
print(low_primes)
#{1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29}
low_primes.discard(100) #same as remove but there is no error if item is missing
while low_primes:
    print(low_primes.pop())

songs = {"Rockstar", "Wow.", "Better Now"}
songs.add("Treehouse Hula")
songs.update({"Python Two-Step", "Ruby Rhumba"}, {"My PDF Files"})
songs.discard("My PDF Files")
print(songs)

set1 = set(range(10))
set2 = {1, 2, 3, 5, 7, 11, 13, 17, 19, 23}
print(set1.union(set2)) #set1 still the same
print(set1 | set2) #Union
#{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 13, 17, 19, 23}
print(set1.difference(set2))
print(set1 - set2)
#{0, 4, 6, 8, 9}
print(set2.difference(set1))
#{11, 13, 17, 19, 23}
print(set1.symmetric_difference(set2))
print(set1 ^ set2) #Unique
#{0, 4, 6, 8, 9, 11, 13, 17, 19, 23}
print(set1.intersection(set2))
print(set1 & set2)
#{1, 2, 3, 5, 7}

COURSES = {
    "Python Basics": {"Python", "functions", "variables",
                      "booleans", "integers", "floats",
                      "arrays", "strings", "exceptions",
                      "conditions", "input", "loops"},
    "Java Basics": {"Java", "strings", "variables",
                    "input", "exceptions", "integers",
                    "booleans", "loops"},
    "PHP Basics": {"PHP", "variables", "conditions",
                   "integers", "floats", "strings",
                   "booleans", "HTML"},
    "Ruby Basics": {"Ruby", "strings", "floats",
                    "integers", "conditions",
                    "functions", "input"}
}

def covers(topics):
    cover_list = []
    for course, topic_list in COURSES.items():
        if topics & topic_list:
            cover_list.append(course)

    return cover_list

print(covers({"HTML"}))
#['PHP Basics']

def covers_all(topics):
    cover_list = []
    for course, topic_list in COURSES.items():
        intersection_list = topic_list & topics
        if len(intersection_list) == len(topics):
            cover_list.append(course)
            
    return cover_list

print(covers_all({"floats", "strings"}))
