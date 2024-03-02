###############################################################################
# Done: 1. (2 pts)
#   
#   This module is going to look very similar to m1 in the Session 10 Coding
#   Exercises, but this time we will use tuples instead of lists.
#
#   For this _TODO_, simply create a tuple called recipes that will have a
#   list of strings that represent different recipes of different meals you
#   might make. Choose whichever meals you like, but make sure you have at
#   least 4 meals in your list.
#
#   Once you have created the tuple, make sure to print out the tuple.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################

meals = ("pizza", "spaghetti", "soup", "stir fry")
print(meals)

###############################################################################
# Done: 2. (2 pts)
#   
#   For this _TODO_, write a line of code that accesses the *second* item in the
#   tuple (remember the index of the first item is 0) and prints the item. Make
#   sure you do NOT create a new tuple, but actually use the original.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################

print(meals[1])

###############################################################################
# Done: 3. (2 pts)
#   
#   For this _TODO_, write some code that changes the *third* item to a
#   different meal that you don't already have in your tuple. Once you have
#   done this, print the tuple. Remember that tuples are immutable (can't be
#   changed) so you will need to convert it to a list, do your modification,
#   and convert it back again.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################

different_meals = list(meals)
different_meals[2] = "hamburgers"
meals = tuple(different_meals)
print(meals)


###############################################################################
# Done: 4. (2 pts)
#   
#   For this _TODO_, write a some code that adds a recipe to the end of
#   the tuple. Once you have done this, print the tuple. Remember that tuples
#   are immutable (can't be changed) so you will need to convert it to a list,
#   do your modification, and convert it back again.
#
#   NOTE: Your solution should work for any tuple of any length. DO NOT use
#   indexes in your solution.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################

additional_meal = list(meals)
additional_meal.append("keish")
meals = tuple(additional_meal)
print(meals)

###############################################################################
# Done: 5. (2 pts)
#   
#   For this _TODO_, write some code that removes the last item from the
#   tuple. Once you have done this, print the tuple. Remember that tuples are
#   immutable (can't be changed) so you will need to convert it to a list, do
#   your modification, and convert it back again.
#
#   NOTE: Your solution should work for any tuple of any length. DO NOT use
#   indexes or reference a specific item in your solution.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################

remove_meal = list(meals)
remove_meal.pop()
meals = tuple(remove_meal)
print(meals)

###############################################################################
# Done: 6. (2 pts)
#
#   In the reading, you saw a concept called unpacking a tuple. If you don't
#   remember what this is, go back an look at the reading. Once you have done
#   that, you should come back to this _TODO_.
#
#   For this _TODO_, write a line of code that unpacks your tuple into a
#   variable for each item in the tuple as it currently is. Once you have done
#   this, print each variable.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
(delicious, alright, good, amazing) = meals
print(delicious)
print(alright)
print(good)
print(amazing)