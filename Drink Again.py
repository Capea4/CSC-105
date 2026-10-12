# Charlie Haynes
# Drink again

iBottlesCH = 0

while iBottlesCH <= 0:
    try:
        iBottlesCH  = int(input("How many bottles of root beer? : "))

    except ValueError:
        print("Root Beer Only No Hard Stuff.")
        continue

    if iBottlesCH <= 0 :
        print ("Please Add More Root Beer")


while iBottlesCH >= 1:
    
    
    if iBottlesCH == 1 :
        print(f"{iBottlesCH} bottle of root beer on the wall")
        print(f"{iBottlesCH} bottle of root beer")
    else:
        print(f"{iBottlesCH} bottles of root beer on the wall")
        print(f"{iBottlesCH} bottles of root beer")
        
    print("take one down pass it around")
    
    iBottlesCH -= 1
    if iBottlesCH == 1:
        print(f"{iBottlesCH} bottle of root beer on the wall\n")
    
    elif iBottlesCH > 1:
        print(f"{iBottlesCH} bottles of root beer on the wall\n")


print("0 bottles of root beer on the wall")
print("WE'RE GONNA NEED AN UBER")
