import subprocess

host = input("Enter a host to ping: ") 
p1 = subprocess.Popen(['ping', '-n 2', host], stdout=subprocess.PIPE) 
output = p1.communicate()[0] 
print (output)