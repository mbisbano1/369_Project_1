import shutil
import os, sys

#Constant Definititions
CWD = os.getcwd()
source = CWD + '/MDrive'
destination = CWD + '/Downloadables/mdrive.zip'

#Function Definitions
def make_zip(source, destination):
        base = os.path.basename(destination)
        name = base.split('.')[0]
        format = base.split('.')[1]
        archive_from = os.path.dirname(source)
        archive_to = os.path.basename(source.strip(os.sep))
        print(source, destination, archive_from, archive_to)
        shutil.make_archive(name, format, archive_from, archive_to)
        shutil.move('%s.%s'%(name,format), destination)



#Beginning of code

make_zip(source, destination)

while(True):
	a = 0
	


