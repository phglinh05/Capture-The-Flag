import requests
from Crypto.PublicKey import RSA
from OpenSSL import crypto

domain = "thetransparencyflagishere.cryptohack.org"
seen_serials = set()

# Đọc modulus từ transparency.pem
with open("transparency.pem", "r") as f:
    transparency_key = RSA.import_key(f.read())
    target_modulus = transparency_key.n

def fetch_certs(domain):
    url = f"https://crt.sh/?q=%25.{domain}&output=json"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception("Failed to fetch data from crt.sh")
    return response.json()

def get_cert_pem(cert_id):
    url = f"https://crt.sh/?d={cert_id}"
    response = requests.get(url)
    return response.content

def extract_modulus(pem_data):
    cert = crypto.load_certificate(crypto.FILETYPE_PEM, pem_data)
    pub_key_obj = crypto.dump_publickey(crypto.FILETYPE_PEM, cert.get_pubkey())
    key = RSA.import_key(pub_key_obj)
    return key.n

# Lấy danh sách chứng chỉ
certs = fetch_certs(domain)
print(f"[+] Found {len(certs)} cert entries for *.{domain}")

# Duyệt từng chứng chỉ
for cert in certs:
    cert_id = cert["id"]
    if cert_id in seen_serials:
        continue
    seen_serials.add(cert_id)

    try:
        pem = get_cert_pem(cert_id)
        modulus = extract_modulus(pem)

        if modulus == target_modulus:
            print(f"MATCH FOUND at cert ID: {cert_id}")
            print(f"https://crt.sh/?id={cert_id}")
            print(f"Subdomain likely uses this key: {domain}")
            break
        else:
            print(f"Cert ID {cert_id} → No match.")
    except Exception as e:
        print(f"[!] Error parsing cert {cert_id}: {e}")

