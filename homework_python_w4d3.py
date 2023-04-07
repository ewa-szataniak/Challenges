# CODEWARS CHALLENGES #


#Question 1 "Find out whether the shape is a cube": #
#................................................. #

#To find the volume (centimeters cubed) of a cuboid you use the formula:

#volume = Length * Width * Height

#But someone forgot to use proper record keeping, so we only have the volume, and the length of a single side!

#It's up to you to find out whether the cuboid has equal sides (= is a cube).

#Return true if the cuboid could have equal sides, return false otherwise.

#Return false for invalid numbers too (e.g volume or side is less than or equal to 0).

#Note: side will be an integer.


# Answer: #

def cube(volume, side):
    for i in range(side):
        if i**3 == volume:
            return True
    return False

# This code checks if any number from 0 to side-1 when cubed is equal to volume. If such a number is found, it returns True.
#If no such number is found, it returns False. This code takes longer to run as side becomes larger and fucnction "cube" has linear time complexity.


def cube (volume, side):
    return 0 < volume == side**3

#This "cube" function is very fast because it does a quick check to see if the volume matches the cube's dimensions,
#and it can do this for any input values without slowing down. 
# The function has a constant time complexity and only performs two single operations. 



#Question 2 Alphabet war: #
#................................................. #

# There is a war and nobody knows - the alphabet war!
# There are two groups of hostile letters. The tension between left side letters and right side letters was too high and the war began.

#Task
#Write a function that accepts fight string consists of only small letters and return who wins the fight. When the left side wins return Left side wins!, when the right side wins return Right side wins!, in other case return Let's fight again!.

#The left side letters and their power: w - 4 p - 3 b - 2 s - 1 The right side letters and their power: m - 4 q - 3 d - 2 z - 1
#The other letters don't have power and are only victims.



# Answer: #

def alphabet (fight):
    left_side = {"w": 4, "p": 3, "b": 2, "s": 1}
    right_side = {"m": 4, "q": 3, "d": 2, "z": 1}
    left_side_count = 0
    right_side_count = 0
    for ch in fight:
        if ch in left_side:
            left_side_count += left_side[ch]
        elif ch in right_side:
            right_side_count += right_side[ch]
    if left_side_count > right_side_count:
        return ("Left side wins!")
    elif right_side_count > left_side_count:
        return ("Right side wins!")
    else:
        return ("Let's fight again!")
    
    
# Function "alphabet" has here linear time complexity.
# This means that the algorithm's running time increases linearly with the size of the input (here "fight")


def alphabet (fight):
    left_side = {"w": 4, "p": 3, "b": 2, "s": 1}
    right_side = {"m": 4, "q": 3, "d": 2, "z": 1}
    fight = sorted(fight)
    left_side_count = 0
    right_side_count = 0
    i = 0
    while i < len(fight):
        ch = fight[i]
        if ch in left_side:
            left_side_count += left_side[ch]
            i += 1
        elif ch in right_side:
            right_side_count += right_side[ch]
            i += 1
        else:
            fight.pop(i)
    if left_side_count > right_side_count:
        return ("Left side wins!")
    elif right_side_count > left_side_count:
        return ("Right side wins!")
    else:
        return ("Let's fight again!")
    
#One way to make the "alphabet" function faster is to sort the input string first before counting the score. 
#This would make the function have a log-linear time complexity. This means that the algorithm's running time 
#increases logarithmically with the size of the input, but with an additional factor. 
#The sorting operation changed the time complexity of the function.#



#Question 3  "Your order, please": #
#................................................. #

#Your task is to sort a given string. Each word in the string will contain a single number. This number is the position the word should have in the result.

#Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).
#If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers:
# "is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est" "4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople" ""  -->  "" 

# Answer: #

def order(sentence):
    if not sentence:
        return ""
    result = []    
      
    split_up = sentence.split() 
    for i in range(1,10):
        for item in split_up:
            if str(i) in item:
                 result.append(item)    
  
    return " ".join(result)


#Here is an example of Quadratic time complexity. 
#This means that the algorithm's running time increases quadratically with the size of the input.


def order(sentence):
    if not sentence:
        return ""
    result = []    

    split_up = sentence.split() 
    for i in range(1,10):
        for item in split_up:
            if str(i) in item:
                 result.append(item)    

    return " ".join(result)

#To make the function faster, the list is instead of a dictionary to store the words in the right order. 
#The function has a linear time complexity. 
#This means that the time it takes to run the function will increase at the same rate as the input size.

    