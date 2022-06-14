from astropy.io import fits
from astropy.table import Table
from astropy.time import Time
import sys
import os

def access(fileLocation):
    with fits.open(fileLocation) as hdu:
        print(' Found file: %s' % (fileLocation))
        l = len(hdu)
        print(' Checking ' + str(l-1) + ' extensions:')
        for i in range(l):
            if i>0:
                print('  '+str(i)+' ASPCORR = ' +str(hdu[i].header['ASPCORR']))
            if i>1 and hdu[i].header['ASPCORR'] == 'NONE' and hdu[i-1].header['ASPCORR'] == 'DIRECT':
                diff = (Time(hdu[i].header['DATE-OBS']).jd-
                      Time(hdu[i-1].header['DATE-OBS']).jd)*24*60
                print('    Time difference (minutes) = ' +str(diff))
                if diff < 60:
                    print('    CRVAL1/2 of '+str(i)+' replaced with CRVAL1/2 of '+str(i-1))
                    fits.setval(fileLocation, 'CRVAL1', value = hdu[i-1].header['CRVAL1'], ext=i)
                    #print(str(hdu[i].header['CRVAL1']) + ' changed to ' + str(hdu[i-1].header['CRVAL1']))
                    fits.setval(fileLocation, 'CRVAL2', value = hdu[i-1].header['CRVAL2'], ext=i)
                    #print(str(hdu[i].header['CRVAL2']) + ' changed to ' + str(hdu[i-1].header['CRVAL2']))
                else:
                    print('----!! Time Difference Too Big!')
            else:
                if i>1 and hdu[i].header['ASPCORR'] == 'NONE' and hdu[i-1].header['ASPCORR'] != 'DIRECT':
                    print('---!! ASPCORR = DIRECT not avaliable')
try:
    fileLocation = sys.argv[1] #'/home/quadblast24/PythonPrograms/sw00049929013uuu_sk.img'
    print('Checking file or directory: %s' %fileLocation)
except IndexError:
    print('No file or directory location defined!')
try:
    access(fileLocation)
except FileNotFoundError:
    print('The file or path specified is not correct')
except NameError:
    print('Please enter a valid file or directory location')
except IsADirectoryError:
    for dirName, subdirList, fileList in os.walk(fileLocation, topdown=False):
        for sdName in subdirList:
            if sdName == 'image':
                print('Attempting to read: '+dirName+'/'+sdName)
                for dirName, subdirList, fileList in os.walk(dirName+'/'+sdName, topdown=False):
                    for fName in fileList: 
                        try:
                            if fName[-9:-7] == 'sk': 
                                access(dirName+'/'+fName)
                        except FileNotFoundError:
                            print('The file or path specified is not correct')
                        except OSError:
                            print('   ^--This does not appear to be a valid FITS file.')
except OSError:
    print('   ^--This does not appear to be a valid FITS file.')
exit