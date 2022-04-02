import os

for a, b, c in os.walk('Sound'):
    for d in c:
        if d.endswith('.awb'):
            os.system(f'./vgmstream-cli {a}/{d}')