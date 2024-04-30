N = int(input("plz enter a number: "))
binary_num = bin(N)[2:]
toggled_bit = ''.join('1' if bit == '0' else '0' for bit in binary_num)
print(int(toggled_bit, 2))
