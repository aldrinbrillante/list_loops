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
songs.extend(["On Bended Knee", "Water Runs Dry", "Back At One"])
# print(songs)
# LOL sorry to whoever is looking at this lol I was watching Fresh Prince BelAir Boyz II Men episode while doing quiz


# There are also several methods that can remove elements from a list:
            # removes element from list
            #        songs.remove("ROCKSTAR")
            # removes and returns element at specific index
            #       songs.pop(1)
            # removes all elements from a list
            #       songs.clear()
            # delete the 3rd element
            #       del songs[3]


# TASK: delete one of the elements in your songs list in your list_loops.py file
del songs[4] # deletes 'water runs dry' 
print(songs)


# QUESTION 5:
# Lists Combined with Loops
# Loops let us repeat blocks of code over and over and over...without having to write tons of code!
# If we want to repeat something a specified number of times we can use a for loop.

# There are a couple different ways we can print out all the items in a list using a for loop:
            # Option 1
            # for song in songs:
            #      print(song) 

            # Option 2
            # for i in range(len(songs)):
            #    print(songs[i])

# TASK: What are the differences between these two approaches?
# In option 1, you are creating the temporary variable song to be from the former variable 'songs,' 
# and then printing the new variable 'song' out. Which would print what ever was in the previous variable "songs."
# For option 2, you are specifically using the 'for i in range()' iterator variable, and
# specifically making the range/parameter as the current LENGTH of the songs list.


# QUESTION 6:
# Final Task:
# 1. Create another list called 'animals' and fill it with 3 animal strings 
        # of your choice such as "Cat", "Dog", and "Bird"
animals = ["dog", "cat", "mouse"]

# 2. Add another animal to your list
animals.append("bear")
# 3. print out the 3rd animal in the list // should print out 'mouse'
print(animals[2])
# 4. Delete the first animal in the list
animals.remove("dog")
# 5. Use a loop to print out all the animals in your animals list
for i in animals:
    print(i) # should print out 'cat , mouse , bear' 
# 6. Paste the link to your code ON GRADESCOPE QUIZ when you have completed the tutorial tasks