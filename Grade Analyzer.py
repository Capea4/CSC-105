# Charlie Haynes
# Grade Analyzer
# I liked adding the Possesive 'S to the name even though it wasnt requested
# I struggled with figuring out how to compute 3 test (Y) or 4 tests (N)
# I compared each test result using "and" and with a <= to each other tests. (1) if (2) elif and (1) else
# (1) Tab again...its soo damn important..indents failed several times (learn the same lesson till its perminant?)
# (2) , adds a space in print + doesnt...its what i struggled with when adding the 's to the name
# (3) Spelling tings the same over and over...another lesson learned every task

sEnterNameCH = input("Name of person we are calculating the grade for: ")
iTestoneCH = int(input("Test 1: "))
iTesttwoCH = int(input("Test 2: "))
iTestthreeCH = int(input("Test 3: "))
iTestfourCH = int(input("Test 4: "))

sDropGradeCH = input("Do you wish to drop the lowest grade Y or N: ")

if iTestoneCH < 0 or iTesttwoCH < 0 or iTestthreeCH < 0 or iTestfourCH < 0:
    print ("Test scores must be greater than 0")
    exit()

if sDropGradeCH != "Y" and sDropGradeCH != "N":
    print("Enter Y or N to Drop the Lowest Grade")
    exit()

if sDropGradeCH == "Y":
    
    iThreeorFourCH = 3 
    
    if iTestoneCH <= iTesttwoCH and iTestoneCH <= iTestthreeCH and iTestoneCH <= iTestfourCH:
        iLowestscoreCH = iTestoneCH

    elif iTesttwoCH <= iTestoneCH and iTesttwoCH <= iTestthreeCH and iTesttwoCH <= iTestfourCH:
        iLowestscoreCH = iTesttwoCH

    elif iTestthreeCH <= iTestoneCH and iTestthreeCH <= iTesttwoCH and iTestthreeCH <= iTestfourCH:
        iLowestscoreCH = iTestthreeCH

    else:
        iLowestscoreCH= iTestfourCH

if sDropGradeCH == "N":

    iThreeorFourCH = 4

    iLowestscoreCH = 0


fGradeMathCH = (iTestoneCH + iTesttwoCH + iTestthreeCH + iTestfourCH - iLowestscoreCH) / iThreeorFourCH

if fGradeMathCH >= 97.0:
        sFinalGradeCH = "A+"
elif fGradeMathCH >= 94.0:
        sFinalGradeCH = "A"
elif fGradeMathCH >= 90.0:
        sFinalGradeCH = "A-"
elif  fGradeMathCH >= 87.0:
        sFinalGradeCH = "B+"
elif  fGradeMathCH >= 84.0:
        sFinalGradeCH = "B"
elif  fGradeMathCH >= 80.0:
        sFinalGradeCH = "B-"
elif  fGradeMathCH >= 77.0:
        sFinalGradeCH = "C+"
elif  fGradeMathCH >= 74.0:
        sFinalGradeCH = "C"
elif  fGradeMathCH >= 70.0:
        sFinalGradeCH = "C-"
elif  fGradeMathCH >= 67.0:
        sFinalGradeCH = "D+"
elif  fGradeMathCH >= 64.0:
        sFinalGradeCH = "D"
elif  fGradeMathCH >= 60.0:
        sFinalGradeCH = "D-"
else:
        sFinalGradeCH = "F"


print (sEnterNameCH + "'s test average is" ,format(fGradeMathCH, ".1f"))
print ("Letter Grade for the test is: " ,sFinalGradeCH)
