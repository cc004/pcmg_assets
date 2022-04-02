import os

for a,b,c in os.walk('.'):
    for d in c:
        if '#' in d:
            os.remove(f'{a}/{d}')