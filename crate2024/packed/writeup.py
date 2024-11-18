byte_list = []
decode = []

with open('flag.packed', 'rb') as file:  # 'rb' mode opens the file in binary read mode
    while (byte := file.read(1)):
        byte_list.append(byte)

result = []
for i in range(len(byte_list)):
    if i % 3 == 0:
        for j in range(int.from_bytes(byte_list[i+2],byteorder='big')):
            result.append(int.from_bytes(byte_list[i],byteorder = 'big') + 0x50)
            #result.append(int.from_bytes(byte_list[i+2],byteorder='big') + 0x50)

print(result)
with open('output.bin', 'wb') as file:
    for integer in result:
        integer = integer % 256
        # Convert to a single byte if the integer fits (0-255)
        if 0 <= integer <= 255:
            file.write(integer.to_bytes(1, byteorder='little'))

