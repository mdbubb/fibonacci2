zero = 0
one = 1
two = zero + one

num = raw_input("How many digits of the fibonnacci number would you like to print")
print zero
print one
print two
for x in range(int(num)):
    zero = one
    one = two
    two = zero + one
    print two