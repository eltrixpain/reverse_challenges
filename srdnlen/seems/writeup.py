# in the _start subroutine the code try to change the main function so all we need is see the main code in debugger after changing
key = bytes.fromhex("3d2e707134232e33")
key2 = bytes.fromhex("32341f327336732e")
key3 = bytes.fromhex("1f7328141f347535")
key4 = bytes.fromhex("2e35261f2e71742d")
key5 = bytes.fromhex("00003d2e70713423")
key6 = bytes.fromhex("00001d445c063bd0")
flag = ""
for i in key[::-1]:
    flag+=chr(0x40 ^ i)

for i in key2[::-1]:
    flag+=chr(0x40 ^ i)

for i in key3[::-1]:
    flag+=chr(0x40 ^ i)

for i in key4[::-1]:
    flag+=chr(0x40 ^ i)

for i in key5[::-1]:
    flag+=chr(0x40 ^ i)

print(flag)
