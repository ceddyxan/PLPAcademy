# Question 1: Empty List called my_list
my_list = []
print (my_list)


# Question 2: Appending Elements 10, 20, 30, 40 to my_list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print (my_list)
# Since .Append ONLY allows appending ONE value at a time, .Extend will be the best when there are SEVERAL values to Append
    # This is an example of how the extend works for the above code
        # add_elements = [10, 20, 30, 40]
        # my_list.extend(add_elements)
        # print (my_list)


# Question 3: Insert the value 15 at the second position in the list
my_list.insert(1, 15)
print (my_list)


# Question 4: Extend my_list with [50, 60, 70]
additional_elements = [50, 60, 70]
my_list.extend(additional_elements)
print (my_list)


# Question 5: Remove the last element from my_list
del my_list [-1]
print (my_list)


# Question 6: Sort my_list in Ascending Order
my_list.sort()
print (my_list)
# Sort my_list in Descending Order
# my_list.sort(reverse=True)
# print (my_list)


# Question 7: Find the index of the value 30 in my_list.
# The value to find
find_value = 30
# Finding the Index
index = my_list.index (find_value)
print (f"The index of {find_value} in the list is: {index}")