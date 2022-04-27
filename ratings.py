"""Restaurant rating lister."""


# put your code here
file = open('scores.txt')

dictionary = {}

for line in file:
    x = line.split(":")
    a = x[0]
    b = x[1]
    c = len(b)-1
    b = b[0:c]
    dictionary[a]=b

print(sorted(dictionary.items()))

restaurant = input("Add a restaurant to rate: ")
score = input("Score this restaurant: ")

dictionary[restaurant] = score

print(sorted(dictionary.items()))