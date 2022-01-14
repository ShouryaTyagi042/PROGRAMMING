key_value ={}

# Initializing the value
key_value[20] = 56
key_value[14] = [2,3,5]
key_value[55] = 12
key_value[42] = 12
key_value[61] = 18
key_value[3] = 323

l1 = [1,24,6,354,73547,34]
print(key_value.items())

key = lambda s:(s[2], s[3] )
# print(ke)
key_value_list = list(key_value.items())
print(key(l1))
print(key(key_value_list))

for i in sorted(key_value.keys()) :
    print(i, end=" ")

print(key_value[14][2])

# print(
