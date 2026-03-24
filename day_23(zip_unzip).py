import zipfile as zp

zipp = zp.ZipFile('zipped.zip','w')
zipp.write('img.png')


# Unzip
# Before running these codes comment down 3rd and 4th line
with zp.ZipFile('zipped.zip','r') as file:
    file.extractall('temp unzipped')