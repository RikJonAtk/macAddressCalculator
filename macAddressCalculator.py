"""
Provide a file called "macs.csv" in the same folder as this script.
The file should be a list of MAC addresses, one MAC address per line, and no column header.
MAC addresses should be the only thing in the file.  Eg,
    
macs.csv
d0:d3:e0:c1:97:48
de:ad:be:ef:ca:fe
c0:ff:ee:ca:fe:00

Run the script, and it will output a CSV file in the same location, called processedMacs.csv
Given the three MAC addresses shown above, processedMacs.csv will contain an output like this;

HW MAC, Base Radio MAC
d0:d3:e0:c1:97:48, d0:d3:e0:99:74:80
de:ad:be:ef:ca:fe, de:ad:be:7c:af:e0
c0:ff:ee:ca:fe:00, c0:ff:ee:2f:e0:00
"""

import csv

def getMacs():

    listOfMac = []
    
    with open('./macs.csv') as csvfile:
        thisFile = csv.reader(csvfile)
        for mac in thisFile:
            listOfMac.append(mac[0])
    
    return listOfMac


def calculateBaseRadioMac(mac):

    macStart = mac[:8]                      #Get first half of MAC address

    macEnd = mac[-7:].replace(":","")       #Get second half of MAC address and remove colons
    macEnd = int(macEnd,16)                 #Convert hex to dec
    macEnd = f"{macEnd:020b}"               #Convert dec to bin with zero-padding so it's 20 chars long
    macEnd = f"{macEnd}0000"                #Add four trailing zeros

    xorA = int("1000",2)                    #xorA = "1000" in binary / 8 in decimal
    xorB = int(macEnd[:4],2)                #xorB = First 4 binary digits of macEnd
    result = xorA ^ xorB                    #result = XOR(A,B)

    macEnd = f"{result:004b}{macEnd[4:]}"   #replace first 4 binary digits of macEnd with the XOR result
    macEnd = int(macEnd,2)                  #convert binary to decimal
    macEnd = f"{macEnd:x}"                  #convert decimal to hex

    finalMac = f"{macStart}:{macEnd[0]}{macEnd[1]}:{macEnd[2]}{macEnd[3]}:{macEnd[4]}{macEnd[5]}"

    return finalMac

if __name__ == "__main__":

    listOfMac = getMacs()

    with open('processedMacs.csv', 'w', newline='') as csvfile:
        macWriter = csv.writer(csvfile, delimiter=',')
        macWriter.writerow(["HW MAC", "Base Radio MAC"])
    
        for mac in listOfMac:
            baseMac = calculateBaseRadioMac(mac)
            macWriter.writerow([mac, baseMac])
