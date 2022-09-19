#W2D2 Demo-Cross Country Drive Solution

#Name Ex: Sara Paul
#Lab # Ex: Lab 1A

#PROGRAM PROMPT/ PURPOSE: determine cost of one and rountrip adventure across the USA

#VARIABLE DICTIONARY


#NOTES:

#MAIN CODE BELOW----------------------------------------------

#start by assigning known values or gathering needed values (input)
tolls= 23  #$
gallonGas= 1.8 #$
mpg= 32
hotels= 3
hotelNight= 120 #$
distance= 3158 #miles

#run required math processes/data manipulaion

totalGallons= distance/mpg

totalGasCost= totalGallons * gallonGas

hotelCost= hotels * hotelNight

oneway = totalGasCost + hotelCost + tolls

#display one way cost to user- Round to the 2nd!
#print ("One way cost: $", oneway)
print ("One way cost: $ {:.2f}".format(oneway))
#print (oneway)

roundtrip = oneway * 2

print ("Round trip cost: $ {:.2f}".format(roundtrip))