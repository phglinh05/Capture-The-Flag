import base64
import struct
from paramiko import Message

with open("bruce_rsa.pub", "r") as f:
    b64_data = f.read().split()[1]
    raw = base64.b64decode(b64_data)
    msg = Message(raw)

    _type = msg.get_string()     # "ssh-rsa"
    e = msg.get_mpint()          # public exponent
    n = msg.get_mpint()          # modulus

    print(n)
