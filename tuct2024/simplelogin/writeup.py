## first sub
flag = "TUCTF{"

## second sub
code = "hosepres"
arr = [26,26,29,11,25,28,2,44] 
for i in  range(len(code)):
    flag += chr(ord(code[i]) ^ arr[i])

## thirs sub
code2 = "guebhtu_gur_fhoebhgvarf!!"
for i in code2:
    if ord(i) < 97 or ord(i) > 122:
        flag+= i
    else:
        flag += chr((ord(i) - 84) % 26 + 97)
flag += '}'
print(flag)
