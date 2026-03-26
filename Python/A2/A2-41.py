n=int(input())
print(bin(n).replace("0b",""))
print(oct(n).replace("0o",""))
print(hex(n).replace("0x","").upper())