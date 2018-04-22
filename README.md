# insat-clouds
## Generate animated GIFs from INSAT cloud cover maps for the past five hours

### Purpose 
The INSAT website only provides a single image for the latest cloud cover data. Unfortunately, it lacks a history feature which means it is not possible to observe the cloud trajectories in real time.    
![map](http://satellite.imd.gov.in/img/3Dasiasec_bt1.jpg "INSAT Map")
Fortunately, this problem can be overcome quite easily.      
![animation](https://github.com/arnav-t/insat-clouds/blob/master/22-04-2018_1330.gif?raw=true "Animated GIF")
### Working  
A `cron` job is scheduled to execute this script every 30 minutes (the usual update rate of the INSAT satellite) to download a new, updated cloud cover map. This new image will overwrite any maps older than 5 hours. 
A GIF is now generated using MoviePy from the past 10 images (last 5 hours).   

### Usage
A `cron` job must be scheduled to run the script every five hours.
```
chmod 755 cloudmap.py
crontab -e
```
The following line must be added (the path may differ).
```
*/30 * * * * /home/avz/Documents/py/insat/cloudmap.py
```
Now, every 30 minutes, the GIF will be updated.

### Dependencies 
* MoviePy 
