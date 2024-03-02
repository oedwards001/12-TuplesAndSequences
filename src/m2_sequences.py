names = ["Francis", "Elizabeth", "Margaret", "Catherine", "Anthony", "Andrew", "Walter"]

###############################################################################
# Done: 1. (4 pts)
#
#   For this _TODO_, we are going to take a look at lists again to help us
#   understand sequences.
#
#   For this _TODO_, using the list of names from above, do all the steps below
#   in order. Notice as you go how the list is changing (number of items and
#   order). Lists are an example of sequences that can be modified, but they
#   keep the attributes of finite and ordered.
#
#       1. Write a line of code that prints the list.
#       2. Write a line of code that prints the length of the list.
#       3. Write a line of code to add another name to the list. You pick a
#          name.
#       4. Write a line of code that prints the list now.
#       5. Write a line of code that prints the length of the list now.
#       6. Write a line of code that sorts the list in alphabetical order.
#
#          HINT: there is a method for sorting a list called sort(). So, if you
#                wanted to sort a list called people, you would use it like
#                this:
#                   people.sort()
#
#       7. Write a line of code that prints the list now.
#       8. Write a line of code that prints the length of the list now.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
print(names)

print(len(names))

names.append("Olivia")

print(names)

print(len(names))

names.sort()

print(names)

print(len(names))