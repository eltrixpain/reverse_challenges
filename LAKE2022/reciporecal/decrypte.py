from pwn import *
import string

context.log_level = 'error'
STR = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz{}_"
out = "XwSoYZWEXnbLmPP0{HO20TYYJKrLVr_2KfYhPgkVsFkR"
flag = ""
key = "120047"
count = 0
for i in out:
    for j in STR:
        temp = flag + j
        r = process("./reciprocal")
        r.recvline()
        r.recvline()
        r.sendline(temp.encode())
        r.recvline()
        r.sendline(key.encode())
        s = r.recvline().decode().split(':')[1].split()[0]
        if s == out[:count + 1]:
            flag += j
            count+=1
            break
        r.close()


print(flag)

