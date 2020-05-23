import os

def ping(alvo):
    if alvo[-1] == '/':
        alvo = alvo[:-1]
    else:
        pass

    if alvo.find('http') == 0:
        index = alvo.index('p') + 1
        if alvo[index] == 's':
            alvo = alvo[8:]
        else:
            alvo = alvo[7:]
    else:
        pass

    rs = alvo.find('www')
    if rs != 0:
        alvo = alvo[0:rs] + site[rs+4:]

     
    bat = open('cmd.bat', 'w')
    bat.write(f'ping {alvo} > cmd.txt')
    bat.close()

    os.system('cmd.bat > nul')
    os.remove('cmd.bat')
    
    txt = open('cmd.txt', 'r')
    return_cmd = txt.readlines()
    line_alvo = return_cmd[1]

    index_ini_alvo = line_alvo.index('[')+1
    index_fim_alvo = line_alvo.index(']')
    ip_alvo = line_alvo[index_ini_alvo:index_fim_alvo]

    return ip_alvo


def find_ip(alvo):
    if alvo.find('http') != 0:
        return alvo
    else:
        try:
            return ping(alvo)
        except:
            return False
