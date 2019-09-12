import socket
import sys


def scan_ports(addr):
    print ('scanning...')
    try:
        for port in range(1, 16535):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.01)
            result = s.connect_ex((addr, port))
            if result == 0:
                print ('port {}: open'.format(port))
            s.close()
    except socket.gaierror:
        print ("hostname not resolved")
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
