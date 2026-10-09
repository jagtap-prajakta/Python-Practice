# 09 Oct 2026
# Practice  Assignment: 

# # 1. print the table of odd number from 1 to 10:
# for i in range(1, 11, 2):
#     print("Table of Odd numbers from 1 to 10")
#     print(f"Table of {i}")

#     for j in range(1, 11):
#         print(f"{i} × {j} = {i * j}")

# 2. create heterogeneous list of numbers and names. split the list from highest number
l = [1, 2, 3, 4, 'Prajakta', 'Nandini', 50, 'Asha', 'Samruddhi', 40, 30 ]
nums = [1,2,3,4,50,40,30]
highest_num = max(nums)
print("Highest num in the list: ",highest_num)
print(l[:l.index(highest_num)])   #split og list l.index(highest_num) finds the index of 50 in th og list. the index of 50 is 6.  so l[:6] prints all elements before index 6
print(l[l.index(highest_num)+1:])   #index(highest_num) gives 6. so 6 + 1 = 7 i.e. a[7:] it prints from index 7 to the end



# # 3. Accept the name and check if it is palindrome
# name = input("Enter a name to check if it is palindrome: ")
# rev = ''
# for i in name:
#     rev = i + rev
#     if rev == name:
#         print("given name is palindrome")
#     else:
#         print("given name is not a palindrome")

# name = input("Enter a name to check if it is palindrome: ")
# if name[::-1] == name:
#     print("Palindrome")
# else:
#     ("Not palindrome")

    
# # 4. Print the sum of digits
# num = input("Enter a number to check sum of its digits: ")
# sum = 0
# for i in num:
#     sum += int(i)   #what if given num is negative
# print(sum)



# # 5. Print following pattern
# #     *
# #     ##
# #     ***
# #     ####
# for i in range(1, 5):
#     if i == 1:
#         print("*"*1)
#     elif i == 2:
#         print("#"*2)
#     elif i == 3:
#         print("*"*3)
#     else:
#         print("#"*4)


# how can you convert a kist to string or wise versa, same for other data types

# 6. create a pyramid pattern:
#      *
#    * * *
#   * * * * 
#  * * * * * 
for i in range(1, 6):
    

# 2.1 add more 2 numbers at third position of a list and append one name in a list and then split



# create a dictionary for liabrary and display the books are available and check if certain book is available.
