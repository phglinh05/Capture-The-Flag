from cryptography import x509
from cryptography.hazmat.backends import default_backend

with open("2048b-rsa-example-cert.der", "rb") as f:
    cert = x509.load_der_x509_certificate(f.read(), default_backend())

print(cert.public_key().public_numbers().n)
