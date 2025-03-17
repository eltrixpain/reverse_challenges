#eltrix
def recover_flag():
    v3 = [6, 17, 29, 114, 96, 31, 24, 124, 62, 15]
    v4 = [0x6D, 0x78, 0x33, 0x35, 0x40, 0x5E, 0x3E, 0x25, 0x5F, 0x30, 0x78, 0x14]
    v5 = [0x37, 0x4A]  
    A = v3 + v4 + v5
    str2 = b"GRX14YcKLzXOlW5iaSlBIrN7"  
    flag_bytes = []
    for i in range(24):
        xor_value = A[i] ^ str2[i]
        flag_bytes.append(xor_value)
    return bytes(flag_bytes).decode('ascii')
def main():
    flag = recover_flag()
    print(flag)

if __name__ == "__main__":
    main()

