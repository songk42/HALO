#!/bin/python3

import time, math, picamera

# time.ctime() gives something like "Sat Jun 29 02:27:50 2019"

# what will be sent to the log
# "{} {} {} [...]".format(time.ctime(), temp, alt, [...])... well the result of this

# do the sensors write up data into separate files? if so then i'll have to read in a bunch of files :|

# honestly a lot of this is going to depend on exactly what hardware we're using

# account for possibly not receiving data from a sensor - just repeat the last entry or say N/A or something like that?

alt = lambda p: (10**(math.log10(p/1013.25) + 6) - 1) / 6.8755856 * -1 # where p is in hPa

while True:
	# code?
	# better condition for while loop?
	# read data from their respective sensors
	# write data to some file
	time.sleep(30) # not actually sure how often I should collect data

# temperature sensor outputs data in w1_slave file - does it keep all data or just the last recorded data?
# assuming the second:
tempData = open("w1_slave", "r") # add path to file name
lines = tempData.readLines()
while lines[0].strip()[-3:] != "YES":
	lines = tempData.readLines()
temp = float(lines[1][lines[1].find("t=")+2:])/1000 # Celsius


# camera

cam = picamera.PiCamera()
while True:
    time.sleep(60)
    cam.capture("IMG_" + time.strftime("%H%M%S", time.localtime()) + ".jpg") # localtime or gmtime?
    # hm change capture rate based on altitude? (like at a certain point the view each minute will not change all too much)
