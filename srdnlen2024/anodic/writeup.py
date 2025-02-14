from pwn import *
import hashlib


# nothing more than a dfs and bruteforce for finding the flag.
def brute_force(depth, inp):
    print(inp)
    if depth == 63:
        print(inp)
        return
    
    for j in "_" + string.printable:
        target = process('./egghead')
        target.recvline()
        for i in inp:
            target.sendline(i)
            target.recvline()
        target.sendline(j)
        out = target.recvline().decode()
        target.close()
        if "There" not in out:
            brute_force(depth+1, inp + j)

if __name__ == "__main__":
    context.log_level = 'critical'

    brute_string = "srdnlen{Mr_Evrart_is_helping_me_find_my"
    brute_force(39, brute_string)
