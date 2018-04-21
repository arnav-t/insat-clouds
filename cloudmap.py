import urllib.request
import time
import os

mapURL = 'http://satellite.imd.gov.in/img/3Dasiasec_bt1.jpg'
currDir = '/home/avz/Documents/py/insat/'

def saveMap(count):
	urllib.request.urlretrieve(mapURL, currDir+str(count) + '.jpg')

t = time.localtime()
curtime = time.strftime('%b-%d-%Y_%R:%S', t)

currentMap = 0

if os.stat(currDir + 'maps.log').st_size:
	with open(currDir + 'maps.log','r') as logfile:
		

saveMap(1)