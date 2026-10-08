#Name:Charlie Haynes
#Assignment: Planetary Weights
#Reflection:I've been doing a lot of work lately, and there was a goal to it, this didnt have that goal for me...
#           Its the spelling and repetition....copy past works, but its small pieces, i ended up writing most of it and having to go back and fix mistakes. save run oops...
#           I used 20s SPACES for the Name and 10.2f PLACES for the numbers including 2 decimal
#           1) Its about testing to get things to run correctly
#           2) Spelling Matters
#           3) Copy and paste can be your best friend AND worst enemy
MERCURY_WEIGHT_LOSS = 0.38
VENUS_WEIGHT_LOSS = 0.91
MOON_WEIGHT_LOSS = 0.165
MARS_WEIGHT_LOSS = 0.38
JUPITER_WEIGHT_GAIN = 2.34
SATURN_WEIGHT_LOSS = 0.93
URANUS_WEIGHT_LOSS = 0.92
NEPTUNE_WEIGHT_GAIN = 1.12
PLUTO_WEIGHT_LOSS = 0.066

sCustomersNameCH = input("What Is Your Name ?")
fStartingWeightCH = float(input("What Is Your Weight ?"))
fMercuryEndResultCH = fStartingWeightCH*MERCURY_WEIGHT_LOSS
fVenusEndResultCH = fStartingWeightCH*VENUS_WEIGHT_LOSS
fMoonEndResultCH = fStartingWeightCH*MOON_WEIGHT_LOSS
fMarsEndResultCH = fStartingWeightCH*MARS_WEIGHT_LOSS
fJupiterEndResultCH = fStartingWeightCH*JUPITER_WEIGHT_GAIN
fSaturnEndResultCH = fStartingWeightCH*SATURN_WEIGHT_LOSS
fUranusEndResultCH = fStartingWeightCH*URANUS_WEIGHT_LOSS
fNeptuneEndResultCH = fStartingWeightCH*NEPTUNE_WEIGHT_GAIN
fPlutoEndResultCH = fStartingWeightCH*PLUTO_WEIGHT_LOSS

print(sCustomersNameCH + ", here are your weights on our solar system's planets:")
print(format("Weight on Mercury:","20s"), format(fMercuryEndResultCH,"10.2f"))
print(format("Weight on Venus:","20s"), format(fVenusEndResultCH,"10.2f"))
print(format("Weight on our Moon:","20s"), format(fMoonEndResultCH,"10.2f"))
print(format("Weight on Mars:","20s"), format(fMarsEndResultCH,"10.2f"))
print(format("Weight on Jupiter:","20s"), format(fJupiterEndResultCH,"10.2f"))
print(format("Weight on Saturn:","20s"), format(fSaturnEndResultCH,"10.2f"))
print(format("Weight on Uranus:","20s"), format(fUranusEndResultCH,"10.2f"))
print(format("Weight on Neptune:","20s"), format(fNeptuneEndResultCH,"10.2f"))
print(format("Weight on Pluto:","20s"), format(fPlutoEndResultCH,"10.2f"))
