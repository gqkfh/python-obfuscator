import os

try:
    import random
    import zlib
    import lzma
    from marshal import dumps, loads
    from colorama import Fore, Style
    
except ImportError:
    os.system('pip install colorama zlib lzma marshal')

class color:
    RED = Fore.RED + Style.BRIGHT
    WHITE = Fore.WHITE + Style.BRIGHT
    RESET = Fore.RESET + Style.RESET_ALL

def error(text):
    print(color.WHITE + '\n[*] Error: ' + color.WHITE + text)
    main()

def ret():
    input(color.WHITE + '[*] Press ENTER to return the menu: ')
    main()

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

def main():
    print_title()
    choice = input(color.WHITE + '[*] Enter your word for obfuscate the text: ')
    file = input(color.WHITE + '[*] Drag or drop your file here: ')
    choice_modif = '__' + choice + '__'
    junk = choice_modif * 15

    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def genvar():
        return ''.join(random.choice(chars) for _ in range(10))

    def compress(text):
        return lzma.compress(zlib.compress(text.encode()))

    def encrypt1(text):
        src = compile(text, 'coduter', 'exec')
        ma = dumps(src)
        s = f'{junk}="{junk}";{junk}="{junk}";{junk}="{junk}";exec(loads({ma}));{junk}="{junk}";{junk}="{junk}"'
        compresse = compress(s)
        return f"import zlib,lzma\nexec(zlib.decompress(lzma.decompress({compresse})))"

    def encrypt2(text):
        sta = genvar()
        s = compile(text, 'coduter', 'exec')
        maa = dumps(s)
        stub2 = f'from marshal import loads;exec(loads({maa}));'
        return f'{junk}="{junk}";{junk}="{junk}";{stub2}{junk}="{junk}";{junk}="{junk}";'

    if not os.path.isfile(file):
        error('File not found')

    print(color.RED + '\n[*] Obfuscating...')

    with open(file, 'r', encoding='utf-8') as f:
        code = f.read()

    code = encrypt1(code)
    code = encrypt2(code)

    print(color.WHITE + '[*] Done!')

    name = os.path.splitext(os.path.basename(file))[0]
    with open(f'{name}-obf.py', 'w', encoding='utf-8') as f:
        f.write(code)

    os.system('cls' if os.name == 'nt' else 'clear')
    print(color.WHITE + f'\n[*] File obfuscated and saved as {color.RED}{name}-obf.py{color.WHITE}')
    ret()

main()
