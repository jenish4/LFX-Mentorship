'''

LFX Mentorship Coding Challenge

Jenish Shah
jenishshah08@gmail.com

'''

# taking the inputs:

isa_string = input("Please input a valid RISC-V ISA string: ")
print ("Thank you. We will now generate coverpoints for each of the relevant bits in the extension field of misa register:")
isa_string = isa_string.strip()     # removing extra spaces in the string, if any
isa_string = isa_string.upper()     # converting to upper case

# Checking for some corner cases:

if ('G' in isa_string):
    if 'I' not in isa_string:
        isa_string = isa_string + 'I'
    if 'M' not in isa_string:
        isa_string = isa_string + 'M'
    if 'A' not in isa_string:
        isa_string = isa_string + 'A'
    if 'D' not in isa_string:
        isa_string = isa_string + 'D'

if ('D' in isa_string):
    if 'F' not in isa_string:
        isa_string = isa_string + 'F'

if ('E' not in isa_string):
    if 'I' not in isa_string:
        isa_string = isa_string + 'I'

# list of all the possibilities in the extension field of misa register:
extensions = ['A', 'B', 'C', 'D', 'E', 'F', ' ', 'H', 'I', 'J', ' ', ' ', 'M', 'N', ' ', 'P', 'Q', ' ', 'S', ' ', 'U', 'V', ' ', 'X', ' ', ' ',]
# the reserved characters are kept empty.

for extension in extensions:                            # checking for each extension bit
    if extension in isa_string[4:]:                     # excluding the "RV32" from "RV32IM"
        extension_bit = extensions.index(extension)     # finding the extension bit
        extension_bit_hex = hex(2**extension_bit)       # convert it to 0x format
        # Now, we generate the coverpoint:
        print (f"misa && {extension_bit_hex} == {extension_bit_hex}")
