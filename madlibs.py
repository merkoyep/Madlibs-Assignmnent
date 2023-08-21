
# Homework: Create a madlib. Imagine a story where some of the words are 
# supplied by user input. Using python you will use input to collect 
# words for a story and then display the story. 

# Use input to collect each word to a variable
# Use an f string to display the story

adj_1 = input("Please enter an adjective")
noun_1 = input("Please input a noun.")
adj_2 = input("Please enter an adjective")
noun_2 = input("Please input a noun.")
verb_1 = input("Please input a verb in past tense.")
adverb_1 = input("Please input an adverb.")
exclaim_1 = input("Please input an exclaimation.")

# Your madlib must collect at least 6 words!
print(f"""
      Once upon a time, a {adj_1} {noun_1} lived isolated in a {adj_2} castle. 
      One day, the {adj_1} {noun_1} saw a {noun_2} outside their window.
      Excited to see something, the {noun_1} {verb_1} {adverb_1} at the {noun_2}.
      Startled, the {noun_2} shouted '{exclaim_1}' and fled. They warned everyone to stay away from the castle.
      Nobody dared visit the {noun_1} at their castle ever again.""")






# --------------------------------------------------
# Partial solution


# name = input("Name:")
# color = input("color:")
# num = input("Number:")

# print(f"{name} wore {color} shoes while they counted to {num}")