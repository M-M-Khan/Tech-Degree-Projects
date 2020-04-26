# temperature = []
# temperature.append(98.6)
# temperature.append(99.6)

# er_temperature = [101,102,101.4]

# temperature.extend(er_temperature) ## adding one list into another
# temperature.extend("104") # 1 0 4 will append individually into the list. why?
# temperature.extend([103,99,96.7]) #in order add into temperature list pass the numbers with []

# print(temperature)

# primary_care_doctors = ["Dr. Adam", "Dr. Nichols"]
# er_care_doctors = ["Doug", "Sara"]

# all_doctors = primary_care_doctors + er_care_doctors # list concatenation
# print(all_doctors)

# print(len(all_doctors))  # length of list all_doctors

# ###### wish list.py ###
# books = ["Think and grow rich", "7 habits of sucesssful people", "Kite runner"]
# print(books[0])  ## retirving from list

# ### adding to the front of the list, insert method can add anywhere when you sepcify the index number ###

# books.insert(0,"Reclaim your heart")

# ### in-place addition on a list entry ###
# books[0] += " by Yasmin Mojahid"
# print(books)

# ### list are mutable but strings are immutable -accessing characteres of list by index  ###
# lyrics = "Books, check'em out"
# print(lyrics[0])

# #lyrics[0] = "C"  ## You can access a specific character on a String by using an index, but you cannot change it. strings are immuatable

# ## remove a label from an object, deletes the name not the object 
# craigs_lunch = "\N{TACO}"  ## UNICODE
# print(craigs_lunch)

# ### even after deleting books[0], the name of the book is still stored in recommendation
# recommendation = books[0]  ## or books.pop() or books.pop(0)
# del books[0]
# print(books)
# print(recommendation)

# ###  Quiz: ###

# continents = [
#     'Asia',
#     'South America',
#     'North America',
#     'Africa',
#     'Europe',
#     'Antarctica',
#     'Australia',
# ]
# for continent in continents:
#     # print("* " +continent + "\n\n")
   
   
# I'd like you to now only print continents that begin with the letter "A".

# HINT: Remember that you can access characters in a string by index
   
    # if continent[0] == "A": # takes A in Asia, S in South America... because [0]
    #     print(continent)


####### code for review - aim to remove all the elements from the list - loops and mutability ######

# l = [1,2,3,4,5,6]

# #removed one element
# l.remove(2)
# #looping through list and removing element
# for idx, num in enumerate(l):
#      l.remove(num)
#      print('loop 1:', l, idx, num)
# #expected an empty list but instead got two items that too not the last two
# print ('result 1:', l)

# l = [1,2,3,4,5,6]

# #if I use l.copy() in the loop then it works
# for idx, num in enumerate(l.copy()):
#      l.remove(num)
#      print('loop 2:', l, idx, num)
# #got an empty list
# print('result 2:', l)

### making strings from list and lists from string ###
# quote = "Coding is hard"
# words = quote.split()
# print(words)

# import time
# for word in words:
#     print(word)
#     time.sleep(1)

# primary_care_doctors = ["Dr. Adam", "Dr. Nichols"]
# er_care_doctors = ["Doug", "Sara"]

# doctors = ", " .join(primary_care_doctors)  #join method belongs to strings not to list
# print(doctors)

# doctors_string = doctors.split(", ")
# print(doctors_string)


### list inside a list --- useful for rows and columns ####
# travel_expenses = [
#     [5.00, 2.75, 22.00, 0.00, 0.00],
#     [24.75, 5.50, 15.00, 22.00, 8.00],
#     [2.75, 5.50, 0.00, 29.00, 5.00],
# ]

# print(len(travel_expenses)) # 3
# print(travel_expenses[0])
# print(travel_expenses[0][1]) #row selected first and then column

# print("Travel Expenses:")
# week_number = 1
# for week in travel_expenses:
#     print("* week #{}: ${}".format(week_number,sum(week)))
#     week_number +=1

#### exercise for to-do list ######

# shopping_list = []

# def show_help():
#     print("What should we pick up at the store")
#     print('''
#     Enter "DONE" to stop adding items.
#     Enter "HELP" for this help.
#     Enter "SHOW" for complete list.
#     ''')


# def add_to_list(item):
#     shopping_list.append(item)
#     print("Number of items on the list currently: {}".format(len(shopping_list)))


# def show_list():
#     print("Here is your list:")
#     for item in shopping_list:
#         print(item)


# show_help()


# while True:
#     new_item = input("> ")

#     if new_item == "DONE":
#         break
#     elif new_item == "HELP":
#         show_help()
#         continue
#     elif new_item == "SHOW":
#         show_list()
#         continue

#     add_to_list(new_item)

# show_list()

 
# Here is a multi-dimensional list of musical groups. The first dimension is group, the second is group members.
# Can you loop through each group and output the members joined together with a ", " comma space as a separator, please?

# Awesome! Now I'd like to see only groups that are trios, you know 3 members.
# So can you please only print out the trios? It should still use the joined string format from task 1.

# musical_groups = [
#     ["Ad Rock", "MCA", "Mike D."],
#     ["John Lennon", "Paul McCartney", "Ringo Starr", "George Harrison"],
#     ["Salt", "Peppa", "Spinderella"],
#     ["Rivers Cuomo", "Patrick Wilson", "Brian Bell", "Scott Shriner"],
#     ["Chuck D.", "Flavor Flav", "Professor Griff", "Khari Winn", "DJ Lord"],
#     ["Axl Rose", "Slash", "Duff McKagan", "Steven Adler"],
#     ["Run", "DMC", "Jam Master Jay"],
# ]

# for groups in musical_groups:
#     # print(groups)    ### takes each list
#     # musician = ", ".join(groups)
#     # print(musician)  ### converts list into a string with a comma
#     if len(groups) == 3:
#         musician = ", ".join(groups)
#         print(musician)
