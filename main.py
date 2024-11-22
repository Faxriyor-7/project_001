# Exercise 1
# numbers = input("add the numbers ::: ").split(" ")
# numbers = [int(i) for i in numbers]
# print(numbers)
#
# l = len(numbers)
#
# c = 0
#
# n = []
#
# for i in numbers:
#     c +=i
#
# middle = c // l
#
# print(middle)
#
# for i in numbers:
#     if middle < i:
#         n.append(i)
#     else:
#         pass
# print(n)


# ...
# Exercise 2
# number = input("Enter the number :: ").split(" ")
# number = [int(i) for i in number]
#
#
#
# for i in range(len(number) - 1):
#     if number[i] > number[i + 1]:
#         number[i], number[i + 1] = number[i + 1], number[i]
#
# print(number)


# ...
# Exercise 5
# text = input("Enter the 7 character :: ")
#
# cat_count = text.count("cat")
#
# print(f"The 'Cat' sense appears {cat_count} times")


# ...
# Exercise 6
# txt = input("Enter the 5 character :: ")
#
# n = len(txt)
#
# for i in range(n):
#     shifted = txt[-i:] + txt[:-i]
#     print(shifted)


# ...
# Exercise 7

# print("3x3 massiv uchun 9 ta sonni kiriting (masalan: 1 2 3 4 5 6 7 8 9):")
#
# elements = list(map(int, input().split()))
#
# matrix = [elements[i:i+3] for i in range(0, len(elements), 3)]
#
# main_diagonal_sum = sum(matrix[i][i] for i in range(3))
#
# print("Asosiy diagonal elementlarining yig'indisi:", main_diagonal_sum)






