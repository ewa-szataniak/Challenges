

#Excercise #1 Accept two user ages as inputs and give us the difference between them. The Answer should always be a positive output

age1 = input("Please write the first age: ")
age2 = input("Please write the second age: ")

age1 = int(age1)
age2 = int(age2)


difference = abs(age1-age2)
print("The difference between your ages is: ", difference, "years")

# Exercise #2 Accept 3 user inputs for variables named noun, verb and adjective. Print out a formatted string using the outputs.

noun = input("Please write the name: ")
verb = input("Please write a verb: ")
adjective = input("PLease write an adjective: ")
Sentence = noun + " " + verb + " " + adjective + "."
print(Sentence)


#Exercise #3 Take in a users input for their age, if they are younger than 18 print kids, if they're 18 to 65 print adults, else print seniors

age = input("What is your age? ")
age = int(age)
if age < 18:
  print("kids")
elif age <= 65:
  print("adults")
else:
  print("seniors")


#Exercise #4 Take in a number from a user input output the number squared.
num = input("Write a number, so I can tell you the square of it: ")
num = int(num)
print("The square of", num, "is equal to", num**2)


# Exercise #5 Check the below variables' length. If the length of the word is greater than 5 output True, if it is less than 5, output False

word1 = "panini"
word2 = "bulbasaur"
word3 = "pie"
word4 = "dolphin"
word5 = "dog"

w1=len(word1)
w2=len(word2)
w3=len(word3)
w4=len(word4)
w5=len(word5)

print("For the word",word1, w1>5)
print("For the word",word2, w2>5)
print("For the word",word3, w3>5)
print("For the word",word4, w4>5)
print("For the word",word5, w5>5)