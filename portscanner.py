import socket
import sys


#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def scan_ports(addr):
    try:
        for port in range(1, 16535):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = s.connect_ex((addr, port))
            if result == 0:
                print ('port {}: open'.format(port))

def main():
    if (len(sys.argv) < 2):
        host = raw_input('No cl args, input hostname: ')
        scan_ports(socket.gethostbyname(host))
    else:
        hosts = sys.argv
        hosts.remove(sys.argv[0])
        for host in hosts:
            scan_ports(socket.gethostbyname(host))

if __name__ == '__main__':
    main()
