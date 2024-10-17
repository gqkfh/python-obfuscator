import os

try:
    import random, zlib, lzma
    from marshal import dumps
    from colorama import Fore, Style

except:
    os.system('pip install zlib lzma marshal')

class color:
    RED = Fore.RED + Style.BRIGHT
    WHITE = Fore.WHITE + Style.BRIGHT
    RESET = Fore.RESET + Style.RESET_ALL

def reset_color():
    print(color.RESET)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_title():
    clear()
    title = '''
██████╗ ██╗   ██╗ ██████╗ ██████╗ ███████╗
██╔══██╗╚██╗ ██╔╝██╔═══██╗██╔══██╗██╔════╝
██████╔╝ ╚████╔╝ ██║   ██║██████╔╝█████╗  
██╔═══╝   ╚██╔╝  ██║   ██║██╔══██╗██╔══╝  
██║        ██║   ╚██████╔╝██████╔╝██║     
╚═╝        ╚═╝    ╚═════╝ ╚═════╝ ╚═╝    
'''

junk = "__skid__" * 15

file = input('Drag or drop youir file here: ')

chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def genvar():
    var = ''
    for i in range(10):
        var += random.choice(chars)
    return var

def compress(text):
    ok = zlib.compress(text.encode())
    ok = lzma.compress(ok)
    return ok

def encrypt1(text):
    src = compile(text, 'coduter', 'exec')
    ma = dumps(src)
    s = f'{junk}="{junk}";{junk}="{junk}";{junk}="{junk}";exec(loads({ma}));{junk}="{junk}";{junk}="{junk}"'
    compresse = compress(s)
    oke = f"import zlib,lzma\nexec(zlib.decompress(lzma.decompress({compresse})))"
    return oke

def encrypt2(text):
    sta = genvar()
    code = text
    s = compile(code, 'coduter', 'exec')
    maa = dumps(s)
    stub2 = f'from marshal import loads;exec(loads({maa}));'
    fin = f'{junk}="{junk}";{junk}="{junk}";{stub2}{junk}="{junk}";{junk}="{junk}";'
    return fin

if not os.path.isfile(file):
    print('File not found')
    exit()
print('\n')
print('[+] encrypting ...')

# Modifier cette ligne pour utiliser l'encodage utf-8
with open(file, 'r', encoding='utf-8') as f:
    code = f.read()

code = encrypt1(code)
code = encrypt2(code)
print('[+] done')
print('\n')
name = file.split('/')[-1]
name = name.split('.')[0]
with open(f'{name}-obf.py', 'w', encoding='utf-8') as f:
    f.write(code)

os.system('cls' if os.name == 'nt' else 'clear')
print(f'done your file is encrypted and saved as {name}-obf.py')
print('\n')
print('[+] thanks for using this tool')
import time
time.sleep(5)
exit()

Contraer
obf (2) (1).py4 KB

import base64

def encode_file_to_base64(input_file, output_file):
    """Read a Python file, encode its content to Base64, and write the encoded content to a new file."""
    with open(input_file, 'rb') as f:
        code = f.read()
