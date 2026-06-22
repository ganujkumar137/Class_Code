# Tupple is a data structure that is similar to a list, but 
# it is immutable, meaning that once it is created, it cannot
# be modified. Tupple is defined using parentheses () and can
# contain any number of elements, including other tupple.
# Example of creating a tupple


# my_tupple = (1, 2, 3, 'hello', [4, 5], (6, 7))
# print(my_tupple)  # Output: (1, 2, 3, 'hello', [4, 5], (6, 7))
# print(type(my_tupple))  # Output: <class 'tuple'>

# marks_tuple = (50,60,70,80,90)
# print(marks_tuple)  # Output: (50, 60, 70, 80, 90)
# print(type(marks_tuple))  # Output: <class 'tuple'>
# print(marks_tuple[-1])  # Output: 90
# print(marks_tuple[::-1])  # Output: (50, 60, 70)
# marks_tuple[2]=500 # Output: (60, 70, 80)
# print(marks_tuple)  # Output: (50, 60, 500, 80, 90)

# Write a program to extract all numbers greater than 55 from marks_tuple
# marks_tuple = (50,60,70,80,90)
# # extracted_numbers = tuple(x for x in marks_tuple if x > 55)
# # print(extracted_numbers)  # Output: (60, 70, 80, 90)

# marks_tuple = (50,60,70,80,90)
# new_tuple = []
# for x in marks_tuple:
#     if x > 55:
#         new_tuple.append(x)
# print(tuple(new_tuple))
# print(type((new_tuple)))

# waf to sum of indicies of a tupple

marks_tuple = (50,60,70,80,90)
# def sum_of_indices(tup):
#     total = 0
#     for i in range(len(tup)):
#         total += i
#     return total

# print(sum_of_indices(marks_tuple))  # Output: 10
# counter = 0
# for i in range(len(marks_tuple)):
#     counter += i
# print(counter)  # Output: 10

# lis comprehension to sum of indices of a tupple

marks_tuple = (50,60,70,80,90)
sum_of_indices = sum([i for i in range(len(marks_tuple))])

print(sum_of_indices)  # Output: 10


