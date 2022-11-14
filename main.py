import subprocess
import platform

system = platform.system()

if ( system == 'Windows') :
    subprocess.run('ping 8.8.8.8')
elif ( system == 'Linux' ) :
    subprocess.run('ping 8.8.8.8 -c 3')