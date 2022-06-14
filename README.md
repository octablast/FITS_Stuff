# FITS_Stuff
script1.py traverses extensions and checks if their 'ASPCORR' atrribute is 'NONE' and the extension before [i-1] has an 'ASPCORR' of 'DIRECT'. If this is true and the time difference in 'DATE-OBS' is less than 60 minutes, then 'CRVAL1' of [i] = 'CRVAL1' of [i-1] and 'CRVAL2' of [i] = 'CRVAL2' of [i-1]
