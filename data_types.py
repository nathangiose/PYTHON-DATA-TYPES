# The first data type-
# Lists
# A list can be an array of many data types


list1 = [123, 'ABC', 10.2, 'd']
# The next list will comprise of text


list2 = ['Hello', 'Beautiful', 'World']
# The print command will display what I want displayed


print(list1)
print(list2)
# The result that will be displayed next is what I want displayed
# So, now I will print pieces of the information I want printed
# Remember that the first number in the lists' value is 0
# Now we're printing the first 2 elements of each list


print(list1[0:2])
print(list2[0:2])
# The next print command will give us the amount of information we want
# So if I want the lists I created to print 3 times, I would say,
# lists * 3. It's best to use your own amounts whilst practicing


print(list1 * 3)
print(list2 * 3)
# The next print command will add (concatenate) the lists
# By adding, it won't be doing the same command as "sum"


print(list1 + list2)
# Space for a small example


print("")
# Let's see what we can get if we merge all the data into one print statement:


print((list1[0:3] * 2) + (list2[0:2] * 3))
# It's crazy, yeah?


print("")
print("Well Done!")