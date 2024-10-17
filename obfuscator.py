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

def error(text):
    print(color.WHITE + '\n[*] Error: ' + color.WHITE + text)
    print_title()

def ret():
    choice = input(color.WHITE + '[*] Press ENTER to return the menu: ')
    print_title()

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
    print(color.RED + title)

print_title()

choice = input(color.WHITE + '[*] Enter your word for obfuscate the text: ')
file = input(color.WHITE + '[*] Drag or drop youir file here: ')
junk = choice * 15

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
    error('File not found')
    
print(color.RED + '\n[*] Obfuscating...')

with open(file, 'r', encoding='utf-8') as f:
    code = f.read()

code = encrypt1(code)
code = encrypt2(code)

print(color.WHITE + '[*] Done!')

name = file.split('/')[-1]
name = name.split('.')[0]
with open(f'{name}-obf.py', 'w', encoding='utf-8') as f:
    f.write(code)

os.system('cls' if os.name == 'nt' else 'clear')
print(color.WHITE + f'\n[*] File obfuscated and saved as {color.RED}{name}-obf.py{color.WHITE}')
ret()
