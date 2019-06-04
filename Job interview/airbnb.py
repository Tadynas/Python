def reverse(text):
    return text[::-1]

print(reverse("ABCDEFG"))

#find_missing(
#   [4, 12, 9, 5, 6],
#   [4, 9, 12, 6]

def find_missing(list1, list2):
    for item1 in list1:
        if item1 not in list2:
            return item1;

print(find_missing([4, 12, 9, 5, 6], [4, 9, 12, 6]))

def find_missing_with_sets(set1, set2):
    return set1 - set2

print(find_missing_with_sets({4, 12, 9, 5, 6}, {4, 9, 12, 6}))

def find_missing_with_sets_and_lists(list1, list2):
    return set(list1) - set(list2)

print(find_missing_with_sets_and_lists([4, 12, 9, 5, 6], [4, 9, 12, 6]))

