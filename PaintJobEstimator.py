#Charlie Haynes
#Paint Job Estimator
#
#The most challenging part of this assignment was formatting the output. I needed help understanding how f-strings work, especially formatting currency and percentages. Once I saw how the syntax worked, I was able to correct my mistakes and get the output displaying properly.
#I also had some trouble understanding how to pass values between functions at first, but once I got the first function working, the others were much easier because they followed the same pattern.
#
#


import math

def calculateGallons(fltWallSquareFeet_CH, fltCoverage_CH):
    intGallons_CH = math.ceil(fltWallSquareFeet_CH / fltCoverage_CH)
    return intGallons_CH

def calculateLaborHours(intGallons_CH, fltLaborHoursPerGallon_CH):
    fltLabHrs_CH = intGallons_CH * fltLaborHoursPerGallon_CH
    return fltLabHrs_CH

def calculateLaborCharges(fltTotalLaborHours_CH, fltLaborChargeperHour_CH):
    fltTotalLabor_CH = fltLaborChargeperHour_CH * fltTotalLaborHours_CH
    return fltTotalLabor_CH

def calculatePaintCharges(intGallons_CH, fltPaintPrice_CH):
    fltTotalPaintCost_CH = intGallons_CH * fltPaintPrice_CH
    return fltTotalPaintCost_CH

def getSalesTax(strState_CH):
        if strState_CH == "CT":
            fltTaxRate_CH = 0.06
        elif strState_CH == "MA":
            fltTaxRate_CH = 0.0625
        elif strState_CH == "ME":
            fltTaxRate_CH = 0.085
        elif strState_CH == "NH":
            fltTaxRate_CH = 0.0
        elif strState_CH == "RI":
            fltTaxRate_CH = 0.07
        elif strState_CH == "VT":
            fltTaxRate_CH = 0.06
        else:
            fltTaxRate_CH = 0.0
        return fltTaxRate_CH
    
def calculateSalesTax(fltTotalPaintCost_CH, fltTaxRate_CH):
    fltSalesTax_CH = fltTotalPaintCost_CH * fltTaxRate_CH
    return fltSalesTax_CH
    
def getFloatInput(strPrompt_CH):
    while True:
        try:
            fltValue_CH = float(input(strPrompt_CH))
            if fltValue_CH <= 0:
                print("Number Must Be Greater Than Zero.")
                continue
            return fltValue_CH
        except ValueError:
            print("Please Enter a Number.")
            
def showCostEstimate(intGallons_CH, fltTotalLaborHours_CH, fltTotalLabor_CH,
                     fltTotalPaintCost_CH, fltTaxRate_CH, fltSalesTax_CH,
                     fltTotalCost_CH, strLastName_CH, strState_CH, strFileName_CH):
    print("Gallons needed:", intGallons_CH)
    print("Total labor hours:", fltTotalLaborHours_CH)
    print(f"Total labor charges: ${fltTotalLabor_CH:,.2f}")
    print(f"Total paint charges: ${fltTotalPaintCost_CH:,.2f}")
    print(f"Sales tax rate: {fltTaxRate_CH:.2%}")
    print(f"Sales tax amount: ${fltSalesTax_CH:,.2f}")
    print(f"Total job cost: ${fltTotalCost_CH:,.2f}")
    objFile_CH = open(strFileName_CH, "w")
    objFile_CH.write("Paint Job Estimate\n")
    objFile_CH.write("========================\n")
    objFile_CH.write(f"Customer: {strLastName_CH}\n")
    objFile_CH.write(f"State: {strState_CH}\n")
    objFile_CH.write("\n")
    objFile_CH.write(f"Gallons needed: {intGallons_CH}\n")
    objFile_CH.write(f"Total labor hours: {fltTotalLaborHours_CH:.2f}\n")
    objFile_CH.write(f"Total labor charges: ${fltTotalLabor_CH:,.2f}\n")
    objFile_CH.write(f"Total paint charges: ${fltTotalPaintCost_CH:,.2f}\n")
    objFile_CH.write(f"Sales tax rate: {fltTaxRate_CH:.2%}\n")
    objFile_CH.write(f"Sales tax amount: ${fltSalesTax_CH:,.2f}\n")
    objFile_CH.write("========================\n")
    objFile_CH.write(f"Total job cost: ${fltTotalCost_CH:,.2f}\n")
    objFile_CH.close()

def main():
    fltWallSquareFeet_CH = getFloatInput("Enter wall square footage: ")
    fltPaintPrice_CH = getFloatInput("Enter Paint Price per Gallon: ")
    fltCoverage_CH = getFloatInput("How many square feet does one gallon of paint cover: ")
    fltLaborHoursPerGallon_CH = getFloatInput("How many labor hours per gallon: ")
    fltLaborChargeperHour_CH = getFloatInput("How much is Labor per Hour: ")
    strState_CH = input("Enter state abbreviation: ").upper()
    strLastName_CH = input("Enter Customer Last Name: ")
    strFileName_CH = strLastName_CH + "_PaintJobOutput.txt"
    intGallons_CH = calculateGallons(fltWallSquareFeet_CH, fltCoverage_CH)
    fltTotalLaborHours_CH = calculateLaborHours(intGallons_CH, fltLaborHoursPerGallon_CH)
    fltTotalLabor_CH = calculateLaborCharges(fltTotalLaborHours_CH, fltLaborChargeperHour_CH)
    fltTotalPaintCost_CH = calculatePaintCharges(intGallons_CH, fltPaintPrice_CH)
    fltTaxRate_CH = getSalesTax(strState_CH)
    fltSalesTax_CH = calculateSalesTax(fltTotalPaintCost_CH, fltTaxRate_CH)
    fltTotalCost_CH = fltTotalLabor_CH + fltTotalPaintCost_CH + fltSalesTax_CH
    showCostEstimate(intGallons_CH, fltTotalLaborHours_CH, fltTotalLabor_CH,
                     fltTotalPaintCost_CH, fltTaxRate_CH, fltSalesTax_CH,
                     fltTotalCost_CH, strLastName_CH, strState_CH, strFileName_CH)
    
main()   







