import socket
import sys


def scan_ports(addr):
    print ('scanning...')
    for port in range(1, 1024):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        try:
            result = s.connect_ex((addr, port))
            if result == 0:
                print ('port {}: open'.format(port))
            else:
                print ('port {}: closed'.format(port))
            s.close()
        except socket.gaierror:
            print ('hostname not resolved')
            return
        except socket.error:
            print ("couldn't connect")
            return


def main():
    if (len(sys.argv) < 2):
        host = input('No cl args, input hostname: ')
        scan_ports(host)
    else:
        hosts = sys.argv
        hosts.remove(sys.argv[0])
        for host in hosts:
            scan_ports(host)


if __name__ == '__main__':
    main()
