

# ! These below are my defined logic gates from AND, OR and XOR

# * AND logic gate
# Definition of an AND logic gate is both inputs need to be 1 for the output to be 1
# ! If one input is 0 then the output will be 0

def AND(A, B):
    return A & B


# * OR logic gate
# Definition of an OR logic gate is if one input is 1 the output will be 1
#! Only when both are 0 then the output will be 0

def OR(A, B):
    return A | B


# * XOR logic gate
# Definition of a XOR (Exclusively-OR) will output a logical 1 if either input are 1, but not the same (exclusively)
# ! Only when either A is one and B is 0 or vice versa will the output be one

def XOR(A, B):
    return A ^ B


# Validates info from user, creates a function to validate the correct input
def getInput():
    try:
        x = int(input("Please enter a number between 0 and 255 inclusive: "))
        if x in range(0, 256):
            return x
        else:
            print("Number out of range, number needs to be between 0 and 255.")
            return getInput()
    except ValueError:
        print("Variable must be an integer")
        return getInput()


# * numOne gets the first input added from getInput and stores it
inputOne = getInput()


# * numTwp gets the first input added from getInput and stores it
inputTwo = getInput()


print("\nThank you, please wait while I convert to binary format...." + "\nYou want to add: " +
      str(inputOne) + " and " + str(inputTwo) + "\nConverted to what's shown below:\n")


# * Converts to binary format
binaryOne = bin(inputOne)
binaryTwo = bin(inputTwo)


# * Convert to list
# * removes the 0b from the binary format / starts from second index
binaryListOne = list(binaryOne[2:].zfill(8))
binaryListTwo = list(binaryTwo[2:].zfill(8))

# Converts input into string to show user the inputs provided to add
print("Input A: " + str(binaryListOne))
print("Input B: " + str(binaryListTwo))


# *? half adder / why is this here? Do I need?
# def half_adder(upper, lower):
#     a = XOR(a,b) #gives sum
#     b = AND(a,b) #gives carry
#     return (a, b)


# * fullBitAdder
def fullBitAdder(upper, lower, carryIn):
    output1 = AND(upper, lower)
    output2 = XOR(upper, lower)
    output3 = AND(output2, carryIn)
    sum = XOR(output2, carryIn)
    carryOut = OR(output1, output3)
    return sum, carryOut


# * Addition of two binary numbers
addList = []
i = 7
carryIn = 0
while i >= 0:
    sum, carryOut = fullBitAdder(
        int(binaryListOne[i]), int(binaryListTwo[i]), carryIn)
    addList.append(sum)
    carryIn = carryOut
    i -= 1

#! test print
addList.reverse()
#! If number inputted is bigger than 256 then it will still be correct in binary
addList.insert(0, carryOut)
print("\nThe sum of the two inputs is: " + str(addList))

print("Thank you for using the program, have a good day.")

# print("Enter first binary number")
# n = input()
# print("Enter second binary number")
# m = input()

# s = bin(int(n, 2)-int(m, 2))
# print("Subtraction of two binary number is - "+s)


#! REPORT

#! psudocode : def = it does something
#! you take input
#! validate the input against conditions 0 - 255 PROCESS STAGE
#! DATA STRUCTURES
#! how you are implementing your data and storing it
#! look at IPO pattern
#! diagrams as well to explain program

"""data structures talk about what you used, lists, while loops, mostly interested in data types and structures, int to binary
1500 words, separate file, apendex opy paste, don't really need the entire screenshot

Algorithm - Speak in normal english about your functions how the program works and what it does 
EX.
"create a function that takes in two inputs from the user and returns the sum of the two inputs"
"Pass these two inputs into the function and return the sum"
... talk about your code and what it does...

psudocode less wordy

110 to 50 people in course now
"""
