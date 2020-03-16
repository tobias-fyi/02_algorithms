# # Returns the secret to beautiful code
# def secret_to_coding_1():
#   print ("")
#   print ("Beautiful code is both ELEGANT and EFFICIENT")
#   print ("  ELEGANT: concise, easy to read, easy to understand, easy to maintain, easy to modify")
#   print ("  EFFICIENT: minimal CPU operations, minimal memory/storage requirements")
#   print ("")
#   for _ in range(1000):
#       print("hello")


# # Returns the secret to beautiful code
# def secret_to_coding_2():
#   print ("\nBeautiful code is both ELEGANT and EFFICIENT\n  ELEGANT: short, easy to read, easy to understand, easy to maintain, easy to modify\n  EFFICIENT: minimal CPU operations, minimal memory/storage requirements\n")


# def my_for_loop(n):
#     print(n)

# my_for_loop(10000)


# import random

# my_range = 10
# my_size = 10

# my_random = random.sample(range(my_range), my_size)

# print(my_random)

# def print_number(n):
#     print(my_random[n])


# print_number(4)

# def print_array(arr):
#     for i in range(len(arr)):
#         print(arr[i])


# print_array(my_random)


# animals = ['Duck', 'Jackal', 'Hippo', 'Aardvark', 'Cat', 'Flamingo', 'Iguana', 'Giraffe', 'Elephant', 'Bear', 'Duck', 'Jackal', 'Hippo', 'Aardvark', 'Cat', 'Flamingo', 'Iguana', 'Giraffe', 'Elephant', 'Bear', 'Duck', 'Jackal', 'Hippo', 'Aardvark', 'Cat', 'Flamingo', 'Iguana', 'Giraffe', 'Elephant', 'Bear', 'Duck', 'Jackal', 'Hippo', 'Aardvark', 'Cat', 'Flamingo', 'Iguana', 'Giraffe', 'Elephant', 'Bear']


# def print_animals(animal_list):
#     my_number = 0
#     for i in range(len(animal_list)):
#         print(animal_list[i])
#         for _ in range(100000):
#             my_number += 1


# print_animals(animals)

# def print_animal_pairs():
#     for animal_1 in animals:
#         for animal_2 in animals:
#             print(f"{animal_1} - {animal_2}")

# print_animal_pairs()

# def print_animal_triplets():
#     for animal_1 in animals:
#         for animal_2 in animals:
#             for animal_3 in animals:
#                 print(f"{animal_1} - {animal_2} - {animal_3}")

# print_animal_triplets()

# def get_animal_combos(l):
#     list_length = len(l)
#     if list_length == 0:
#         return [[]]

#     else:
#         animal_combos = []
#         previous_combos = get_animal_combos(l[1:])
#         for combo in previous_combos:
#             animal_combos.append(combo)
#             animal_combos.append(combo + [l[0]])
#         return animal_combos


# # print(get_animal_combos(animals))

# import random
# import time

# my_range = 100000000
# my_size = 1000000

# my_random = random.sample(range(my_range), my_size)

# # print(my_random)

# searching_for = 7


# def find_in_number():
#     for i in range(len(my_random)):
#         if my_random[i] == searching_for:
#             return True

#     return False

# def find_value_binary(arr, value):
#     if len(arr) <= 1:
#         # TODO Handle edge
#         pass

#     first = 0
#     last = (len(arr) - 1)

#     found = False

#     while first <= last and not found:
#         # find middle using integer divsion
#         middle = (first + last) // 2

#         if arr[middle] == value:
#             found = True

#         else:
#             if value < arr[middle]:
#                 # search lower half of remainder
#                 last = middle - 1
#             else:
#                 # search upper half of remainder
#                 first = middle + 1

#     return found

# print("Linear")
# start = time.time()
# print(find_in_number())
# end = time.time()
# print(f"Runtime: {end - start}")

# print("Binary")
# start = time.time()
# my_random.sort()
# print(find_value_binary(my_random, searching_for))
# end = time.time()
# print(f"Runtime: {end - start}")

# print("Binary _after_ sort")
# start = time.time()
# print(find_value_binary(my_random, searching_for))
# end = time.time()
# print(f"Runtime: {end - start}")


my_list = [8, 2, 5, 4, 1, 3]


def insertion_sort(list_to_sort):
    # separate first element, think of it as sorted

    # for all other indices, starting at 1
    for i in range(1, len(list_to_sort)):
        # put current number in a temp variable
        temp = list_to_sort[i]
        # look left, until we find where it belongs
        j = i
        while j > 0 and temp < list_to_sort[j - 1]:
            print(j)
            # as we look left shift items to the right as we iterate
            list_to_sort[j] = list_to_sort[j - 1]
            j -= 1

        # When left is smaller than temp, or we're at zero, put at this spot
        list_to_sort[j] = temp

    return list_to_sort


print(insertion_sort(my_list))
