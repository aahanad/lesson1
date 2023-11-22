#The new academic year is starting and you as the store 
#manager are told to take care of accounts of textbook 
#purchases. As a python programmer, you decide to maintain a dictionary of 
#textbooks and its cost. Create a dictionary.
#USE DICTIONARY METHODS FOR THE BELOW STEPS
#a) Later you found that the cost of the physics book was entered wrong. Correct price is 200. Make this change
#b) Add the cost of 2 more books to the dictionary.
#c) Print cost of the book entered by the user.
#d) Print all the books and their cost.
books={
    "dictionary":"150","physics":"310","math":"400"
}
books["physics"]="200"
books["science"]="250"
books["history"]="275"
cost=books[input("enter book name")]
print(cost)

print(books)