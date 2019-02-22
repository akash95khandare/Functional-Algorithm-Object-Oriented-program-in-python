from com.bridgelab.util.Utility import toBinary, swapNibbles, toDecimal

decimal = int(input("Enter decimal number : "))
binary = toBinary(decimal)
print("binary number : ", binary)

swapBinary = swapNibbles(binary)
print("Swap Binary number : ", swapBinary)

print("Decimal of swap binary : ", toDecimal(swapBinary))
