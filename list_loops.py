# In Python, we can use lists to help us stay organized 
# by storing all relevant pieces of information in one place.
# a LIST is an ordered collection of objects and are considered a sequence data type.

# Lists can be of any size and contain any mix of data types.

songs = ["ROCKSTAR", "Do It", "For The Night"]

# In ordered to use our list later, we will store the list to a 
# variable using the assignment operator ' = '. The list we created above is called songs.

# QUESTION 2 TASK:
# Task: print out the FIRST and LAST element of the songs list in your list_loops.py file
# For example, if we wanted to print out the 2nd element of the songs list we could write:
            # print(songs[1])

print(songs[0])
print(songs[2])

# We can also access a range of elements using the slicing operator ' : '
# The 1st number specifies which index to start the slice.
# The 2nd number specifies the end of the slicing, the end element is not included.
        # EXAMPLE: # will print 'ROCKSTAR' and 'Do It'
                    # print(songs[0:2])  

# Task: print out "Do It" and "For The Night" using a list slice 
print(songs[1:3])  





