
import random
import time
print(time.time())
seed = int(time.time())
flag = list('o1me0T3}h_hTuvar_M4vdCFF3__{l3TY')
random.seed(seed)
random.shuffle(flag)
flag = ''.join(flag)
if 'FMCTF' in flag:
    print(f'flag = {flag!r}')
