#Name:Charlie Haynes
#Assignment:Compound Interest
#Reflection: I know this is fun sometimes, I think its just a bad day for me to be coding, cause im only coming up with negativity here
#            Honestly this was easier than the weight loss one
#            for things to be done in the right order (you use) parentheses
#            start by looking at the sample before you make your names
#            it can take very little code to make a powerfull tool
#            ** raised to the power of


fStartingPrincipalCH = float(input("Enter the starting principal: "))
fAnnualInterestRateCH = float(input("Enter the annual interest rate: "))
iCompoundedCH = int(input("How many times per year is the interest compounded? "))
iYearsCH = int(input("For how many years will the account earn interest? "))

fConvertedInterestRateCH = fAnnualInterestRateCH/100

fFutureValueCH = fStartingPrincipalCH*(1+fConvertedInterestRateCH/iCompoundedCH)**(iCompoundedCH*iYearsCH)

print("At the end of",(iYearsCH),"years you will have $",(format(fFutureValueCH,",.2f")))

