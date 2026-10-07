# 07 OCT 2026
# ------------------------------------------- String Methods -------------------------------------------
text = "   hello, Im Prajakta  "
name = "prajakta"

# # 1. strip
# print("Remove spaces from both ends: ", text.strip())

# # 2. upper
# print("Upper case:", text.upper())

# # 3. lower
# print("Lower case: ", text.lower())

# # 4. Capitalize first letter
# print("Capitalize first letter: ", name.capitalize())

# # 5. Title case (capitalize each word):
# print(text.title())

# # 6.count occurances of a letter
# print("Letter a occurs", text.count("a"))

# # 7. Find the position of a substring (-1 if not found)
# print("Position of Prajakta in the text is: ", text.find("Prajakta"))

# # 8. Replace a substring
# print(text.replace("Prajakta", "Praju"))

# # 9. Check if string starts or ends with certain substring
# print(text.startswith("  hello"))
# print(name.endswith("a"))

# # 10. Split string into
# print(text.split())

# # 11.
# words = ["Python", "is", "fun"]
# print(" ".join(words))
# 




# ------------------------------------------- String Functions -------------------------------------------

# # 12. sorted: Return a new list containing all items from the iterable in ascending order.
# print(sorted(text))
# print(sorted(name))


# ------------------------------------------- Practice Questions -------------------------------------------

# Q. wap to count number of vowels in a string

# text = input("Enter a string: ").lower()

# a = text.count('a')
# e = text.count('e')
# i = text.count('i')
# o = text.count('o')
# u = text.count('u')

# total = a + e + i + o + u

# print(f"Total vowels: {total}")
# print(f"a: {a}, e: {e}, i: {i}, o: {o}, u: {u}")

# wap to print ha ha ha using string functions. get one ha from the user and and print occurances
# txt = "ha"
# # print(txt*3)
# print(txt+3)
# print(txt-3)

# # accept your name and find out the occurances of letter a in your name
# my_name = input("Enter name: ")
# print("Letter a occurs", my_name.count("a"))

# # replace a with z in you name
# print("Replacing a with z in my name: ", my_name.replace("a", "z"))

# # split you name into two different substrings (hint use len function):
# name = input("Enter your name: ")
# n = len(name)
# mid = n // 2

# first_half = name[:mid]
# second_half = name[mid:]

# print(f"First part: {first_half}")
# print(f"Second part: {second_half}")


# ---------------------------------------------- List ----------------------------------------------
# Empty list
my_list = []
print(my_list)   #[]

# with items
fruits = ["apple", "banana", "cherry"]
print(fruits)  #['apple', 'banana', 'cherry']

# to acces any item in the list use index
# 0 is first element and -1 is last element
numbers = [10, 20, 30, 40]
print(numbers[0])
print(numbers[-2])

# append item in the list
colors = ["red", "blue"]
colors.append("green")
print("After adding at last:", colors)

# insert at specific position:
colors.insert(1,"yellow")
print("after insertion at second position: ", colors)

# remove
print("before remove: ", colors)
print("after remoal of red: ", colors.remove("red") )

# pop
print("Remove using pop: ", numbers.pop())


# ------------------------------------------------------ List Functions: -----------------------------------
# length
numbers = [1, 2, 3, 4, 5, 7, 5, 9]
print("No of items in the list are: ", len(numbers))

# sum 
print("sum of the list numbers is: ", sum(numbers))

# sorting
print("list in asc: ", sorted(numbers))
print("list in desc: ", sorted(numbers, reverse=True))

# Q. create a list of 10 numbers and display the sum of last 4 elements
# Q. remove the items from the list located at 2 and 5th position
# Q. print the diff between highest and smallest number of the list
# Q. append a new element in a list which is half of the item of 3rd position element

nums = [50, 60, 70, 80, 99, 66, 1, 2, 3, 4]
print("List: ", nums)

# sum of last 4 elements
print("Sum of last 4:", sum(nums[-4:]))

# remove items at 2nd and 5th pos
nums.pop(2)
nums.pop(5)
print("List after removing items at 2nd and 5th position: ", nums)   #[50, 60, 80, 99, 66, 2, 3, 4]

# diff between highest and smallest number of the list
diff = max(nums) - min(nums)
print("Difference between highest and smallest number of the list: ", diff)

# append a new element in a list which is half of the item of 3rd position element
half = nums[3] / 2
nums.append(half)
print("After appending half of 3rd element:", nums)






'''
# 1. Print sum of first 10 even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]

even = []
for n in numbers:
    if n % 2 == 0:
        even.append(n)
    if len(even) == 10:
        break

print("First 10 even:", even)
print("Sum:", sum(even))

# 2. Accept S and N. Print square of first N numbers starting from S
S = int(input("Enter S: "))
N = int(input("Enter N: "))

for i in range(S, S+N):
    print(f"{i} -> {i*i}")

# 3. Reverse the accepted string
s = 'raj'
print("Reverse:", s[::-1])

# 4. Remove duplicates from list
lst = [10, 20, 30, 40, 10, 20, 55, 60]
unique = list(set(lst))
print("Without duplicates:", unique)

# OR to keep order:
# unique = []
# for x in lst:
#     if x not in unique:
#         unique.append(x)

# 5. Reverse the list
l = [1, 2, 3, 4, 5]
l.reverse() # or l[::-1]
print("Reversed list:", l)
'''