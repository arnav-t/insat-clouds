# insat-clouds
![Python](https://img.shields.io/badge/Made%20with-Python-blue.svg) 
![Gitter](https://img.shields.io/gitter/room/:user/:repo.svg)
     
Generate animated GIFs from INSAT cloud cover maps for the past five hours

## Purpose 
The INSAT website only provides a single image for the latest cloud cover data. Unfortunately, it lacks a history feature which means it is not possible to observe the cloud trajectories in real time.    
![map](http://satellite.imd.gov.in/img/3Dasiasec_bt1.jpg "INSAT Map")
Fortunately, this problem can be overcome quite easily.      

## Working  
A `cron` job is scheduled to execute this script every 30 minutes (the usual update rate of the INSAT satellite) to download a new, updated cloud cover map. This new image will overwrite any maps older than 5 hours. 
A GIF is now generated using MoviePy from the past 10 images (last 5 hours).   

## Running locally
1. `git clone https://github.com/arnav-t/insat-clouds.git`
2. `cd insat-clouds`
3. `pipenv shell --three`
4. `pipenv install` (Only the first time)
5. `python3 cloudmap.py`

## Usage
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

## Dependencies 
* MoviePy 
## Communication
[Gitter](https://gitter.im/INSAT-CloudsChat/Lobby)
