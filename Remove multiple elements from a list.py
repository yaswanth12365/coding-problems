# Python program to remove multiple
# elements from a list

# creating a list
list1 = [11, 5, 17, 18, 23, 50]

# will create a new list,
# excluding all even numbers
list1 = [ elem for elem in list1 if elem % 2 != 0]

print(*list1)
