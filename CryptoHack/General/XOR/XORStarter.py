string = b'label'
int = 13
from pwn import xor
print(xor(string, int))