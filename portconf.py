def portas_co():
    portas = [21, 22, 23, 25, 26, 53, 69, 79, 80, 106, 110, 115, 135, 139, 143, 443, 445, 465, 587, 873, 993, 995, 1025, 1026, 1027, 1028, 1029, 1030, 2000, 2222, 2049, 2869, 3306, 5357, 5555, 8080, 8443, 9001, 32768, 52869]
    return portas

def portas_info():
    portas_info = {
    21:'FTP',
    22:'SSH',
    25:'SMTP',
    23:'TELNET',
    26:'RSFTP',
    53:'DNS',
    69:'TFTP',
    79:'FINGER',
    80:'HTTP',
    106:'POP3-PW',
    110:'POP3',
    115:'SFTP',
    135:'EPMAP',
    139:'NETBIOS-SSN',
    143:'IMAP4',
    443:'HTTPS',
    445:'MS-DS',
    465:'SMTP',
    587:'SMTP',
    873:'RSYNC',
    993:'IMAP4/SSL',
    995:'POP3/SSL',
    1025:'MSRPC',
    1026:'MSRPC',
    1027:'MSRPC',
    1028:'MSRPC',
    1029:'MSRPC',
    1030:'MSRPC',
    2000:'CISCO',
    2222:'EtherNetIP-1',
    2049:'NFS',
    2869:'ICSLAP',
    3306:'MYSQL',
    5357:'HTTP',
    5555:'FREECIV',
    8080:'HTTP_ALT',
    8443:'SSP',
    9001:'TOR-ORPORT',
    32768:'???',
    52869:'UPNP'
    }
    return portas_info