from Crypto.PublicKey import RSA
pem_file_path = 'privacy_enhanced_mail.pem'
with open(pem_file_path, 'r') as f:
    pem_data = f.read()
    key = RSA.import_key(pem_data)
print(key.d)