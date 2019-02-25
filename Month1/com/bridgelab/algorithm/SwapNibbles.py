from com.bridgelab.util.Utility import to_binary, swap_nibbles, to_decimal

decimal = int(input("Enter decimal number : "))
binary = to_binary(decimal)
print("binary number : ", binary)

swapBinary = swap_nibbles(binary)
print("Swap Binary number : ", swapBinary)

print("Decimal of swap binary : ", to_decimal(swapBinary))
