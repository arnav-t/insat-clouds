import urllib.request
import time
import os

mapURL = 'http://satellite.imd.gov.in/img/3Dasiasec_bt1.jpg'
currDir = '/home/avz/Documents/py/insat/'

def saveMap(count):
	urllib.request.urlretrieve(mapURL, currDir + str(count) + '.jpg')

currentMap = 0

if os.stat(currDir + 'maps.log').st_size:
	with open(currDir + 'maps.log', 'r') as logfile:
		for line in logfile:
			pass
		currentMap = (int(line[-6]) + 1)%10

t = time.localtime()
currTime = time.strftime('%b-%d-%Y_%R:%S', t)

saveMap(currentMap)
with open(currDir + 'maps.log', 'a') as logfile:
	logfile.write(currTime + ' ' + str(currentMap) + '.jpg\n')

