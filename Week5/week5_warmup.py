# Problem Set 1: Indexing and Slicing Strings
# Basic Indexing:
# Given the string magic = 'abracadabra',
magic = "abracadabra"
# a. Retrieve the 5th character.
print(magic[4])
# b. Retrieve the second to last character.
print(magic[-2])
# c. Find the first occurrence of the letter 'c'.
print(magic.find('c'))
# Advanced Slicing:
# Given the string alphabet = 'abcdefghijklmnopqrstuvwxyz',
abc = "abcdefghijklmnopqrstuvwxyz"
# a. Extract the letters 'hij'.
print(abc[7:10])
# b. Extract every second letter starting from 'a' to 'm'.
print(abc[0:12:2])
# c. Reverse the entire string using slicing.
print(abc[::-1])
# Problem Set 2: Extracting Information
# From Descriptions:
# Extract the name of the famous personality from the 
quote = "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
print(quote.find("John"))
print(quote[83:])
# Manipulating Words:
# Given the string 
info = "Python is fun. Fun is good. Good is subjective."
# a. Extract the word 'subjective' without knowing its exact position.
print(info.find("subjective"))
print(info[36:])

# b. Extract every third word.
words = info.split()

every_third_word = words[::3]
result = " ".join(every_third_word)
print(result)
# c. Reverse the positions of the words, but keep the characters in each word in the same order.

# Problem Set 3: String Methods
# Upper & +:
# Convert the following text to lowercase: "MAY THE FORCE BE WITH YOU."
star = "MAY THE FORCE BE WITH YOU."
print(star.lower())
# String Joining and Splitting:
# Given the list 
motto = ["Make", "haste", "slowly."]
# a. Convert the list into a single string.
joined =" ".join(motto)
print(joined)
# b. Now, split the string at every occurrence of the letter 'a'.
print(joined.split("a"))
# Replacing Words:
# Modify the 
sentence = "Life is what happens when you are busy making other plans."
# a. Replace "busy" with "distracted".
print(sentence.replace("busy","distracted"))
# b. Replace "plans" with "mistakes".
print(sentence.replace("plans","mistakes"))
# Problem Set 4: String Properties and Advanced Operations
# Repetition:
# Concatenate the word "Iteration" 7 times.
result2 = "Iteration" * 7
print(result2)
# Word Search:
# Check if the word "moonlight" appears in the 
quote2 = "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"
print("moonlight"in quote2)
# Length and Count:
# a. Calculate the number of characters (including spaces and punctuation) in the word/ 
phrase = "Supercalifragilisticexpialidocious"
print(len("Supercalifragilisticexpialidocious"))
# b. Count the number of times the letter 'i' appears in the same word/phr
print(phrase.count("i"))