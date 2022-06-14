from astropy.io import fits
from astropy.table import Table
from astropy.time import Time


fileLocation = '/home/quadblast24/PythonPrograms/sw00049929013uuu_sk.img'
with fits.open(fileLocation) as hdu:
    l = len(hdu)
    print('Checking ' + str(l-1) + ' extensions.')
    for i in range(l):
        if i>0:
            print(str(i)+' ASPCORR = ' +str(hdu[i].header['ASPCORR']))
        if i>1 and hdu[i].header['ASPCORR'] == 'NONE' and hdu[i-1].header['ASPCORR'] == 'DIRECT':
            diff = (Time(hdu[i].header['DATE-OBS']).jd-
                  Time(hdu[i-1].header['DATE-OBS']).jd)*24*60
            print('Time difference (minutes) = ' +str(diff))
            if diff < 60:
                print('CDELT1/2 of '+str(i)+' replaced with CDELT1/2 of '+str(i-1))
                fits.setval(fileLocation, 'CDELT1', value = hdu[i-1].header['CDELT1'], ext=i)
                #print(str(hdu[i].header['CDELT1']) + ' changed to ' + str(hdu[i-1].header['CDELT1']))
                fits.setval(fileLocation, 'CDELT2', value = hdu[i-1].header['CDELT2'], ext=i)
                #print(str(hdu[i].header['CDELT2']) + ' changed to ' + str(hdu[i-1].header['CDELT2']))
                
                
    