# Charlie Haynes
# Assignment: Temp Converter
# I Liked seeing the result of the conversion
# I struggled with indentation...again...got a syntax error
# if elif else, was needed to determin if F elif C or everything else
# 1)indentation, still learning it
# 2)if elif else ive never used or elif
# 3)or, is it this OR that

print("Charlie's Temp Converter")
fTempEnteredCH = float(input("Enter a temperature: "))
sTempForCCH = input("Is the temp F for Fahrenheit or C for Celsius? ")
if sTempForCCH == "F" or  sTempForCCH == "f":
    if fTempEnteredCH > 212:
        print("Temp can not be > 212")
    else:
        fCelsiusEqualCH = (5.0/9)*(fTempEnteredCH-32)
        print("The Celsius equivalent is:", format(fCelsiusEqualCH, ".1f"))

elif sTempForCCH == "C" or  sTempForCCH == "c":
    if fTempEnteredCH > 100:
        print("Temp can not be > 100")
    else:
        fFahrenheitEqualCH = (9.0/5)*(fTempEnteredCH)+32
        print("The Fahrenheit equivalent is:", format(fFahrenheitEqualCH, ".1f"))
else:
    print("You must enter a F or C")
