#!/usr/bin/python3

import requests
import time
import os
import moviepy.editor as mpy

from PIL import Image # imports image modulefrom Pillow 
from io import BytesIO

mapURL = 'http://satellite.imd.gov.in/img/3Dasiasec_bt1.jpg'
currDir = os.path.dirname(os.path.abspath('insat-clouds'))
fps = 2
gifName = 'animation.gif'

def saveMap(count):
	template = Image.open('celsius.jpg')
	response = requests.get(mapURL)
	img = Image.open(BytesIO(response.content))
	img.paste(template, (0, 1420))
	img.save(str(count) + '.jpg')
	
currentMap = 0

if os.stat(currDir + '/maps.log').st_size:
	with open(currDir + '/maps.log', 'r') as logfile:
		for line in logfile:
			pass
		currentMap = (int(line[-6]) + 1)%10

t = time.localtime()
currTime = time.strftime('%b-%d-%Y_%R:%S', t)

saveMap(currentMap)
with open(currDir + '/maps.log', 'a') as logfile:
	logfile.write(currTime + ' ' + str(currentMap) + '.jpg\n')

images = []
for i in range(10):
	images.append(currDir + '/' + str((currentMap - 9 + i)%10) + '.jpg')
clip = mpy.ImageSequenceClip(images, fps=fps)
clip.write_gif(currDir + gifName, fps=fps)
