#pulls five years of BTS ontime zip files and stores locally

import urllib
import datetime

# global variables
now = datetime.datetime.now()
currentyear = now.year
currentmonth = now.month

# handle
testfile = urllib.URLopener()

def getBTSfiles(currentmonth, currentyear):
	"""function to pull five years of files but skip current and future months and months prior
	to five years to the month"""
	for y in range(currentyear - 5, currentyear):
		for m in range(1, 13):
			if (y == currentyear - 5) and (m < currentmonth):
				continue
			elif (y == currentyear) and (m >= currentmonth):
				continue
			else:
				testfile.retrieve(("http://www.transtats.bts.gov/Download/On_Time_On_Time_Performance_" + str(y) +"_" + str(m) + ".zip"), (str(m) + str(y) + ".zip"))
				
getBTSfiles(currentmonth, currentyear)
