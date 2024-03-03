# Amanda M
# 1/31/2024
# Chapter 6 Programming Exercises

def main():
    test1 = float(input('Enter the score for test 1: '))
    test2 = float(input('Enter the score for test 2: '))
    test3=  float(input('Enter the score for test 3: '))
    test4=  float(input('Enter the score for test 4: '))
    test5=  float(input('Enter the score for test 5: '))

    # Determine the Grade
    if  test1 >= 90:
        print('Congratulations! You earned an A.')
    elif test1 >= 80:
        print('Congratulations! You earned a B.')
    elif test1 >= 70:
        print('You earned a C.')
    elif test1 >= 60:
        print('You earned a D.')
    elif test1 < 60:
        print('You failed the test.')
    else:
        print('Invalid entry. Please input test score')
    
    # Calculating the Average
    def sharp():
        sharp = "Y"
        sharp = input("Continue onto the averages? Y or N ")
        if sharp == "Y":
            average = (test1 + test2 + test3 + test4 + test5) / 5.0
            return(print(f"The average score is {average}."))
        else:
            quit
    sharp()

# Repetition Cycle 
keepGoing = "y"            
def loop():
    keepGoing = "y"
    while keepGoing == "y":
        keepGoing = input("Would you like to use the dule again? y or N ")
        if keepGoing == "y":
            main()
        else:
            print("Have a good day!")

main()
loop()
