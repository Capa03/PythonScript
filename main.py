from urllib.request import urlretrieve
import getpass
import subprocess


urls ="https://download.anydesk.com/AnyDesk.exe"
print('File Downloading')

usrname = getpass.getuser()
destination = f'C:\\Users\\{usrname}\\Downloads\\download.exe'

download = urlretrieve(urls, destination)

print('File downloaded')

subprocess.Popen( f'C:\\Users\\{usrname}\\Downloads\\download.exe')
