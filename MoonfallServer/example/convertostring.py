def padded_bin(number, width=8, padchar='0'):
    return bin(number)[2:].rjust(width, padchar)

with open(r'suma.exe', 'rb') as f:
    as_binary = ''.join(padded_bin(ord(c)) for c in f.read())

print(as_binary)