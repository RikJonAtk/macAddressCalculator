# macAddressCalculator
I was trawling Twitter and saw that @JustDoWiFi (https://twitter.com/JustDoWiFi) was asking a question about how to use Excel to run through some MAC addresses and convert them to a different format.

The details of the request are here: https://twitter.com/JustDoWiFi/status/1559321186068090880?s=20&t=DyexyBV1VDWueRsI1r2lsQ

I don't have the Excel skills for this, but I do have some Python skills, so here's my Python-centric solution to the challenge.

The code is deliberately not condensed in any way as I wanted to make it super easy for anybody to be able to compare my code to the algorith described in Timothy's post.

# Usage
Download the "macAddressCalculator.py" Python script and provide a file called "macs.csv" in the same folder as where you put this script.

The macs.csv file should be a list of MAC addresses, one MAC address per line, and no column header. MAC addresses should be the only thing in the file and they must be colon delimeted.  Eg,

```
d0:d3:e0:c1:97:48
de:ad:be:ef:ca:fe
c0:ff:ee:ca:fe:00
```

Run the script and it will output a CSV file in the same location, called processedMacs.csv.  Given the three MAC addresses shown above, processedMacs.csv will contain an output like this;

```
HW MAC, Base Radio MAC
d0:d3:e0:c1:97:48, d0:d3:e0:99:74:80
de:ad:be:ef:ca:fe, de:ad:be:7c:af:e0
c0:ff:ee:ca:fe:00, c0:ff:ee:2f:e0:00
```

Examples of macs.csv and processedMacs.csv are included in the repository

# Testing
Tested on Windows 11 with Python v3.9.12

# Issues
No error handling of any kind.
Not extensively tested - use at your own peril.

#Feedback
Most welcome
