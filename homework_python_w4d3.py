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

# Solution 1

def cube(volume, side):
    for i in range(side):
        if i**3 == volume:
            return True
    return False

# This code checks if any number from 0 to side-1 when cubed is equal to volume. If such a number is found, it returns True.
#If no such number is found, it returns False. This code takes longer to run as side becomes larger and function "cube" has linear time complexity.

#..............

# Solution 2 (improved)

def cube (volume, side):
    return 0 < volume == side**3

#This "cube" function is very fast because it does a quick check to see if the volume matches the cube's dimensions,
# and it can do this for any input values without slowing down. 
# The function has a constant time complexity and only performs two single operations. 


# Question 2 
# ................................................. #
# There is a war and nobody knows - the alphabet war!
#There are two groups of hostile letters. The tension between left side letters and right side letters was too high and the war began.

#Task
#Write a function that accepts fight string consists of only small letters and return who wins the fight. When the left side wins return Left side wins!, when the right side wins return Right side wins!, in other case return Let's fight again!.

#The left side letters and their power:

 #w - 4
 #p - 3
 #b - 2
 #s - 1
#The right side letters and their power:

# m - 4
# q - 3
# d - 2
# z - 1
#The other letters don't have power and are only victims.

#Example
#AlphabetWar("z")
#//= > Right side wins!
#AlphabetWar("zdqmwpbs")
#//= > Let's fight again!
#AlphabetWar("zzzzs")
#//= > Right side wins!
#AlphabetWar("wwwwwwz")
#//= > Left side wins!

# Answer: #

# Solution 1

def alphabet_war(fight):
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

    # The time complexity of the function alphabet_war is linear,  O(n), where n represents the length of the input fight string.

#solution 2


def alphabet_war(fight):
    left_side_score = 0
    right_side_score = 0
    for ch in fight:
        if ch == "w":
            left_side_score += 4
        elif ch == "p":
            left_side_score += 3
        elif ch == "b":
            left_side_score += 2
        elif ch == "s":
            left_side_score += 1
        elif ch == "m":
            right_side_score += 4
        elif ch == "q":
            right_side_score += 3
        elif ch == "d":
            right_side_score += 2
        elif ch == "z":
            right_side_score += 1

    if left_side_score > right_side_score:
        return "Left side wins!"
    elif right_side_score > left_side_score:
        return "Right side wins!"
    else:
        return "Let's fight again!"
    
    #In the simplified solution 2, we keep track of the scores for the left and right sides using separate variables. We iterate through the fight string and update the scores accordingly based on the individual characters. This implementation maintains a linear time complexity.
    # O(n)

# Question 3 "Equal Sides Of An Array":
#................................................. #

    # You are going to be given an array of integers. Your job is to take that array and find an index N where the sum of the integers to the left of N is equal to the sum of the integers to the right of N. If there is no index that would make this happen, return -1.

#For example:

#Let's say you are given the array {1, 2, 3, 4, 3, 2, 1}:
#Your function will return the index 3, because at the 3rd position of the array, the sum of left side of the index({1, 2, 3}) and the sum of the right side of the index({3, 2, 1}) both equal 6.

#Let's look at another one.
#You are given the array {1, 100, 50, -51, 1, 1}:
#Your function will return the index 1, because at the 1st position of the array, the sum of left side of the index({1}) and the sum of the right side of the index({50, -51, 1, 1}) both equal 1.

#Last one:
#You are given the array {20, 10, -80, 10, 10, 15, 35}
#At index 0 the left side is {}
#The right side is {10, -80, 10, 10, 15, 35}
#They both are equal to 0 when added. (Empty arrays are equal to 0 in this problem)
#Index 0 is the place where the left side and right side are equal.

#Note: Please remember that in most programming/scripting languages the index of an array starts at 0.

#Input:
#An integer array of length 0 < arr < 1000. The numbers in the array can be any integer positive or negative.

#Output:
#The lowest index N where the side to the left of N is equal to the side to the right of N. If you do not find an index that fits these rules, then you will return -1.

#Note:
#If you are given an array with multiple answers, return the lowest correct index.

#Solution 1

def find_even_index_1(arr):
    for index, num in enumerate(arr):
        if sum(arr[:index]) == sum(arr[index+1:]):
            return index
    return -1

# The function checks each index of the array one by one. For each index, it calculates the sum of the numbers before that index and the sum of the numbers after that index. To calculate these sums, it creates new arrays by slicing the original array. Each slicing operation takes time proportional to the length of the array (O(N)). Since these slicing operations are performed for each index in a loop that iterates N times, the overall time complexity becomes quadratic (O(N^2)), which means the time taken increases rapidly as the size of the array grows.

# ..............


#Solution 2 (impproved)

def find_even_index_2(arr):
    total_sum = sum(arr)
    left_sum = 0
    for index, num in enumerate(arr):
        if left_sum == total_sum - left_sum - num:
            return index
        left_sum += num
    return -1

# The improved version achieves a linear time complexity of O(N), where N is the length of the input arr. This is because it iterates over the array only once, performing constant time operations (such as addition and comparison) for each element. The sum of the array is calculated once in the beginning, and the left sum is updated incrementally in each iteration. As a result, the time taken increases linearly with the size of the array.



    