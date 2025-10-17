import base64
hex = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
bytes = bytes.fromhex(hex)
encode_base64 = base64.b64encode(bytes)
print(encode_base64)

# bytes: represents binary data 
# each byte is a number between 0 and 255.
# bytes is stored as binary data in memory, it is often displayed in hex format for easier inspection

# Encoding Base64: represent binary data as an ASCII string using an alphabet of 64 characters. One character of a Base64 string encodes 6 binary digits (bits)