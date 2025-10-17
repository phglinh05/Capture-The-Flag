integer = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
str = ""
for i in integer:
    str += chr(i)
print(str)

#chr(): convert an ASCII ordinal number to a character
#ord(): convert a character to an ASCII ordinal number
