from pwn import *
import time

context.log_level = 'error'
keys = []
for i in range(64 , 200000):
    print(i)
    r = process("./reciprocal")
    r.recvline()
    r.recvline()
    r.sendline('EPFL'.encode())
    r.recvline()
    r.sendline(str(i).encode())
    s = r.recvline()
    if 'XwSo' in s.decode():
        keys.append(i)
    if i == 100000:
        print(keys)
    if i == 50000:
        print(keys)
    r.close()


print(keys)


