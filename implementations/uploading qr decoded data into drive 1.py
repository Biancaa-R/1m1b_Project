from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth

# For using listdir()
import os
F=open("D:\\12th File handle\\string.txt","a")
Y="In physics, string theory is a theoretical framework\
in which the point-like particles of particle physics are replaced\
by one-dimensional objects called  strings. String theory describes how\
these strings propagate through space and interact\
with each other. ... Thus string theory is a theory of quantum gravity."
F.write(Y)
F.close()
# Below code does the authentication
# part of the code
gauth = GoogleAuth()

# Creates local webserver and auto
# handles authentication.
gauth.LocalWebserverAuth()	
drive = GoogleDrive(gauth)

# replace the value of this variable
# with the absolute path of the directory
path = r"D\12th File handle\string.txt"

# iterating thought all the files/folder
# of the desired directory
for x in os.listdir(path):

	f = drive.CreateFile({'string theory': x})
	f.SetContentFile(os.path.join(path, x))
	f.Upload()

	# Due to a known bug in pydrive if we
	# don't empty the variable used to
	# upload the files to Google Drive the
	# file stays open in memory and causes a
	# memory leak, therefore preventing its
	# deletion

	f = None
