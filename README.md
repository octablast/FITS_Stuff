# FITS_Stuff
script1.py traverses extensions and checks if their 'ASPCORR' atrribute is 'NONE' and the extension before [i-1] has an 'ASPCORR' of 'DIRECT'. If this is true and the time difference in 'DATE-OBS' is less than 60 minutes, then 'CDELT1' of [i] = 'CDELT1' of [i-1] and 'CDELT2' of [i] = 'CDELT2' of [i-1]
