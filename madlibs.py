
# Homework: Create a madlib. Imagine a story where some of the words are 
# supplied by user input. Using python you will use input to collect 
# words for a story and then display the story. 

# Use input to collect each word to a variable
# Use an f string to display the story

adj_def = "Please enter an adjective. (Beautiful, Horrific, etc.)"
noun_def = "Please enter a common noun. (Prince, Rock, etc.)"

print(""" 
Welcome to the Madlib! Please enter a unique response to each of the following prompts, followed by the enter key to create your one-of-a-kind madlib story!
""")
      
adj_1 = input(adj_def)
noun_1 = input(noun_def)
adj_2 = input(adj_def)
noun_2 = input(noun_def)
verb_1 = input("Please input a movement verb in the past tense. (Ran, Rolled, etc.)")
verb_2 = input("Please input any verb in the past tense. (Kicked, Coughed, etc.)")
adverb_1 = input("Please input an adverb ending in -ly. (Quickily, Softly, etc.)")
exclaim_1 = input("Please input an exclamatory sentence. (Great Job!, Go Away!, etc.)")

# Your madlib must collect at least 6 words!
print(f"""
      Once upon a time, one {adj_1} {noun_1} lived atop a hill in an old, {adj_2} cabin. 
      One day, the {adj_1} {noun_1} saw a suspicious {noun_2} from their window.
      Startled, the {noun_1} {verb_1} outside. The {noun_2} {verb_2} {adverb_1} at the {noun_2}.
      Startled, the {noun_2} shouted '{exclaim_1}' and fled away.""")






# --------------------------------------------------
# Partial solution


# name = input("Name:")
# color = input("color:")
# num = input("Number:")

# print(f"{name} wore {color} shoes while they counted to {num}")