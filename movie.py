import os

for a, b, c in os.walk('Movie'):
    for d in c:
        os.system(f'CRID-umd-Decrypter.exe -a 3CEB7781 -b 0000002B -o {a} {a}\\{d}')