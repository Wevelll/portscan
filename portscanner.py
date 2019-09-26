#!/bin/python3
import socket
import time
import sys

def scan_ports(host, ports):
    avialiable_ports = list()
    print ('[*] Scanning {}'.format(host))
    t1 = time.time()
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        try:
            result = s.connect_ex((host, port))
            if result == 0:
                avialiable_ports.append(port)
            s.close()
        except socket.gaierror:
            print ('[!] Hostname not resolved')
            return None
        except socket.error:
            print ("[!] Couldn't connect")
            return None
    t2 = time.time()
    print ('[*] Scanned in {0:,.2f} seconds!\n[>]'.format(t2 - t1))
    return avialiable_ports


def check_argv(argv):
    data = { 'full_scan': False, 'hosts': list() }
    for arg in argv:
        if arg == '-a':
            data['full_scan'] = True
        else:
            data['hosts'].append(arg)
    return data


def print_result(result, ports):
    for port in result:
# rewrite for -a
        if port in ports.keys():
            print ('[+] Port {} {}: open'.format(port, ports[port]))
        else:
            print ('[+] Port {}: open'.format(port))
    print ('[>]\n[*] Total ports scanned: {0}\n[*] open ports: {1}\n[*] closed ports: {2}'.format(len(ports), len(result), (len(ports) - len(result))))


def main():
# most popular ports by https://kb.justhost.ru/article/1150
    ports = {20: 'FTP', 21: 'FTP', 22: 'SSH', 23: 'telnet', 25: 'SMTP',  53: 'DNS', 80: 'HTTP', 110: 'POP3', 143: 'IMAP', 443: 'HTTPS', 587: 'SMTP', 993: 'IMAP-SSL', 995: 'POP3S', 2083: 'cPanel(user)', 2087: 'cPanel(admin)', 2222: 'DirectAdmin',3128: 'HTTP-PROXY', 3306: 'MySQL', 8080: 'HTTP-PROXY', 8083: 'Vesta'}
    f = False

    data = check_argv(sys.argv[1:])
    if not data['hosts']:
        print ('Usage: "python3 porscanner.py [-a to scan 1024 ports, default: scan 20 most popular ports] [hostname(s) or ip(s)]"')
        sys.exit(0)
    if data['full_scan']:
        ports = range(1, 1025)
    for host in data['hosts']:
        if f:
            print('\n')
        print_result(scan_ports(host, ports), ports)
        f = True


if __name__ == '__main__':
    main()
