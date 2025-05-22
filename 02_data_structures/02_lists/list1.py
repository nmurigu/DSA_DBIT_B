my_list = [10, 20, 30, 40, 60, 70, 80, 90]
mixed_list = [1, "apple", True, 3.14]
print(f" Original list: {my_list}")
#
# # Get first element
print(f" First element: {my_list[0]}")
#
# # Get last element
print(f" Last element: {my_list[-1]}")
#
# # Modify element
my_list[1] = 25
print(f"  After modifying index 1: {my_list}")
#
# # Add to end
my_list.append(50)
print(f"  After appending 50: {my_list}")
#
# # Insert 99 at index 2
my_list.insert(0, 99)
print(f" After inserting 99 at index 0: {my_list}")
# All elements will be pushed back
#
# Removes first occurrence of value 25
my_list.remove(25)
print(f" After removing 25: {my_list}")
#
# # Removes and returns last element
removed = my_list.pop()
print(f" Popped element: {removed}")
print(f" After pop(): {my_list}")
#
# # Deletes element at index 0
del my_list[0]
print(f" After deleting index 0: {my_list}")
#
# # Elements from index 1 to 2
last_index = my_list[-2]
print(f" {last_index} ")

sliced = my_list[2:-2]
print(f" Sliced list : {sliced}")
#
# # Iterating through the list
print(f" Iterating through my_list:")
for item in my_list:
    print(f"  {item}")
