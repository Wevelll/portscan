import socket
import sys

def scan_ports(host, ports):
    avialiable_ports = list()
    print ('scanning {}...'.format(host))
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        try:
            result = s.connect_ex((host, port))
            if result == 0:
                avialiable_ports.append(port)
            s.close()
        except socket.gaierror:
            print ('hostname not resolved')
            return
        except socket.error:
            print ("couldn't connect")
            return
    return avialiable_ports


def check_argv(argv):
    data = { 'full_scan': False, 'hosts': list() }
    for arg in argv:
        if arg == '-a':
            data['full_scan'] = True
        else:
            data['hosts'].append(arg)
    return data


def main():
# most popular ports by https://kb.justhost.ru/article/1150
    ports = {20: 'FTP', 21: 'FTP', 22: 'SSH', 23: 'telnet', 25: 'SMTP',  53: 'DNS', 80: 'HTTP', 110: 'POP3', 143: 'IMAP', 443: 'HTTPS', 587: 'SMTP', 993: 'IMAP-SSL', 995: 'POP3S', 2083: 'cPanel(user)', 2087: 'cPanel(admin)', 2222: 'DirectAdmin',3128: 'HTTP-PROXY', 3306: 'MySQL', 8080: 'HTTP-PROXY', 8083: 'Vesta'}

    data = check_argv(sys.argv[1:])
    if not data['hosts']:
        data['hosts'] = input('No hosts given, give one: ')
    if data['full_scan']:
        ports = range(1, 1024)
    for host in data['hosts']:
        result = scan_ports(host, ports)
    for port in result:
        print ('[+]port {} {}: open'.format(port, ports[port]))
    print ('\n[*] total ports scanned: {0}\n[*] open ports: {1}\n[*] closed ports: {2}'.format(len(ports), len(result), (len(ports) - len(result))))

if __name__ == '__main__':
    main()
