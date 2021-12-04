#recognising qrcode
import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

d=decode(Image.open("mycode.png"))
y=(d[0].data.decode("ascii"))

gauth = GoogleAuth()           
drive = GoogleDrive(gauth)

#uploading the picture of qr
'''upload_file_list = ['mycode.png']
for upload_file in upload_file_list:
	gfile = drive.CreateFile({'parents': [{'id': '1pzschX3uMbxU0lB5WZ6IlEEeAUE8MZ-t'}]})
	# Read file and set it as the content of this instance.
	gfile.SetContentFile(upload_file)
	gfile.Upload() # Upload the file.'''

value=input("Do you want to see the list of files in drive? type in yes or no")
if value in["yes","YES","Yes"]:

    file_list = drive.ListFile({'q': "'{}' in parents and trashed=false".format('1cIMiqUDUNldxO6Nl-KVuS9SV-cWi9WLi')}).GetList()
    for file in file_list:
	    print('title: %s, id: %s' % (file['title'], file['id']))
	    
# Create a GoogleDriveFile instance with title 'test.txt'.
file1 = drive.CreateFile({'parents': [{'id': '1cIMiqUDUNldxO6Nl-KVuS9SV-cWi9WLi'}],'title': 'test.txt'})  
# Set content of the file from the given string.
file1.SetContentString("y") 
file1.Upload()