def xor1(a, b):
    return (not a and b) or (a and not b)


def xor2(a, b):
    return a is not b


print(xor1(True, True))
print(xor1(True, False))
print(xor1(False, True))
print(xor1(False, False))

print(xor2(True, True))
print(xor2(True, False))
print(xor2(False, True))
print(xor2(False, False))
