from pwn import remote # pip install pwntools
from Crypto.Util.number import *
import json
import base64
import codecs
import random

r = remote('socket.cryptohack.org', 13377, level = 'debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)



for i in range(100):
    received = json_recv()

    print("Received type: ")
    print(received["type"])
    print("Received encoded value: ")
    print(received["encoded"])
    if(received["type"]=="base64"):
        to_send = {
            "decoded": base64.b64decode(received["encoded"]).decode()
        }
        json_send(to_send)
    elif(received["type"]=="hex"):
        to_send = {
            "decoded": bytes.fromhex(received["encoded"]).decode()
        }
        json_send(to_send)
    elif(received["type"]=="rot13"):
        to_send = {
            "decoded": codecs.decode(received["encoded"], 'rot_13')
        }
        json_send(to_send)
    elif(received["type"]=="bigint"):
        to_send = {
            "decoded": bytes.fromhex((received["encoded"].replace("0x",""))).decode()
        }
        json_send(to_send)
    elif(received["type"]=="utf-8"):
        to_send = {
            "decoded": ''.join(chr(b)for b in received["encoded"])
        }
        json_send(to_send)


json_recv()