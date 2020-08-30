# I, Meet Patel, student number 000794612, certify that all code submitted
# is my own work; that I have not copied it from any other source.
# I also certify that I have not allowed my work to be copied by others.

provList = ("AB", "BC", "MB", "NB", "NL", "NT", "NS", "NU", "ON", "PE", "QC", "SK", "YT")

#function to validate postal code
def postalCodeOk( postalCode ):
    flag = True
    if len( postalCode ) == 6:
        flag = postalCode[ 0 ].isalpha() and postalCode[ 1 ].isdecimal() and postalCode[ 2 ].isalpha() and postalCode[ 3 ].isdecimal() and postalCode[ 4 ].isalpha() and postalCode[ 5 ].isdecimal() 
    elif len( postalCode ) == 7:
        flag = postalCode[ 0 ].isalpha() and postalCode[ 1 ].isdecimal() and postalCode[ 2 ].isalpha() and postalCode[ 3 ].isspace() and postalCode[ 4 ].isdecimal() and postalCode[ 5 ].isalpha() and postalCode[ 6 ].isdecimal()
    else:
        flag = False
    return flag
    
def validate( prov, b ):
    flag = True
    if prov == "AB":
        if not postalCode[0] == "T":
            flag = False
    if prov == "BC":
        if not postalCode[0] == "V":
            flag = False
    if prov == "MB":
        if not postalCode[0] == "R":
            flag = False
    if prov == "NB":
        if not postalCode[0] == "E":
            flag = False
    if prov == "NL":
        if not postalCode[0] == "A":
            flag = False
    if prov == "NT":
        if not postalCode[0] == "X":
            flag = False
    if prov == "NS":
        if not postalCode[0] == "B":
            flag = False
    if prov == "NU":
        if not postalCode[0] == "X":
            flag = False
    if prov == "ON":
        if not ( postalCode[0] == "K" or postalCode[0] == "L" or postalCode[0] == "M" or postalCode[0] == "N" or postalCode[0] == "P" ):
            flag = False
    if prov == "PE":
        if not postalCode[0] == "C":
            flag = False
    if prov == "QC":
        if not ( postalCode[0] == "G" or postalCode[0] == "H" or postalCode[0] == "J" ):
            flag = False
    if prov == "SK":
        if not postalCode[0] == "S":
            flag = False
    if prov == "YT":
        if not postalCode[0] == "Y":
            flag = False
    return flag

#streetNum : Street number of the user
streetNum = input("Please, enter your street number: ")


#while loop to check whether the street number is valid or not
while not streetNum.isdecimal():
    print("Please enter a valid street number! i.e 12 or 123 ")
    streetNum = input("Please, enter your street number: ")

    
#streetName : Street number of the user
streetName = input("Please, enter your street name: ")
#while loop to validate streetb number whether it is valid or not
while not ( len(streetName) >= 6 ):
    print("Please enter a valid street number! i.e. hamilton (6 character or more)")
    streetName = input("Please, enter your street name: ")
streetName = streetName.title()

    
#city : name of the city
city = input("Please, enter your city name: ")
city = city.capitalize()

 
#prov : name of the province
prov = input("Please, enter your province name: ")

#while loop to check province whether it is valid or not
while prov.upper() not in provList:
    print("Please enter a valid province name i.e. on or On (just abbreviation) ")
    prov = input("Please, enter your province name: ")

prov = prov.upper()
#postalCode : postal code of the user's location
postalCode = input("Please, enter a postal code: ")
#while loop to check 
while not postalCodeOk( postalCode ):
    print("Please enter a valid postal code i.e. n1h 2m5 or n1h2m5 ")
    postalCode = input("Please, enter a valid postal code: ")
postalCode = postalCode.upper()
b = postalCode[0]

if len( postalCode ) == 6:
        postalCode = postalCode[0:3] + " " + postalCode[3:6]

while not validate ( prov, b ):
    print("Either of your province or postal code does not match please enter properly! you entered " + prov + " for province and " + str(postalCode) + " for postal code.")
    prov = input("Please, enter your province name i.e. on or On (just abbreviation): ")
    prov = prov.upper()
    while prov not in provList:
        print("Please enter a valid province name i.e. on or ON ")
        prov = input("Please, enter your province name i.e. on or On (just abbreviation): ")

    postalCode = input("Please, enter a postal code: ")
    
    while not postalCodeOk( postalCode ):
        print("Please enter a valid postal code i.e. n1h 2m5 or n1h2m5 ")
        postalCode = input("Please, enter a valid postal code: ")
    postalCode = postalCode.upper()
    b = postalCode[0]
    if len( postalCode ) == 6:
        postalCode = postalCode[0:3] + " " + postalCode[3:6]

        
if ( prov == "AB" or prov == "BC" or prov == "MB" or prov == "SK" ):
    cost = 12
if ( prov == "NM" or prov == "NL" or prov == "NS" or prov == "PE" ):
    cost = 15
if ( prov == "NT" or prov == "NU" or prov == "YK" ):
    cost = 20
if ( prov == "ON" or prov == "QC" ):
    cost = 8

print( "Shipping to " + str(streetNum) + " " + str(streetName) + ", " + str(city) + ", " + str(prov) + " - " + str(postalCode) + " will cost $" + str(cost) + "." )
