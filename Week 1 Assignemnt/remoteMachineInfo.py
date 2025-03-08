import socket
def get_remote_machine_info():
    remote_host= 'www.python.org'
    remote_host2= 'www.uts.edu.au'
    try:
        print("  Remote host name: %s"  % remote_host)
        print("  IP address: %s" %socket.gethostbyname(remote_host))
    except socket.error as err_msg:
        print("Error accessing %s: error number and detail %s" %(remote_host, err_msg))
    try:
        print("  Remote host name: %s"  % remote_host2)
        print("  IP address: %s" %socket.gethostbyname(remote_host2))
    except socket.error as err_msg:
        print("Error accessing %s: error number and detail %s" %(remote_host2, err_msg))
if __name__== '__main__':
    get_remote_machine_info()
              