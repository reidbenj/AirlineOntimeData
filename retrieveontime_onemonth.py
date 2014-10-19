#pulls one month (specified by user) of BTS ontime zip files and stores locally

import urllib

# prompt user for desired month and year
m = raw_input('Enter desired month (1-12):')
y = raw_input('Enter desired year (ex. 2014):')

# handle & pull
testfile = urllib.URLopener()
testfile.retrieve(("http://www.transtats.bts.gov/Download/On_Time_On_Time_Performance_" + str(y) +"_" + str(m) + ".zip"), (str(m) + str(y) + ".zip"))
				
