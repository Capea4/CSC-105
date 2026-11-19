#Charlie Haynes
#Compound Interest Loops
#1. I liked how the program automatically calculated the number of months needed to reach the savings goal. The loop stopped on its own once the goal was reached without needing to specify how many times it should run.
#2. My biggest struggle with this assignment was finding the time to complete it while balancing work and my other classes.
#3. Both for and while loops repeat code. A for loop is useful when the number of repetitions is known, while a while loop is useful when the number is unknown and the loop continues until a condition is met.
#4. I used a for loop to display the monthly balances because the number of months was known. I used a while loop for the savings goal because I didn't know how many months it would take to reach it. I also used while loops for input validation.
#5. I used 5 while loops and 1 for loop
#6. Three things I learned from this assignment:
#       1. When to use a for loop versus a while loop.
#       2. How to format numeric output with commas and decimal places.
#       3. How testing can reveal misleading error messages, even when the code itself works correctly.



# Get and validate the original deposit
while True:
    try:
        fltDeposit_CH = float(input("What is the Original Deposit (positive value): "))
        if fltDeposit_CH <= 0:
            print("Number Must Be Greater Than Zero.")
        else:
            break
    except ValueError:
        print("Please Enter a Number.")
        
# Get and validate the annual interest rate
while True:
    try:
        fltInterestRate_CH = float(input("What is the Interest Rate (positive value): "))
        if fltInterestRate_CH <= 0:
            print("Number Must Be Greater Than Zero.")
        else:
            break
    except ValueError:
        print("Please Enter a Number.")
        
# Get and validate the number of months..I changed the error message to my liking here...
while True:
    try:
        intMonths_CH = int(input("What is the Number of Months (positive value): "))
        if intMonths_CH <= 0:
            print("Number Must Be Greater Than Zero.")
        else:
            break
    except ValueError:
        print("Please Enter a Whole Number of Months.")
        

# Get and validate the savings goal
while True:
    try:
        fltSavingsGoal_CH = float(input("What is the Goal Amount (can enter 0 but not negative): "))
        if fltSavingsGoal_CH < 0:
            print("Number Cannot Be Negative.")
        else:
            break
    except ValueError:
        print("Please Enter a Number.")


# Calculate the monthly interest rate
fltMonthlyRate_CH = fltInterestRate_CH / 100 / 12
fltBalance_CH = fltDeposit_CH       

# Calculate and display monthly balances...BTW i realised i had wrong indentation here, but python still runs it, so I left it to make it more personal to me...its my mistake but it still works sooo...
for intMonth_CH in range(1, intMonths_CH + 1):
        fltBalance_CH = fltBalance_CH + (fltBalance_CH * fltMonthlyRate_CH)
        print(f"Month {intMonth_CH}: ${fltBalance_CH:,.2f}")

# Reset balance and month counter
fltBalance_CH = fltDeposit_CH
intGoalMonths_CH = 0

# Calculate months needed to reach savings goal
while fltBalance_CH < fltSavingsGoal_CH:
    fltBalance_CH = fltBalance_CH + (fltBalance_CH * fltMonthlyRate_CH)
    intGoalMonths_CH = intGoalMonths_CH + 1

# Display savings goal results if a goal was entered
if fltSavingsGoal_CH > 0:
    print(f"It will take {intGoalMonths_CH:,} months to reach your goal of ${fltSavingsGoal_CH:,.2f}.")
