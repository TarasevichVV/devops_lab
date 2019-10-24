n = int(input())
for i in range(1, n + 1):
    print(i, str(oct(i))[2:], str(hex(i))[2:], str(bin(i))[2:])
