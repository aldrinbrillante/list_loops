# In Python, we can use lists to help us stay organized 
# by storing all relevant pieces of information in one place.
# a LIST is an ordered collection of objects and are considered a sequence data type.

# Lists can be of any size and contain any mix of data types.

songs = ["ROCKSTAR", "Do It", "For The Night"]

# In ordered to use our list later, we will store the list to a 
# variable using the assignment operator ' = '. The list we created above is called songs.

# QUESTION 2:
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


# QUESTION 3:
# Updating Elements
# Lists also allow us to change elements in the list after it has been created.
# First, we access the item we want to update using its index. Then, we use the
# assignment operator ' = ' to update the value at that specified index.

            # update the first element
            # songs[0] = "Dynamite"
            # print the list
            # print(songs)


# Task: update the last element in the songs list with a new song 
# of your choice in your list_loops.py file

songs[2] = "End of the Road" #Boyz II Men

# QUESTION 4: 
# To add and remove elements from lists, we need to learn how to use methods.
# A method is similar to a function, except it is associated with object. 
# Sequence objects (strings, lists, etc) have different methods than Numeric objects methods.

# There are several methods that can add new elements to a list: 
            # adds an element to the end of the list
            #       songs.append("Mood")
            # adds a list to end of a list
            #       songs.extend(["Laugh Now Cry Later", "Blinding Lights"])
            # adds element at specific index followed by item
            #       songs.insert(0, "Life Is Good")

# TASK: add three songs of your choice to your songs list in your list_loops.py file
songs.append("On Bended Knee", "Water Runs Dry", "Back At One")
# LOL sorry I was watching Fresh Prince Boyz II Men episode while doing quiz
print(songs)






