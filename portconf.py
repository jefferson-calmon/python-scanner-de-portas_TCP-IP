def portas_co():
    portas = [0, 1, 2, 5, 7, 9, 11, 13, 17, 18, 19, 20, 21, 22, 23, 25, 26, 35, 37, 38, 39, 41, 42, 42, 43, 49, 53, 57, 69, 70, 79, 80, 80, 81, 81, 88, 101, 102, 106, 107, 109, 110, 111, 113, 115, 117, 118, 119, 123, 135, 137, 138, 139, 143, 152, 153, 156, 158, 161, 162, 170, 179, 194, 201, 209, 213, 218, 220, 259, 264, 311, 318, 323, 383, 366, 369, 371, 384, 387, 389, 401, 411, 412, 427, 443, 444, 445, 464, 465, 500, 502, 512, 513, 514, 515, 520, 524, 530, 531, 532, 540, 542, 543, 544, 546, 547, 548, 554, 556, 563, 587, 591, 593, 604, 631,
636, 639, 646, 647, 648, 652, 654, 665, 674, 691, 692, 695, 698, 699, 700, 701, 702, 706, 711, 712, 720, 749, 782, 829, 860, 873, 901, 911, 981, 989, 990, 991, 992, 993, 995, 1025, 1026, 1027, 1028, 1029, 1030, 10001, 1059, 1080, 1099, 1109, 1176, 1182, 1198, 1214, 1223, 1234, 1241, 1248, 1270, 1311, 1313, 1337, 1344, 1352, 1387, 1414, 1431, 1433, 1434, 1494, 1512, 1521, 1521, 1522, 1524, 1526, 1533, 1547, 1677, 1716, 1723, 1755, 1761, 1761, 1762,
1763, 1764, 1765, 1766, 1767, 1768, 1863, 1883, 1935, 1970, 1971, 1972, 1984, 2000, 2002, 2031, 2049, 2053, 2074, 2082, 2082, 2083, 2083, 2086, 2086, 2087, 2095, 2096, 2161, 2181, 2200, 2219, 2220, 2222, 2301, 2369, 2370, 2381, 2400, 2404, 2447, 2483, 2484, 2546, 2593, 2598, 2612, 2710, 2710, 2735, 2809, 2869, 2948, 2949,
2967, 3000, 3001, 3002, 3003, 3004, 3006, 3007, 3050, 3074, 3128, 3260, 3305, 3306, 3333, 3389, 3396, 3689, 3690, 3784, 3872, 3900, 3945, 4000, 4007, 4089, 4093, 4096, 4111, 4111, 4226, 4224, 4662, 4662, 4664, 4894, 4899, 5000, 5000, 5001, 5003, 5050, 5051, 5060, 5061, 5104, 5190, 5222, 5223, 5269, 5351, 5357, 5402,
5405, 5432, 5495, 5498, 5500, 5501, 5517, 5555, 5556, 5631, 5666, 5667, 5800, 5814, 5900, 5938, 6000, 6005, 6050, 6051, 6112, 6112, 6129, 6346, 6347, 6502, 6522, 6566, 6619, 6665, 6666, 6667, 6668, 6669, 6679, 6697, 6699, 6881, 6891, 6901, 6969, 6969, 7000, 7001, 7002, 7005, 7006, 7010, 7171, 7707, 7777, 8000, 8000, 8002, 8008, 8008, 8010, 8074, 8080, 8080, 8086, 8086, 8087, 8090, 8118, 8087, 8200, 8220, 8291, 8294, 8443, 8500, 8888, 8888, 8888, 9000, 9001, 9043, 9060, 9100, 9200, 9535, 9800, 10050, 10051, 10113, 10114, 10115, 10116, 12975, 13720, 13721, 13724, 13782, 13783, 15000, 19226, 19813, 20720, 22347, 22350, 25565, 25575, 25999, 26000, 26000, 30564, 31337, 31337, 31456, 32245, 32768, 37777, 4359, 52869]
    return portas

def portas_info():
    portas_info = {
    1:'TCPMUX',
    2:'iConnect Telecom',
    5:'RJE',
    7:'ECHO',
    9:'DISCARD',
    11:'SYSTAT',
    13:'DAYTIME',
    17:'QOTD',
    18:'MSP',
    19:'CHARGEN',
    20:'FTP',
    21:'FTP',
    22:'SSH',
    25:'SMTP',
    23:'TELNET',
    26:'RSFTP',
    35:'QMS',
    37:'TIME',
    38:'RAP',
    39:'RLP',
    41:'GRAPHICS',
    42:'WINS / HNS',
    43:'WHOIS',
    49:'TACACS',
    53:'DNS',
    57:'MTO',
    69:'TFTP',
    70:'GOPHER',
    79:'FINGER',
    80:'HTTP',
    81:'SKYPE / TORPARK',
    88:'KERBEROS',
    101:'HOSTNAME',
    102:'ISO-TSAP',
    107:'RTS',
    106:'POP3-PW',
    109:'POP',
    110:'POP3',
    111:'SUN',
    113:'IDENT',
    115:'SFTP',
    117:'UUCP-PATH',
    118:'SQL',
    119:'NNTP',
    123:'NTP',
    135:'EPMAP',
    137:'NETBIOS',
    139:'NETBIOS-SSN',
    143:'IMAP4',
    152:'BFTP',
    153:'SGMP',
    156:'SQL Service',
    158:'DMSP',
    161:'SNMP',
    162:'SNMPTRAP',
    170:'Print-srv',
    179:'BGP',
    194:'IRC',
    201:'ATRM',
    209:'TQMTP',
    213:'IPX',
    218:'MPP',
    220:'IMAP',
    259:'ESRO',
    264:'BGMP',
    311:'ASATWMT',
    318:'TSP',
    323:'IMMP',
    366:'SMTP / ODMR',
    369:'RPC2PORTMAP',
    371:'ClearCase aldb',
    383:'HP OpenView HTTPs Operations Agent',
    384:'ARNSS',
    387:'AURP',
    389:'LDAP',
    401:'UPS',
    443:'HTTPS',
    444:'SNPP',
    445:'MS-DS',
    464:'KERBEROS',
    465:'SMTP',
    500:'ISAKMP',
    520:'RIP',
    524:'NCP',
    530:'RPC',
    540:'UUCP',
    542:'COMMERCE',
    554:'RTSP',
    563:'NNTP',
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