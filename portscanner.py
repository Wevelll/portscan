import socket
import sys

#ports taken from https://kb.justhost.ru/article/1150

def scan_ports(host, ports):
    print ('scanning {}...'.format(host))
    for port in ports.keys():
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        try:
            result = s.connect_ex((host, port))
            if result == 0:
                print ('[+]port {0} {1}: open'.format(port, ports[port]))
#            else:
#print ('[-]port {0} {1}: closed'.format(port, ports[port]))
            s.close()
        except socket.gaierror:
            print ('hostname not resolved')
            return
        except socket.error:
            print ("couldn't connect")
            return


def main():
    ports = {20: 'FTP', 21: 'FTP', 22: 'SSH', 23: 'telnet', 25: 'SMTP',  53: 'DNS', 80: 'HTTP', 110: 'POP3', 143: 'IMAP', 443: 'HTTPS', 587: 'SMTP', 993: 'IMAP-SSL', 995: 'POP3S', 2083: 'cPanel(user)', 2087: 'cPanel(admin)', 2222: 'DirectAdmin',3128: 'HTTP-PROXY', 3306: 'MySQL', 8080: 'HTTP-PROXY', 8083: 'Vesta'}
    if (len(sys.argv) < 2):
        host = input('No cl args, input hostname: ')
        scan_ports(host, ports)
    else:
        hosts = sys.argv
        hosts.remove(sys.argv[0])
        if '-a' in sys.argv:
            ports = range(1, 1024)
            hosts.remove('-a')
        for host in hosts:
            scan_ports(host, ports)


if __name__ == '__main__':
    main()
