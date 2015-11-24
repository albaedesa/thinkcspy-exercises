# Chapter 2 Exercises

# Question 3

current_time_string = input("What is the current time (in hours)? ")
waiting_time_string = input("How many hours do you have to wait? ")

current_time_int = int(current_time_string)
waiting_time_int = int(waiting_time_string)

hours = current_time_int + waiting_time_int

timeofday = hours % 24

print(timeofday)

# Question 4

startday_string = input("What is the starting day number?")
lengthOfstay_string = input("What is the length of your stay?")

startday_int = int(startday_string)
lengthOfstay_int = int(lengthOfstay_string)

days = startday_int + lengthOfstay_int

num_of_day = days % 6

print(num_of_day)

# Question 5

word1 = "All"
word2 = "work"
word3 = "and"
word4 = "no"
word5 = "play"
word6 = "makes"
word7 = "Jack"
word8 = "a"
word9 = "dull"
word10 = "boy."

print(word1, word2, word3, word4, word5, word6, word7, word8, word9, word10)

# Question 6

print(6 * (1 -2)) #make it print -6 by adding parenthesis

# Question 7

P = 10000
n = 12
r = .08
t = input("What is the number of years?")
t = int(t)

interest = P * ((1 + r/n)**(n*t)) #sketchy math...

print("The interest is", interest)

# Question 8

radius = int(input("What is the radius?")) #you can also do this on two separate lines

area = 3.14 * (radius**2)

print("This is your nice answer:", area)

# Question 9

width = int(input("What is the width of the rectangle, yo?"))
height = int(input("What is the height of the rectangle, dude?"))

area = width * height

print("The area is", area)

# Question 10

miles_driven = int(input("What is the number of miles driven?"))
gallons_used = int(input("What is the number of gallons?")) 

MPG = miles_driven / gallons_used

print("Miles per gallon is", MPG)

# Question 11

degreesC = int(input("What is the degrees in celsius?"))

degreesF = (degreesC * (9/5)) + 32

print("The degrees farenheit are", degreesF)

# Question 12

degreesF = int(input("What is the degrees in farenheit?"))

degreesC = (degreesF - 32) * (5/9)

print("The degrees celsius are", degreesC)