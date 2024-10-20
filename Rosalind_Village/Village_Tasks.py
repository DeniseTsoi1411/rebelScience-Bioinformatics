##### Task 1: Installing Python
# import this
# -----------------------------------------------------------------------------------------------------------------------

##### Task 2: Variables and Some Arithmetic
# Given: Two positive integers a and b, each less than 1000.
# Return: The integer corresponding to the square of hypotenuse of the right triangle whose legs have lengths a and b.

## My solution
a = 828
b = 805
print("Task 2, My solution:", a ** 2 + b ** 2)

## rebel Solution
print("Task 2, rebel solution:", f'{a}^2 + {b}^2 = {a ** 2 + b ** 2}')
# Using f-strings to format a sentence, can also input pre-determined objects by their values
# -----------------------------------------------------------------------------------------------------------------------

##### Task 3: Strings and Lists
# Given: A string s of length at most 200 letters and four integers a, b,  c and d.
# Return: The slice of this string from indices a through b and c through d (with space in between),
# inclusively. In other words, we should include elements s[b] and s[d] in our slice.

# Example Q = HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyin
# hisplaceagain.
# 22 27 97 102
# Example A = Humpty Dumpty

a = 30
b = 40
c = 128
d = 134
s = "M60UR2jZL73oSWBwJwfRFwXE2QxibJNemorhaedusgLMnS1VksKksowCOaD8ENRCrWMYUEUn80Htco2jGFWEfAUSYw4BRfq1whwRiXZFFMHlQ7" \
    "oSxghhL194GHgoRXEyboschasQTbNHSXlF1ea0VJXEwrBe4RrvikixUJtmesuVJCMIMpEdFy72RDiZM."

## My solution
# result = ' '.join(str(s[a:b+1]) + str(s[c:d+1]))
# print("Task 3, My solution:", result) # Not sure how to do this w/o f-strings

## Rosalind solution
print("Task 3, Rosalind solution 1:", s[a:b + 1], s[c:d + 1])  # Solution 1
print("Task 3, Rosalind solution 2:", s[a:b + 1] + ' ' + s[c:d + 1])  # Solution 2

## rebel solution
print("Task 3, rebel solution:", f'{s[a:b + 1]} {s[c:d + 1]}')  # Another way to print using f-strings
# -----------------------------------------------------------------------------------------------------------------------

##### Task 4: Conditions and Loops
# Given: Two positive integers a and b (a<b<10000).
# Return: The sum of all odd integers from a through b, inclusively.

a = 4955
b = 9233

## My solution
tmp = []
for i in range(a, b + 1):
    if i % 2 == 1:
        tmp.append(i)
    else:
        pass
print("Task 4, My solution:", sum(tmp))

## rebel solution 1
tmp = 0
for i in range(a, b + 1):
    if i % 2 != 0:  # Checks if its division by 2 has a remainder of 0 or not
        tmp += i
print("Task 4, rebel solution 1:", tmp)

## rebel solution 2
tmp = sum([i for i in range(a, b + 1) if i % 2 != 0])  # square brackets for lists
print("Task 4, rebel solution 2:", tmp)
# -----------------------------------------------------------------------------------------------------------------------

##### Task 5: Working with Files
# Notes:
# open() -> To open and access certain files. Have the following 3 modes:
# r = read mode (opened for reading)
# w = write mode (opened for writing; would erase other files if have same name)
# a = append mode (opened to add data to existing data to a file)
# EG f = open('filename.txt', 'r')
# Methods that can be used on 'f':
# f.read(n) -> returns n bytes of data from file. No n = return entire content
# f.readline() -> Takes a single line from file if lines end with "\n", else returns all data
# All lines in file (except for last) ends with "\n"
# f.strip() -> removes "\n" from a line
# f.readlines() -> returns every line from file as a list
# f.readlines()[2] -> returns 3rd line from file
# Ways to parse files / lines:
# line.split() -> Uses whitespaces and "\n" as delimiters and separate words
# Can also specify delimiter:
# EG 'Explicit, is better, than implicit.'.split(",") ==
# ['Explicit', ' is better', ' than implicit.']
# .splitlines() -> Returns list for lines in string broken at line boundaries
# EG 'Simple is\nbetter than\ncomplex.\n'.splitlines() ==
# ['Simple is', 'better than', 'complex.']
# How to save a file:
# 1. Output file in write mode
# EG f = open('output.txt', 'w')
# 2. Write data using .write() method
# EG f.write('Any data you want to write into file')
# Can only be used on strings (Might need to use str())
# EG f.write(str(i) + '\n') == Writes i to f and starts new line after every item

# Given: A file containing at most 1000 lines.
# Return: A file containing all the even-numbered lines from the original file. Assume 1-based numbering of lines.

## My solution
# result = []
f = open('input.txt', 'r')
result = f.readlines()[1::2]

f = open('out.txt', 'w')
f.write(''.join([line for line in result]))
# Need join cuz 'result' is a list, while 'write()' requires a str
# Need [] cuz you are taking elements out of the list

## rebel solution
# outputfile = []
with open('input.txt', 'r') as f:
    outputfile = [line for pos, line in enumerate(
        f.readlines()) if pos % 2 != 0]
        # enumerate() = Adds counter to an iterable -> Returns it in a form of enumerating object

with open('out.txt', 'w') as f:
    f.write(''.join([line for line in outputfile]))
# to write the results in another file
# if 'out.txt' doesn't exist, it makes one (cuz have 'w')
# ----------------------------------------------------------------------------------------------------------------------

##### Task 6: Dictionaries

# Given: A string s of length at most 10000 letters.
# Return: The number of occurrences of each word in s, where words are separated by spaces. Words are case-sensitive,
# and the lines in the output can be in any order.

s = "When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour" \
    " of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it " \
    "be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree " \
    "There will be an answer let it be For though they may be parted there is still a chance that they will see There" \
    " will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be" \
    " let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper" \
    " words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine until" \
    " tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be" \
    " Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be" \
    " yeah let it be Whisper words of wisdom let it be"

## rebel solution 1
d = dict()  # dict == {}

for words in s.split(' '):
    if words in d:
        d[words] += 1  # d[words] = d[words] + 1
    else:
        d[words] = 1

print("Task 6, rebel solution 1:", d)

## rebel solution 2
from collections import Counter

d = Counter(s.split(' '))
# Counter creates a dictionary automatically, do not need to define it first


for key, value in d.items():
    print("Task 6, rebel solution 2:", key, value)
    # A different way to present results

## Rosalind solution
string = 'example text'
word_counts = {}
for s in string.split():
    word_counts[s] = word_counts.get(s, 0) + 1

for w in word_counts:
    print(w, word_counts[w])
