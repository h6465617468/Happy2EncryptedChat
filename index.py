import sys
sys.dont_write_bytecode = True

elliptic_private_key_pem = """
-----BEGIN EC PRIVATE KEY-----
MHQCAQEEIP7I0fsNgSfPCRggdnEFXarwWUGuLBBmalFMQNnoHDZdoAcGBSuBBAAK
oUQDQgAE/tolsS0q6NQIynNqs+efEKUVv4TRwZCNMgHF41mrveMxCOfoYG8m6ew8
JK36TXLwgSDZeMC4RDHnOTDTsbeceg==
-----END EC PRIVATE KEY-----
"""

elliptic_public_key_pem = """
-----BEGIN PUBLIC KEY-----
MFYwEAYHKoZIzj0CAQYFK4EEAAoDQgAE/tolsS0q6NQIynNqs+efEKUVv4TRwZCN
MgHF41mrveMxCOfoYG8m6ew8JK36TXLwgSDZeMC4RDHnOTDTsbeceg==
-----END PUBLIC KEY-----
"""

# Private key in PEM format
private_key_pem = b"""
-----BEGIN RSA PRIVATE KEY-----
MIIJJgIBAAKCAgB7/3o2EI0vYMc6WUMmZGlaSZZ3w8WMRTdl6Z1RoKiyBPFY9jmy
Grbismvx7Vj/jRNt6aCKM1N83WkXNIEwCpOgWK1BoM7CaNu+VDr/bVd9UoAqYcdQ
uA4383hlAoTenln2t42Rk0sV9HsVa9uo6ZDTGURdbE79lrKxkwwM5p2La+8RtVWT
Z+k4VOfIbOvurwN6Ovct2RG03FB2URfAqY6GN/5WnCcFKWTO/tn/Bm6wLh6xGmBS
SjA8OUDYl5PE4EaxrmODnf+L7nOjIGpOGZ6cYkE9XhOjjr+1IOzv3OoKTYyn9Odu
6+jbV0lPksbnYFxG0kuFZIirt5EwEH+juaXsGoxGiqP6hTZEocMAHomEzabDNY1B
9Y+3YhyC4RP59ifd8fo/uD7DGQvxRgO9dGpwprTZfKrPxFCT9p17vw8/rOY88Cqb
dczF7BoMiLolKDq4YVxOhYreKj3NTyqrV5+xEuqfmTFJ6D/uEMAGnSRYMQneBJIC
wn1j0G78jkn8aMQcTofEOXG1UjDMKKvjfNfK4lLNB2VJzx6o/zd/vUYTjqYAotV0
dRrPPUJYXjWd0ZDL6PruQMW88gLfLJrV8WMYNgfV1A/YrJ2TrM+goS2aAYQ+gIPm
UgmgZSigqTDOV5ELz/JFTJ3/dMD5kg+rEBJYpwMSluAcoe/e+puxkA3PYwIDAQAB
AoICAHgU2lp/PusR8v47sX79oNUyDIihS69i3JpSWerSBmyXws6fbRJhMplppoXc
j+Kz0YwQw0rzF7gFh59UVoOayopvNiInQ/Qbriqs0ZHJZv/TpJDmrioqhIKEwyQ3
A0u/2GnIKk4/cWiqoYQGNuxmfL0ibAV5PSnyBc1YFURtFUcO2K+yh1RAPigyeWCs
svMsA9ccQYHiBHa9ISLjt3f5/C9ZDHL9uAAUrS6UubJynUD6+PgUDhHDDOFVpMnc
SNtRQsURmAe/O9pcqxnf63ME9oiF0p5GfAhZ1qfnYe2MaA5gOYXx8yqFRbUc2782
6m7p75MaVs6wpHZ/SBhe8e0xfU9EIb9RpF+aCM81UeOgqYWSlo1+1HsoXu02L8mT
/0khVN+Wq37t4pTktcl7YS1HumX6nMvnqQUUfF5rEQX7RoKGYfufe8GC8JdaYVqL
62jbzS3wAf+QL0j+vxUmaxwnoiZTpgTj6XiyjDT8qRLmeOgGSmG3cOe2JRGENV3W
n89RGsOY+LaiMaNuD25Cg0y9YBhwmZCJdKH3djvtbbLv/H2QY4SSKPdfqqpYOAlF
e3uyx5jZQSuA4CmnSxUw0ofqeBlDArYxtmqwFlKDCFJQNww7ye2tzD5ZiHZsdt0f
XIRm/Y0zRsOyW/SWGLpRa/r+8oGfgyyzbGriDoI+XZvVhHpxAoIBAQDKd86FY0V+
4Wyidz6HNMwhB5drvNGMG2L9KwnPWkJcZulgiUDuHPnsJZhpiR5+pRUjqFzb8zIW
EZPFMV/Ww9Y4Jn7dt2ndMLHLPxTcEgEbxZqxZFNYaPPiy1kMCISx4jOdAxB9OCJR
nvZKOaQE1wltTlPsvCWRUD8LJfeS9DuuERAOkaTpARbvi5f/o+JUJO1eK2+SAjHh
DK54iRlQMHnDi5BMjujpyG/acL7P7IIhQJZxvoit8/8wHPmiiy1bz4PwdzpdUNNs
yW+sLYqHui7JJ4ui2cq0fdAOwjiTYb0Km5XCtOvNYTrUjkYz0SOkTbDJQfG8YtzG
Dp//OOVvFFGJAoIBAQCcyF6H2okGUEnxEa0+VEGu0c71K+Bs5hUq08dQULTFQ5qN
YyVBpCcGGAlB9BTzeRuNGv1SXnqHpp/Gvn2sIra7Z0P+V0scHdFkhilXzmul6lRE
6dIpeHimDPchT4jdzk9xLw9yRDejUqhVnMLg7G5OdVGPGikC5lr/RMKCGk1N6skE
3S8olkDtn5FJv9/zpDhWezwpQaIUgnIZaamEo4pn3EX0DSgyxaw8BrIw3lq4eeKr
N30mUSgAGeM/pHumaqrkRUyeFVVvY4MjKU+k/tzCJRoP+c2Q+WUEGPJ4AQt0MqNL
DfmkaZC7wBB1dNTg2nBZCK3q+mT6Z44siz3MiLqLAoIBABXsEvhuXz/1uIV+085f
8RpCcCrCLw40iOtQladV5omKuwow0k715DmleHM03ZBo33kU6bkHBA1PqehYCECA
w9kgkev/x/6jHx0an2+Uo3oWU0GR01RnSMDts56R7Yw1KdF+W3KzeUPNKm2vAAtm
HScwq/WeCZNKVQkn+z52I2AdiNeK/YgdDhaxzqtnW0IxHWJs4Y+1nSD49osmjQ8Z
sJVzrxQbBS0K/tFwE7j/qrde/ush7jqniKH1ATKQT0D5nxeSUUd5UOsehHDoHW/E
wPwWxA/F9STF2pk+flG263kSj4ydekqqlGwfW4qQwoMvxkyET2BOdAkd3EUOLAly
8cECggEAG55skLAdvV/9dpsvkrBTFdHeDHCbS3PIvM+r5+kfvzRmkIurr4GUYk1v
rA+sdSubf+MGRzFfkm/265L5Ho7K8/6ACtkj4SMblQLRW6eAbSz3hWBPZoDTeCUG
j/ar3K8QbZbluLJtvra78sD3z5m24Nln8bahDOK5mwho33R0s8oteU7hlNvLOlEG
ziAf+pKuXgW9lmL6g3RrVzC27SfGJP+3zwNWVoNeEQD4+QTipGbMWG8g+9QGIOZu
kvKN2cYmrqnKknqdn06/dj07y4weJZFVowTVgrl8Yxll9V/xvZmCDKG8nYr/NSPj
gl1/dtDkQ7r0sFVF3prJf+1TiKl5ewKCAQAntjOgSQk/mhqeMsgY+8td42qzYc6a
XRjXqoaNMk0iGW9iam9T7rHV25c3RV6ijlFTVLAyeZjSm81/4fv+ZiQb2O4eijKj
kJiSWY4pnC5IjC3m2Th52ShaBAM/naokzXr/OK7Lba/mmdwlByTiBSv1no9hjd4F
IP6bwPQD5VnD4ruymdVF7RyHbOllMYt4m1WZSuQJt6JjuYfTWe+B9BnthhuEJ/d7
CIgVv5kjtp9EoruOkHcuAYmqU+gW3FyuAaUZOB/31AfO0X0Q79DTfZ7Y6zfdiaEn
XpqXHPN6erWpiXh1U/e6hlYpagVTetr31y0auBYHVW3O3bB7EtIe8akz
-----END RSA PRIVATE KEY-----
"""

# Public key in PEM format
public_key_pem = b"""
-----BEGIN PUBLIC KEY-----
MIICITANBgkqhkiG9w0BAQEFAAOCAg4AMIICCQKCAgB7/3o2EI0vYMc6WUMmZGla
SZZ3w8WMRTdl6Z1RoKiyBPFY9jmyGrbismvx7Vj/jRNt6aCKM1N83WkXNIEwCpOg
WK1BoM7CaNu+VDr/bVd9UoAqYcdQuA4383hlAoTenln2t42Rk0sV9HsVa9uo6ZDT
GURdbE79lrKxkwwM5p2La+8RtVWTZ+k4VOfIbOvurwN6Ovct2RG03FB2URfAqY6G
N/5WnCcFKWTO/tn/Bm6wLh6xGmBSSjA8OUDYl5PE4EaxrmODnf+L7nOjIGpOGZ6c
YkE9XhOjjr+1IOzv3OoKTYyn9Odu6+jbV0lPksbnYFxG0kuFZIirt5EwEH+juaXs
GoxGiqP6hTZEocMAHomEzabDNY1B9Y+3YhyC4RP59ifd8fo/uD7DGQvxRgO9dGpw
prTZfKrPxFCT9p17vw8/rOY88CqbdczF7BoMiLolKDq4YVxOhYreKj3NTyqrV5+x
EuqfmTFJ6D/uEMAGnSRYMQneBJICwn1j0G78jkn8aMQcTofEOXG1UjDMKKvjfNfK
4lLNB2VJzx6o/zd/vUYTjqYAotV0dRrPPUJYXjWd0ZDL6PruQMW88gLfLJrV8WMY
NgfV1A/YrJ2TrM+goS2aAYQ+gIPmUgmgZSigqTDOV5ELz/JFTJ3/dMD5kg+rEBJY
pwMSluAcoe/e+puxkA3PYwIDAQAB
-----END PUBLIC KEY-----
"""

import threading
import argparse
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs
import os
import socket
import base64
import binascii
import json
import hashlib
import time
import zlib
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad, unpad
import webbrowser
import random
import asyncio
import websockets
import subprocess
import requests
from bs4 import BeautifulSoup
import datetime
import string
from Cryptodome.PublicKey import RSA
from Cryptodome.Signature import pkcs1_15
from Cryptodome.Cipher import PKCS1_v1_5
from Cryptodome.Hash import SHA256
from Cryptodome.Cipher import PKCS1_OAEP
import elliptic
import ecdsa
from ecdsa import VerifyingKey, util
import colorama
colorama.init()

# pip install pycryptodome
# pip install pycryptodomex
# pip install websockets
# pip install requests
# pip install beautifulsoup4
# pip install ecdsa
# pip install elliptic

# Disable bytecode writing for the Crypto module
sys.modules['Cryptodome'].__dict__['__file__'] = ''

host = '127.0.0.1'
port = 80

chatbotinvtext = ''.join(random.choices(string.ascii_letters + string.digits, k=512))

x1iv = ''.join(random.choices(string.ascii_letters + string.digits, k=16))

httpd = None
server_thread = None
__process_close__ = 0

def banner():
    print('''

                   ...
                 ;::::;              
               ;::::; :;             
             ;:::::'   :;            
            ;:::::;     ;.                   
           ,:::::'       ;           OOO\    
           ::::::;       ;          OOOOO\         
           ;:::::;       ;         OOOOOOOO        
          ,;::::::;     ;'         / OOOOOOO       
        ;:::::::::`. ,,,;.        /  / DOOOOOO
      .';:::::::::::::::::;,     /  /     DOOOO
     ,::::::;::::::;;;;::::;,   /  /        DOOO
    ;`::::::`'::::::;;;::::: ,#/  /          DOOO
    :`:::::::`;::::::;;::: ;::#  /            DOOO
    ::`:::::::`;:::::::: ;::::# /              DOO
    `:`:::::::`;:::::: ;::::::#/               DOO
     :::`:::::::`;; ;:::::::::##                OO
     ::::`:::::::`;::::::::;:::#                OO
     `:::::`::::::::::::;'`:;::#                O
      `:::::`::::::::;' /  / `:#
       ::::::`:::::;'  /  /   `#
    ''')

def str_splitx(string, splitLength):
    if splitLength is None:
        splitLength = 1
    if string is None or splitLength < 1:
        return False
    string += ""
    chunks = []
    pos = 0
    length = len(string) # Use a different name for the local variable
    while pos < length:
        chunks.append(string[pos:pos + splitLength])
        pos += splitLength
    return chunks

async def encryptDataserver(cache_x_RSA, target_public_x_key,ec_private_key):
    cache_signp = ""
    cache_109 = str_splitx(cache_x_RSA, 256) # I assume this is a custom function to split a string into chunks of 128 characters
    crypted0193 = []
    asjdasjdajs = []
    for data5 in cache_109:
        fsdkjf34o2it2 = base64.b64encode(data5.encode())
        if ec_private_key.strip().decode().startswith("-----BEGIN EC PRIVATE KEY-----"):
            # assume it is PEM format
            signingKey = ecdsa.SigningKey.from_pem(ec_private_key.strip())
        else:
            # assume it is hex format
            signingKey = ecdsa.SigningKey.from_string(bytes.fromhex(ec_private_key.strip().decode()),curve=ecdsa.SECP256k1)
        privKeyHex = signingKey.to_string().hex()
        privKey = int(privKeyHex, 16)
        signingKey = ecdsa.SigningKey.from_secret_exponent(privKey, curve=ecdsa.SECP256k1, hashfunc=hashlib.sha256)
        # Veriyi imzalarken hashlib.sha256 fonksiyonunu çağırın
        cache_signp = signingKey.sign(fsdkjf34o2it2, hashfunc=hashlib.sha256)
        asjdasjdajs.append({"text": fsdkjf34o2it2.decode(), "sign": cache_signp.hex()}) # Append the data and the signature to the list
    cache_123123 = json.dumps(asjdasjdajs) # Convert the list to JSON string
    cryptedasdasdas1111 = []
    cache_12312asdasdas3 = str_splitx(cache_123123, 256) # Split the JSON string into chunks of 128 characters
    for data10 in cache_12312asdasdas3:
        # Encrypt the data with public key
        crypt = RSA.import_key(target_public_x_key.strip()) # Import the public key from PEM format
        cipher = PKCS1_v1_5.new(crypt) # Create a PKCS1_OAEP cipher object
        cryptedasdasdas1111.append(base64.b64encode(base64.b64encode(cipher.encrypt(data10.encode()))).decode()) # Encrypt and base64 encode the data and append to the list
    crypted0193.append(base64.b64encode(json.dumps(cryptedasdasdas1111).encode()).decode()) # Convert the list to JSON string and base64 encode and append to the list
    return base64.b64encode(json.dumps(crypted0193).encode()).decode() # Convert the list to JSON string and base64 encode and return as string

async def decryptDataserver(encryptedData, myprivate,ec_public_key):
    decryptedData = ""
    try:
        crypted0193 = json.loads(base64.urlsafe_b64decode(encryptedData)) # Decode and parse the JSON string
        cryptedasdasdas1111 = json.loads(base64.urlsafe_b64decode(crypted0193[0])) # Decode and parse the JSON string
        asjdasjdajs = []
        asdasdasd = ""
        for data10 in cryptedasdasdas1111:
            crypt = RSA.import_key(myprivate.strip()) # Import the private key from PEM format
            cipher = PKCS1_v1_5.new(crypt) # Create a PKCS1_OAEP cipher object
            decryptedData1 = cipher.decrypt(base64.urlsafe_b64decode(base64.urlsafe_b64decode(data10)),None) # Decode and decrypt the data
            asdasdasd = asdasdasd + decryptedData1.decode() # Concatenate the decrypted data
        asjdasjdajs = asjdasjdajs + json.loads(asdasdasd) # Parse the JSON string and append to the list
        for data5 in asjdasjdajs:
            # var crypt123123123 = new JSEncrypt(); // RSA ile imzalamayı kaldır
            # crypt123123123.setPublicKey(key); // RSA ile imzalamayı kaldır
            signature = data5["sign"]
            plaintext = data5["text"]
            if ec_public_key.strip().decode().startswith("-----BEGIN PUBLIC KEY-----"):
                # assume it is PEM format
                verifying_key = ecdsa.VerifyingKey.from_pem(ec_public_key.strip())
                signature_bytes = bytes.fromhex(signature.strip())
                is_signature_valid = verifying_key.verify(signature_bytes, plaintext.encode(), hashfunc=hashlib.sha256)
            else:
                # assume it is hex format
                verifying_key = ecdsa.VerifyingKey.from_string(bytes.fromhex(ec_public_key.strip().decode()),curve=ecdsa.SECP256k1)
                signature_bytes = bytes.fromhex(signature.strip())
                is_signature_valid = verifying_key.verify(signature_bytes, plaintext.encode(), hashfunc=hashlib.sha256)
            if is_signature_valid:
                decryptedData += base64.urlsafe_b64decode(plaintext).decode() # Decode and append the plaintext to the decrypted data
            else:
                raise Exception("Invalid signature!")
    except Exception as e:
        print("Decryption failed! " + str(e))
    return decryptedData

data = None

with open("cb1.json", "r", encoding="utf-8") as f:
    data = json.load(f)

def multi_thread(text):
    global data
    cevap = ""
    metin = text.split()
    for key in data["multi"]:
        if key.startswith("set"):
            sub_keys = data["multi"][key].split("=")[-1].split()
            left_keyx = data["multi"][key].split("=")[0].split(",")
            for i in range(len(sub_keys)):
                for c in range(len(left_keyx)):
                    current_sub_key = sub_keys[i]
                    left_key = left_keyx[c].split("+")
                    if len(left_key) == 1:
                        for a in range(len(left_key)):
                            left_key1 = left_key[a].split("/")
                            for c in range(len(left_key1)):
                                if left_key1[c] in metin:
                                    response = data["multi"][current_sub_key.replace("$","")].split("/")
                                    if not any(item in cevap for item in response):
                                        if len(response) == 1:
                                            cevap += response[0] + " "
                                        else:
                                            cevap += random.choice(response) + " "
                    else:
                        sayac = 0
                        for a in range(len(left_key)):
                            left_key1 = left_key[a].split("/")
                            for c in range(len(left_key1)):
                                if left_key1[c] in metin:
                                    sayac=sayac+1
                        if len(left_key) == sayac:
                            response = data["multi"][current_sub_key.replace("$","")].split("/")
                            if not any(item in cevap for item in response):
                                sayac = 0
                                if len(response) == 1:
                                    cevap += response[0] + " "
                                else:
                                    cevap += random.choice(response) + " "
    if cevap == "":
        return None
    else:
        return cevap.strip() 

def single_thread(text):
    global data
    text = text.strip()
    if text in data["single"]:
        response = data["single"][text]
        if len(response) == 1:
            cevap = response[0] + " "
        else:
            cevap = random.choice(response) + " "
        return cevap.strip()
    else:
        return None

def cevapla(metin):
    global data
    cevap = ""
    test = single_thread(metin)
    if test is not None:
        return test
    test = multi_thread(metin)
    if test is not None:
        return test
    return random.choice(data["multi"]["default"]).strip()

#print(cevapla(input("Bot a sor : ")))

def encrypt(key, iv, plaintext):
    try:
        # Create AES-CBC cipher.
        cipher = AES.new(key, AES.MODE_CBC, iv)

        # Encrypt and return the IV and ciphertext.
        ciphertext = cipher.encrypt(pad(plaintext.encode(), AES.block_size))
        return ciphertext
    except Exception as e:
        print("Encryption error:", e)
        return None

def decrypt(key, iv, ciphertext):
    try:
        # Create AES-CBC cipher.
        cipher = AES.new(key, AES.MODE_CBC, iv)

        # Decrypt and return the plaintext.
        plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
        return plaintext.decode()
    except Exception as e:
        print("Decryption error:", e)
        return None

general_token = {}

def generatekey_general_token(key):
    global general_token
    name = ''.join(random.choices(string.ascii_letters + string.digits, k=256))
    general_token[name] = key.encode()
    if len(general_token) > 32:
        oldest_name = next(iter(general_token))
        del general_token[oldest_name]
    return name, key

def delete_general_token(token):
    global general_token
    if token in general_token:
        del general_token[token]
        return True
    else:
        return False

aes256_token = {}

def generatekeyAES256():
    global aes256_token
    key = ''.join(random.choices(string.ascii_letters + string.digits, k=32))
    name = ''.join(random.choices(string.ascii_letters + string.digits, k=64))
    aes256_token[name] = key.encode()
    if len(aes256_token) > 32:
        oldest_name = next(iter(aes256_token))
        del aes256_token[oldest_name]
    return name, key

def aes256_token_exists(name):
    global aes256_token
    return name in aes256_token

def delete_aes256_token(token):
    global aes256_token
    if token in aes256_token:
        del aes256_token[token]
        return True
    else:
        return False

def test_decrypt_aes256_token(token, ciphertext):
    global aes256_token, x1iv
    if not aes256_token_exists(token):
        return False
    try:
        decoded_ciphertext = base64.b64decode(ciphertext.encode())
        value = str(decrypt(aes256_token[token], x1iv.encode(), decoded_ciphertext))
        if delete_aes256_token(token):
            return value
        else:
            return False
    except:
        return False

def test_decrypt_aes256_token_wait(token, ciphertext):
    global aes256_token, x1iv
    if not aes256_token_exists(token):
        print("Token Bulunamadı")
        print(token)
        print(aes256_token)
        return False
    try:
        decoded_ciphertext = base64.b64decode(ciphertext.encode())
        value = str(decrypt(aes256_token[token], x1iv.encode(), decoded_ciphertext))
        return value
    except:
        print("Error Expect")
        return False

def generateToken_str():
    now = datetime.datetime.now()
    year = str(now.year)
    month = str(now.month).zfill(2)
    day = str(now.day).zfill(2)
    hour = str(now.hour).zfill(2)
    minute = str(now.minute).zfill(2)
    second = str(now.second).zfill(2)
    randomPassword = ''.join(random.choices(string.ascii_letters + string.digits, k=64))
    token = year + month + day + hour + minute + second + randomPassword
    return hashlib.sha256(token.encode()).hexdigest()

PASSWORD = generateToken_str()

SALT = generateToken_str()

# Global file_token list
file_token = {generateToken_str():"crypto-js.min.js",generateToken_str():"jquery-3.6.4.min.js",generateToken_str():"jsencrypt.min.js",generateToken_str():"abc.css",generateToken_str():"a.css",generateToken_str():"a1b.css",generateToken_str():"functions.js",generateToken_str():"elliptic.min.js",generateToken_str():"buffer-es@latest.js"}

# Global token list
tokens = []

def token_exists(token):
    for t in tokens:
        if t == token:
            return True
    return False
def generate_token(token_string):
    # Generate sha256 hash of the input string
    sha256_hash = hashlib.sha256(token_string.encode()).hexdigest()
    
    # Check if token already exists in the list
    if token_exists(sha256_hash):
        return "This token is already used"
    
    # Add the token to the beginning of the list
    tokens.insert(0, sha256_hash)
    
    # If the list has more than 32 tokens, remove the last one
    if len(tokens) > 32:
        tokens.pop()
    
    # Return the generated token
    return sha256_hash
def token_login(token_string):
    # Generate sha256 hash of the input string
    sha256_hash = hashlib.sha256(token_string.encode()).hexdigest()
    
    # Check if the token is in the list and remove it
    if sha256_hash in tokens:
        tokens.remove(sha256_hash)
        return True
    
    # If the token is not in the list, return False
    return False

def list_tokens():
    global tokens
    print(" >> Token list:")
    if tokens:
        for token in tokens:
            if token is not None:
                print(token)
    else:
        print("None")


# Global token list
invs = []

def inv_exists(token):
    for t in invs:
        if t == token:
            return True
    return False
def generate_inv():
    # Generate sha256 hash of the input string
    random_inv = base64.urlsafe_b64encode(os.urandom(48)).decode().replace('-', 'x').replace('_', 'a')
    
    # Check if token already exists in the list
    if inv_exists(random_inv):
        generate_inv()
        return "This inv is already used"
    
    # Add the token to the beginning of the list
    invs.insert(0, random_inv)
    
    # If the list has more than 32 invs, remove the last one
    if len(invs) > 32:
        invs.pop()
    
    # Return the generated token
    return random_inv
def inv_login(inv_string):
    # Check if the token is in the list and remove it
    if inv_string in invs:
        invs.remove(inv_string)
        return True
    
    # If the token is not in the list, return False
    return False
def list_inv():
    global invs,host,port
    print(" >> invs list:")
    if invs:
        for inv in invs:
            if inv is not None:
                print(f"http://{host}:{port}/?inv="+ inv)
    else:
        print("None")


def crc32bhash(string):

    # Calculate the CRC32b hash of the string.
    crc32b_hash = zlib.crc32(string)

    # Convert the CRC32b hash to a string.
    crc32b_hash_string = hex(crc32b_hash)[2:]

    # Return the CRC32b hash as a string.
    return crc32b_hash_string

server_memory_encrypt_key_Hash=None
server_memory_encrypt_iv_Hash=None
server_key=None
def set_memory_hash(text):
    global server_memory_encrypt_key_Hash,server_memory_encrypt_iv_Hash,server_key
    server_key = text
    key = hashlib.sha256(text.encode()).digest()
    iv = hashlib.md5(text.encode()).digest()
    server_memory_encrypt_key_Hash = hashlib.sha512(key).hexdigest()
    server_memory_encrypt_iv_Hash = hashlib.sha512(iv).hexdigest()
    return True
def set_password(text):
    global PASSWORD
    PASSWORD = text
    return True

def print_server_key():
    if server_memory_encrypt_key_Hash and server_memory_encrypt_iv_Hash:
        print(f' >> Server Key Hash: {server_memory_encrypt_key_Hash}{server_memory_encrypt_iv_Hash}')
    else:
        print(f' >> Server Key Hash: None')

def memory_key_generate(text):
    key = hashlib.sha256(text.encode()).digest()
    iv = hashlib.md5(text.encode()).digest()
    return key,iv

encrypted_messages = []
async def mesajat(message,key,iv, target,islem=0):
    if hashlib.sha512(key).hexdigest() == server_memory_encrypt_key_Hash and hashlib.sha512(iv).hexdigest() == server_memory_encrypt_iv_Hash:
        if len(key) != 32:
            return "Key size not suitable, must be 32 bytes"
        if len(iv) != 16:
            return "IV size is not appropriate, must be 16 bytes"
        crc32message=crc32bhash(message.encode())
        try:
            encrypted = base64.b64encode(encrypt(key, iv, message)).decode()
        except Exception as e:
            encrypted = colored_write(f" (!) Encryption error: {e}")
            return encrypted
        if islem==1:
            encrypted="___PUBLICKEY___"+encrypted
        new_add_data = {
        "crc32b": crc32message,
        "time": "19:06:08 10/04/2023",
        "id": "x",
        "text": encrypted,
        "type": "normal"
        }
        encrypted_messages.insert(0, new_add_data)
        if len(encrypted_messages) > 100:
            encrypted_messages.pop(-1)
        return "Message was sent to " + target
    else:
        return " (!) Server Key Error"

def mesajlari_oku(key,iv,encrypted_messages_cache):
    global server_memory_encrypt_key_Hash, server_memory_encrypt_iv_Hash
    if hashlib.sha512(key).hexdigest() == server_memory_encrypt_key_Hash and hashlib.sha512(iv).hexdigest() == server_memory_encrypt_iv_Hash:
        if len(key) != 32:
            return "Key size not suitable, must be 32 bytes"
        if len(iv) != 16:
            return "IV size is not appropriate, must be 16 bytes"
        decrypted_messages = []
        for message in encrypted_messages_cache:
            try:
                if message['text'].startswith("___PUBLICKEY___"):
                    messagexx = message['text'].split("___PUBLICKEY___")[1]
                    decrypted_message = decrypt(key, iv, base64.b64decode(messagexx))
                    if message['crc32b'] != crc32bhash(decrypted_message.encode()):
                        decrypted_messages.append('(!) CRC32B Error: Message changed')
                    else:
                        new_add_data = {
                            "crc32b": message['crc32b'],
                            "time": message['time'],
                            "id": message['id'],
                            "text": "___PUBLICKEY___"+decrypted_message,
                            "type": message['type']
                        }
                        decrypted_messages.append(new_add_data)
                else:
                    messagexx = message['text']
                    decrypted_message = decrypt(key, iv, base64.b64decode(messagexx))
                    if message['crc32b'] != crc32bhash(decrypted_message.encode()):
                        decrypted_messages.append('(!) CRC32B Error: Message changed')
                    else:
                        new_add_data = {
                            "crc32b": message['crc32b'],
                            "time": message['time'],
                            "id": message['id'],
                            "text": decrypted_message,
                            "type": message['type']
                        }
                        decrypted_messages.append(new_add_data)
            except Exception as e:
                decrypted_messages.append(f"Decrypt Error: {e}")
        return decrypted_messages
    else:
        return None

def print_decrypted_messages(decrypted_messages):
    if decrypted_messages==None:
        print(colored_write(" (!) Key Error"))
    elif decrypted_messages=="view":
        global encrypted_messages
        print(" >> Encrypted Data List:")
        if encrypted_messages:
            for message in encrypted_messages:
                if isinstance(message, dict) and 'time' in message and 'text' in message and 'id' in message and 'type' in message and 'crc32b' in message:
                    if message['text'].startswith("___PUBLICKEY___"):
                        messagexx = message['text'].split("___PUBLICKEY___")[1]
                        print(f"Data: ___PUBLICKEY___{messagexx}___END_PUBLICKEY___ {message['time']} ID:{message['id']} CRC32B:{message['crc32b']} {message['type']}")
                    else:
                        print(f"Data: {message['text']} {message['time']} ID:{message['id']} CRC32B:{message['crc32b']} {message['type']}")
                elif isinstance(message, str):
                    print(message)
                else:
                    print("Invalid message format")
        else:
            print("None")
    else:
        print(" >> Message List:")
        if decrypted_messages:
            for message in decrypted_messages:
                if isinstance(message, dict) and 'time' in message and 'text' in message and 'id' in message and 'type' in message and 'crc32b' in message:
                    if message['text'].startswith("___PUBLICKEY___"):
                        messagexx = message['text'].split("___PUBLICKEY___")[1]
                        print(f"___PUBLICKEY___{messagexx}___END_PUBLICKEY___ {message['time']} ID:{message['id']} CRC32B:{message['crc32b']} {message['type']}")
                    else:
                        print(f"Message: ___text___{message['text']}___end_text___ {message['time']} ID:{message['id']} CRC32B:{message['crc32b']} {message['type']}")
                elif isinstance(message, str):
                    print(message)
                else:
                    print("Invalid message format")
        else:
            print("None")

def return_decrypted_messages(decrypted_messages):
    cache_asdas_012302=""
    if decrypted_messages==None:
        cache_asdas_012302="(!) Key Error"
    else:
        if decrypted_messages:
            for message in decrypted_messages:
                if isinstance(message, dict) and 'time' in message and 'text' in message and 'id' in message and 'type' in message and 'crc32b' in message:
                    if message['text'].startswith("___PUBLICKEY___"):
                        messagexx = message['text'].split("___PUBLICKEY___")[1]
                        cache_asdas_012302 += (f"___PUBLICKEY___{messagexx}___END_PUBLICKEY___ {message['time']} ID:{message['id']} CRC32B:{message['crc32b']} {message['type']}") + "<br>"
                    else:
                        cache_asdas_012302 += (f"___text___{message['text']}___end_text___ {message['time']} ID:{message['id']} CRC32B:{message['crc32b']} {message['type']}") + "<br>"
                elif isinstance(message, str):
                    cache_asdas_012302 += (message) + "\n"
                else:
                    cache_asdas_012302 += ("Invalid message format") + "<br>"
        else:
            cache_asdas_012302 = ("None")
    return cache_asdas_012302

def return_broadcast_messages(key, iv):
    global encrypted_messages
    messages = []
    if encrypted_messages:
        messages.append(encrypted_messages[0])
        cache_asdas_012302 = ""
        try:
            for message in messages:
                if message['text'].startswith("___PUBLICKEY___"):
                    messagexx = message['text'].split("___PUBLICKEY___")[1]
                    decrypted_message = decrypt(key, iv, base64.b64decode(messagexx))
                    if message['crc32b'] != crc32bhash(decrypted_message.encode()):
                        cache_asdas_012302 += '(!) CRC32B Error: Message changed\n'
                    else:
                        cache_asdas_012302 += f"___PUBLICKEY___{decrypted_message}___END_PUBLICKEY___ {message['time']} ID:{message['id']} CRC32B:{message['crc32b']} {message['type']}\n"
                else:
                    messagexx = message['text']
                    decrypted_message = decrypt(key, iv, base64.b64decode(messagexx))
                    if message['crc32b'] != crc32bhash(decrypted_message.encode()):
                        cache_asdas_012302 += '(!) CRC32B Error: Message changed\n'
                    else:
                        cache_asdas_012302 += f"___text___{decrypted_message}___end_text___ {message['time']} ID:{message['id']} CRC32B:{message['crc32b']} {message['type']}\n"
        except Exception as e:
            cache_asdas_012302 += f"Decrypt Error: {e}\n"
        if not messages:
            cache_asdas_012302 = "None"
        return cache_asdas_012302
    else:
        return None

def get_token_variables(file_token):
    tokens = list(file_token.keys())
    return tuple(tokens)

random_token=None
class StaticServer(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        return
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.directory = 'www'
    def do_GET(self):
        global random_token
        token1 = self.path[1:]
        if token1 in file_token:
            file_name = file_token[token1]
            file_extension = os.path.splitext(file_name)[1]
            if file_extension == '.css':
                file_type = 'text/css'
            elif file_extension == '.js':
                file_type = 'text/javascript'
            else:
                file_type = 'text/plain'
            try:
                file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'www', file_name)
                with open(file_path, 'rb') as file:
                    content = file.read()
                    self.send_response(200)
                    self.send_header('Content-type', file_type)
                    self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
                    self.send_header('Expires', '0')
                    self.send_header('Pragma', 'no-cache')
                    self.end_headers()
                    self.wfile.write(content)
            except:
                self.send_error(404)
            return
        if self.path == '/':
            self.path = '/index.html'
            try:
                file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'www', self.path[1:])
                if not os.path.exists(file_path):
                    raise Exception(f'File "{file_path}" not found!')
                with open(file_path, 'rb') as file:
                    content = file.read()
                self.send_response(200)
                self.send_header('Content-Type', 'text/html')
                self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
                self.send_header('Expires', '0')
                self.send_header('Pragma', 'no-cache')
                self.end_headers()
                self.wfile.write(content)
            except Exception as e:
                self.send_error(404, f'Error: {e}')
        elif self.path.startswith('/?token='):
            token = self.path.split('=')[1]
            if token == random_token:
                message = 'Please set the server key:'
                content = f'''
                <html>
                    <body>
                        <h2>{message}</h2>
                        <form method="post" action="/{nametoken_cache}">
                            <input type="text" name="server_key" id="server_key" autocomplete="off">
                            <input type="submit">
                        </form>
                    </body>
                </html>
                '''
                self.send_response(200)
                self.send_header('Content-Type', 'text/html')
                self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
                self.send_header('Expires', '0')
                self.send_header('Pragma', 'no-cache')
                self.end_headers()
                self.wfile.write(content.encode())
                return
            else:
                return
        elif self.path.startswith('/?inv='):
            if server_key == None:
                self.send_response(200)
                self.send_header('Content-Type', 'text/html')
                self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
                self.send_header('Expires', '0')
                self.send_header('Pragma', 'no-cache')
                self.end_headers()
                self.wfile.write("Server Key Not Found".encode())
                return
            inv = self.path.split('=')[1]
            if inv_login(inv):
                token1, token2, token3, token4, token5, token6, token7, token8, token9 = get_token_variables(file_token)
                namex89, keyx98 = generatekeyAES256()
                #print(x1iv)
                #print("KEY:"+keyx98)
                #asdasdas = base64.b64encode(encrypt(keyx98.encode(), x1iv.encode(), "123")).decode()
                #print(asdasdas)
                #print(decrypt(keyx98.encode(), x1iv.encode(), base64.b64decode(asdasdas)))
                keyx98 = keyx98.encode().hex()
                namex89 = namex89

                namex89_public_key, keyx98_public_key = generatekeyAES256()
                keyx98_public_key = keyx98_public_key.encode().hex()
                namex89_public_key = namex89_public_key

                namexserver_key, keyxserver_key = generatekeyAES256()
                server_key_token_encrypted = namexserver_key + "#" + base64.b64encode(encrypt(keyxserver_key.encode(), x1iv.encode(), server_key)).decode()

                namexdecrypt_server_key, keyxdecrypt_server_key = generatekeyAES256()
                decrypt_server_key_token_encrypted = namexdecrypt_server_key + "#" + base64.b64encode(encrypt(keyxdecrypt_server_key.encode(), x1iv.encode(), server_key)).decode()
                #asdasdas = base64.b64encode(encrypt(keyxserver_key.encode(), x1iv.encode(), server_key)).decode()
                #print(decrypt(keyxserver_key.encode(), x1iv.encode(), base64.b64decode(asdasdas)))
                content = f'''
<!DOCTYPE html>
<html>
<head>
    <link rel="icon" href="">
    <meta charset="utf-8">
    <title> </title>
    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=0">
    <meta http-equiv="pragma" content="no-cache">
    <meta name="subject" content="">
    <meta name="description" content="">
    <Meta name="Classification" content="">
    <Meta name="rating" content="">
    <meta name="category" content="">
    <meta name="keywords" content="">
    <meta name="author" content="">
    <meta name="robots" content="index, follow">
    <meta http-equiv="content-type" content="text/html;UTF-8">
    <meta http-equiv="content-language" content="en">
    <meta http-equiv="expires" content="">
    <meta http-equiv="revisit-after" content="">
    <script>
    var decrypt_location = "/{namedecrypt_cache}";
    var token_location = "/{nametokenpost_cache}";

    var server_key = "{server_key}";
    var decrypt_server_key_x = "{decrypt_server_key_token_encrypted}";
    var encrypt_1_iv = "{x1iv.encode().hex()}";

    safe_thread_ok=false;
    </script>
    <script src="/{token9}"></script>
    <script src="/{token1}"></script>
    <script src="/{token2}"></script>
    <script type="text/javascript" src="/{token3}"></script>
    <link rel="stylesheet" href="/{token4}">
    <link rel="stylesheet" href="/{token5}">
    <link rel="stylesheet" href="/{token6}">
    <script src="/{token8}"></script>
    <script src="/{token7}"></script>
    
</head>
<body style="background-color:black!important;">
<serverpublickey style='display:none'>{public_key_pem.decode()}</serverpublickey>
<mypublicelliptic style='display:none'></mypublicelliptic>
<myprivateelliptic style='display:none'></myprivateelliptic>
<div id="deathpage" style="display:none;color:white;">
<h1>Connection Was Slained By Server :(</h1>
</div>
<div id="loading" style="display: none;position: absolute;top: 0;left: 0;z-index: 100;width: 100vw;height: 100vh;background-color: black;background-repeat: no-repeat;background-position: center;"><div style="margin:0 auto;text-align:center;height:auto;"><br><br><!-- SPINNER ORBITS -->
<div class="spinner-box">
  <div class="blue-orbit leo">
  </div>

  <div class="green-orbit leo">
  </div>
  
  <div class="red-orbit leo">
  </div>
  
  <div class="white-orbit w1 leo">
  </div><div class="white-orbit w2 leo">
  </div><div class="white-orbit w3 leo">
  </div>
</div><br><loading-durum style='color:white;margin:0 auto;font-size:24px;'>Your friend didn't come or Your Processor Is Used For RSA 2048 Bit Encryption Key Generation</loading-durum></div></div>
<script>
var safe_retry_rsa=true;
function changedurum(asdasdasdadasd){{
    $("loading-durum").html(asdasdasdadasd);
}}
  function setVisible(selector, visible) {{
  document.querySelector(selector).style.display = visible ? 'block' : 'none';
}}
function killpage(){{
  setVisible('main', false);
  setVisible('#loading', false);
setVisible('#deathpage', true);
}}
function openloading(){{
  setVisible('main', false);
  setVisible('#loading', true);
}}
function closeloading(){{
  setVisible('main', true);
  setVisible('#loading', false);
}}
</script>
<main>
<div style="margin:0 auto;text-align:center;height:auto;color:grey;max-width:600px;">
<div style="margin:0 auto;text-align:center;height:auto;">
<mypublic style='display:none'></mypublic>
<myprivate style='display:none'></myprivate>
<targetpublic id='targetpublic' style='display:none'></targetpublic>
<form id="message-form">
<div id="asdasds" style="display: flex; align-items: center; width: 600px;">
<textarea spellcheck='false' type="text" id="message-input" class="textareaxx asdas1c" placeholder="Send Message" style="height:59px;display:block;font-size:16px;font-weight:1000;width:100%;border:0;background-color:transparent;border:0;margin:0;border-bottom:2.5px solid dimgrey;padding:16px;color:white!important;resize: vertical!important;" autocomplete="off" autofocus required></textarea>
<input type="submit" id="message-submit" value=">" style="margin:0;font-size:16px;font-weight:1000;width:40px;border:0;background-color:transparent;border-bottom:2.5px solid dimgrey;padding:16px;color:white!important;height:59px!important;">
</div>
<input type="text" id="target-input" value="a" style="display:none" required></form>
<div id="messages" style="word-wrap: break-word;"></div>
<button onclick="keychange()">Public,Private key Change</Button>
<script>
$(document).ready (function() {{
    console.log('x1');

var submit = document.getElementById("message-submit");

var textarea = document.getElementById("message-input");
var height = textarea.clientHeight;
textarea.addEventListener("mouseup", function() {{
  if (height != textarea.clientHeight) {{
    submit.style.setProperty("height", (textarea.clientHeight+2) + "px", "important");
  }}
  height = textarea.clientHeight;
}});

}});
// özel ve açık anahtarlarını oluştur
var EC = elliptic.ec;
var ec = new EC('secp256k1');
var key = ec.genKeyPair();
var privKey = key.getPrivate().toString(16);
var pubKey = key.getPublic().encode('hex');
$("mypublicelliptic").html(pubKey);
$("myprivateelliptic").html(privKey);
function sendMessage(message1, target, keyx,gorunum=1,latest=false) {{
  var payload = `${{message1}}:${{target}}:${{keyx}}`;
  payload = encryptDataserver(payload,$("serverpublickey").html());
  socket.send(payload);
  if (gorunum==1){{
  var messages = document.querySelector('#messages');
  var messagex = document.createElement('div');
  messagex.style.display = "block";
  //message1="(Encrypted)";
  //messagex.innerHTML = "Mesaj Gönderildi => <textarea spellcheck='false' style='color:grey;overflow: hidden;resize: vertical;'>"+message1+"</textarea> "+getCurrentTime()+" ID: "+target;
  if(latest!=false){{
  messagex.innerHTML = "<p class='a lf'><label id='f1'>"+"You : " + "<textarea spellcheck='false' class='textareaxx'>"+ latest + "</textarea>"  + "</label></p><p class='rg' style='color:grey;border:none!important;z-index:2;'>" + getCurrentTime()+" ID: "+target+"</p>";
  }}else{{
  messagex.innerHTML = "Mesaj Gönderildi " + getCurrentTime()+" ID: "+target;
  }}
  messages.insertBefore(messagex, messages.firstChild);
  message1="";
  }}
}}
var wait=true;
function keychange(){{
    wait=true;
    safe_retry_rsa=true;
    openloading();
    var targetInput = document.querySelector('#target-input');
    var target = targetInput.value;
    var keypublic;
    var keyprivate;
    var crypt9 = new JSEncrypt({{default_key_size: 2048}});
    new Promise((resolve)=>{{
    setTimeout(resolve, 100);
    }}).then( async()=>{{
        crypt9.getKey();
    }}).finally(() => {{
        keypublic = crypt9.getPublicKey();
        keyprivate = crypt9.getPrivateKey();
        var interval123 = setInterval(() => {{
        if(keypublic != undefined && keyprivate != undefined){{
            clearInterval(interval123);
            var securemessage=encryptData(keypublic,$('targetpublic').html(),$('myprivate').html());
            sendMessage("___key_change1___"+securemessage+"___end_key_change1___", target, server_key,1,"#Public Key Request");
            var interval1 = setInterval(() => {{
                if(wait==false){{
                    clearInterval(interval1);
                    $('myprivate').html(keyprivate);
                    $('mypublic').html(keypublic);
                }}
            }}, 100);
        }}
    }}, 3000);
    }});
}}
  const socket = new WebSocket('ws://'+window.location.hostname+':{str(WEBSOCKET_PORT)}');

  socket.onopen = function(event) {{
    var keyx="{server_key_token_encrypted}";
    console.log('WebSocket connection is open');
    promptUser('Enter Password:')
  .then(passx => {{
    if(passx != "" && passx != null && passx != undefined && passx != " "){{
        var namex89_public_key = "{namex89_public_key}";
        var keyx98_public_key = "{keyx98_public_key}";
        var encrypted_name_public_key = "{namex89_public_key}";
        var encrypt_key_public_key ="{keyx98_public_key}";
        var text12123213_public_key = encrypted_name_public_key+"#"+encrypt_1(keyx98_public_key,encrypt_1_iv,$("mypublicelliptic").html());
        socket.send(`${{text12123213_public_key}}`);

        var encrypted_name = "{namex89}";
        var encrypt_key ="{keyx98}";
        var text12123213 = encryptDataserver(encrypted_name+"#"+encrypt_1(encrypt_key,encrypt_1_iv,passx),$("serverpublickey").html());
        socket.send(`${{text12123213}}`);
        var keyx12312312 = encryptDataserver(keyx,$("serverpublickey").html());
        socket.send(`${{keyx12312312}}`);
        openloading();
        key_gen_main(false);
    }}else{{
        killpage();
    }}
  }})
  .catch(error => {{
    killpage();
    console.error(error);
  }});
  }};
socket.onmessage = function(event) {{

// start-3
  var messages = document.querySelector('#messages');
  var message = document.createElement('div');
  message.style.display = "block";
  if (event.data.startsWith("___PUBLICKEY___") && event.data.includes("___END_PUBLICKEY___")) {{ // başlangıç ve bitiş kısmının varlığını kontrol et
closeloading();
  var startIndex = event.data.indexOf("___PUBLICKEY___") + "___PUBLICKEY___".length; // başlangıç kısmının sonundaki indeksi bul
  var endIndex = event.data.indexOf("___END_PUBLICKEY___"); // bitiş kısmının başındaki indeksi bul
  var messagexx = event.data.slice(startIndex, endIndex); // aradaki kısmı al
  var div = document.getElementById("targetpublic");
  if(safe_retry_rsa==true){{
    console.log("success 1");
              safe_retry_rsa=false;
div.innerHTML = messagexx;
            }}
}}
else {{
if (event.data.startsWith("___text___") && event.data.includes("___end_text___")) {{
  var startIndex = event.data.indexOf("___text___") + "___text___".length;
  var endIndex = event.data.indexOf("___end_text___");
  var messagexx = event.data.slice(startIndex, endIndex);

  var endIndex1 = event.data.indexOf("___end_text___");
  var sonradata = event.data.slice(endIndex1 + "___end_text___".length);
  if(messagexx.startsWith("___key_change1___") && messagexx.includes("___end_key_change1___")){{
    safe_retry_rsa=true;
    openloading();
    var startIndex2 = messagexx.indexOf("___key_change1___") + "___key_change1___".length;
    var endIndex2 = messagexx.indexOf("___end_key_change1___");
    var messagexx = messagexx.slice(startIndex2, endIndex2);
    var publickeytargetsadasdas1 = decryptData(messagexx,$('targetpublic').html(),$('myprivate').html());
    var targetInput = document.querySelector('#target-input');
    var target = targetInput.value;
    var keypublic;
    var keyprivate;
    var crypt9 = new JSEncrypt({{default_key_size: 2048}});
    new Promise((resolve)=>{{
    setTimeout(resolve, 500);
    }}).then( async()=>{{
        crypt9.getKey();
    }}).finally(() => {{
        keypublic = crypt9.getPublicKey();
        keyprivate = crypt9.getPrivateKey();
        var div = document.getElementById("targetpublic");
        var interval12 = setInterval(() => {{
        if(keypublic != undefined && keyprivate != undefined){{
            clearInterval(interval12);
            var securemessage=encryptData(keypublic,$('targetpublic').html(),$('myprivate').html())
            sendMessage("___key_change2___"+securemessage+"___end_key_change2___", target, server_key,1,"#Public Key Request");
            $('myprivate').html(keyprivate);
            $('mypublic').html(keypublic);
            div.innerHTML = publickeytargetsadasdas1;
            closeloading();
        }}
    }}, 500);
    }});
  }}else if(messagexx.startsWith("___key_change2___") && messagexx.includes("___end_key_change2___")){{
    var startIndex3 = event.data.indexOf("___key_change2___") + "___key_change2___".length; // başlangıç kısmının sonundaki indeksi bul
    var endIndex3 = event.data.indexOf("___end_key_change2___"); // bitiş kısmının başındaki indeksi bul
    var messagexx1 = event.data.slice(startIndex3, endIndex3); // aradaki kısmı al
    var publickeytargetsadasdas1 = decryptData(messagexx1,$('targetpublic').html(),$('myprivate').html());
    var div = document.getElementById("targetpublic");
    if(safe_retry_rsa==true){{
        safe_retry_rsa=false;
        div.innerHTML = publickeytargetsadasdas1;
        wait=false;
        closeloading();
    }}
  }}else{{
    var messagecbbtbtnrte = decryptData(messagexx,$('targetpublic').html(),$('myprivate').html());
    message.innerHTML = "<p class='a rg'><label id='f1'>"+"<textarea spellcheck='false' class='textareaxx'>"+messagecbbtbtnrte+"</textarea>"+"</label></p><p class='rg' style='color:grey;border:none!important;z-index:2;'>"+sonradata+"</p>";
    messages.insertBefore(message, messages.firstChild);    
  }}


  }}else{{
    message.innerHTML = "<textarea spellcheck='false' class='textareaxx'>"+event.data+"</textarea>";
    messages.insertBefore(message, messages.firstChild);
  }}
}}

// end-3

}};

  socket.onerror = function(error) {{
    console.error('WebSocket error: ', error);
  }};

  socket.onclose = function(event) {{
    console.log('WebSocket connection is closed with code ', event.code);
    closeloading();
    killpage();
  }};

var form = document.querySelector('#message-form');
form.addEventListener('submit', function(event) {{
  event.preventDefault();
  var messageInput = document.querySelector('#message-input');
  var targetInput = document.querySelector('#target-input');
  var messagex2 = messageInput.value;
  var target = targetInput.value;
  messagex=encryptData(messagex2,$('targetpublic').html(),$('myprivate').html())
  sendMessage(messagex, target, server_key,1,messagex2);
  messageInput.value = '';
  messagex2="";
  messagex="";
}});
</script>



  <form onsubmit="return decrypt();">
    <label for="serverkey">Server Key:</label>
    <input type="text" name="serverkey" id="serverkey" value="">
    <br>
    <button type="submit">Submit</button>
  </form>
  <div id="resultmessage"></div>
  <form onsubmit="return sendToken();">
    <label for="token">Token:</label>
    <input type="text" name="token" id="token" value="">
    <br>
    <button type="submit">Submit</button>
  </form>
  <div id="resulttoken"></div>
  <form onsubmit="return sendRSA();">
    <label for="myrsapublic">My Public Key:</label><br>
    <textarea spellcheck='false' name="myrsapublic" id="myrsapublic"></textarea>
    <br>
    <label for="myrsaprivate">My Private Key:</label><br>
    <textarea spellcheck='false' name="myrsaprivate" id="myrsaprivate"></textarea>
    <button type="submit">Submit</button>
  </form>
  <div id="resultrsa"></div>
  <form onsubmit="return sendForm();">
    <label for="message">Mesaj At:</label>
    <input type="text" name="message" id="message">
    <br>
    <label for="key">Server key:</label>
    <input type="text" name="key" id="key" value="">
    <br>
    <label for="target">Target:</label>
    <select name="target" id="target" required>
      <option value="">Select an target</option>
      <option value="m2a">A</option>
      <option value="m2b">B</option>
    </select>
    <br>
    <button type="submit">Submit</button>
  </form>
  <div id="result"></div>
  </div>
</div>
</main>
</body>
</html>
                '''
                self.send_response(200)
                self.send_header('Content-Type', 'text/html')
                self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
                self.send_header('Expires', '0')
                self.send_header('Pragma', 'no-cache')
                self.end_headers()
                self.wfile.write(content.encode())
                return
            else:
                self.send_response(404)
                return
        else:
            self.send_response(404)
            return
    def do_POST(self):
        global random_token
        token1 = self.path[1:]
        if token1 in general_token:
            g_name = general_token[token1].decode()
            if g_name == "#submit":
                content_length = int(self.headers.get('Content-Length', 0))
                post_data = self.rfile.read(content_length)
                post_data = parse_qs(post_data.decode())
                token = post_data.get('token', [''])[0]
                if token_login(token):
                    message = post_data.get('message', [''])[0]
                    keyx = post_data.get('key', [''])[0]
                    key,iv=memory_key_generate(keyx)
                    target = post_data.get('target', [''])[0]
                    if target not in ['m2a', 'm2b']:
                        error_message = "Invalid Target. The Target parameter must have a value of either 'm2a' or 'm2b'."
                        self.send_response(200)
                        self.send_header('Content-type', 'text/html')
                        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
                        self.send_header('Expires', '0')
                        self.send_header('Pragma', 'no-cache')
                        self.end_headers()
                        self.wfile.write(error_message.encode())
                        return
                    if target == 'm2a':
                        asyncio.run(mesajat(message,key,iv,"a",0))
                    elif target == 'm2b':
                        asyncio.run(mesajat(message,key,iv,"b",0))
                    else:
                        text = 'Target Invalid'
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
                    self.send_header('Expires', '0')
                    self.send_header('Pragma', 'no-cache')
                    self.end_headers()
                    self.wfile.write("Mesaj Gönderildi".encode())
                    return
                else:
                    self.send_response(404)
                return
            if g_name == "#tokenpost":
                content_length = int(self.headers.get('Content-Length', 0))
                post_data = self.rfile.read(content_length)
                post_data = json.loads(post_data)
                token = post_data.get('token', None)
                #print("Token:"+token)
                text = generate_token(token)
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
                self.send_header('Expires', '0')
                self.send_header('Pragma', 'no-cache')
                self.end_headers()
                self.wfile.write(text.encode())
            if g_name == "#decrypt":
                content_length = int(self.headers.get('Content-Length', 0))
                post_data = self.rfile.read(content_length)
                post_data = json.loads(post_data)
                token = post_data.get('token', None)
                #print("Token2:"+token)
                if token_login(token):
                    keyx = post_data.get('key', None)
                    if "#" in keyx:
                        parts = keyx.split("#")
                        if len(parts) == 2:
                            keyx = test_decrypt_aes256_token_wait(parts[0],parts[1])
                            if keyx != None and keyx != False:
                                #print("Keyx:"+keyx)
                                key,iv=memory_key_generate(keyx)
                                dec_server_data=return_decrypted_messages(mesajlari_oku(key, iv,encrypted_messages[::-1]))
                                if dec_server_data != None and dec_server_data != False and dec_server_data != "None":
                                    delete_aes256_token(parts[0])
                                    #print(dec_server_data)
                                    self.send_response(200)
                                    self.send_header('Content-type', 'text/html')
                                    self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
                                    self.send_header('Expires', '0')
                                    self.send_header('Pragma', 'no-cache')
                                    self.end_headers()
                                    self.wfile.write(dec_server_data.encode())
                                    return
                                else:
                                    self.send_response(200)
                                    self.send_header('Content-type', 'text/html')
                                    self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
                                    self.send_header('Expires', '0')
                                    self.send_header('Pragma', 'no-cache')
                                    self.end_headers()
                                    self.wfile.write("None".encode())
                                    return
                            else:
                                self.send_response(200)
                                self.send_header('Content-type', 'text/html')
                                self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
                                self.send_header('Expires', '0')
                                self.send_header('Pragma', 'no-cache')
                                self.end_headers()
                                self.wfile.write("None".encode())
                                return
                        else:
                            print("hata 2")
                            self.send_response(404)
                            return
                    else:
                        print("hata 3")
                        self.send_response(404)
                        return
                else:
                    print("hata 4")
                    self.send_response(404)
                    return
        if token1 == random_token:
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            post_data = parse_qs(post_data.decode())
            new_server_key = post_data.get('server_key', [''])[0]
            set_password(new_server_key)
            set_memory_hash(new_server_key + SALT)
            random_token = None
            message = f'OK'
            content = f'''
                <html>
                    <head>
                        <title>Success</title>
                        <meta charset="UTF-8">
                    </head>
                    <body onclick="location.reload();">
                        <h2>{message}</h2>
                        <h2>{server_memory_encrypt_key_Hash}{server_memory_encrypt_iv_Hash}</h2>
                        <button onclick="location.reload();">Sayfayı Kapat</button>
                        <script>
                        window.addEventListener('click', function() {{
                            location.reload();
                        }});
                        var asdasd=0;
                        window.addEventListener('mousemove', function() {{
                            if(asdasd==0){{
                                location.reload();
                                asdasd++;
                            }}
                        }});
                        </script>
                    </body>
                </html>
            '''
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
            self.send_header('Expires', '0')
            self.send_header('Pragma', 'no-cache')
            self.end_headers()
            self.wfile.write(content.encode())
            return
        if self.path == '/speech':
            global host,port,chatbotinvtext
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length)
            post_data = parse_qs(post_data.decode())
            inv = post_data.get('speech', [''])[0]
            if inv == chatbotinvtext:
                print("")
                print(colored_write_ok(" >> Magic Word: Backdoor Access"))
                chatbotinvtext = ''.join(random.choices(string.ascii_letters + string.digits, k=512))
                print(colored_write_ok(" >> Magic Word: Deleted"))
                print("EncryptedChat@Python > ", end="")
                sys.stdout.flush()
                text = generate_inv()
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
                self.send_header('Expires', '0')
                self.send_header('Pragma', 'no-cache')
                self.end_headers()
                self.wfile.write(f"<input type='button' value=\"Hidden Tunnel\" onclick=\"window.location='/?inv=".encode()+text.encode()+"';\">".encode())
                return
            else:
                textx = cevapla(inv)
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
                self.send_header('Expires', '0')
                self.send_header('Pragma', 'no-cache')
                self.end_headers()
                self.wfile.write(textx.encode())
                return
            

host = '127.0.0.1'
WEBSOCKET_PORT = 5678
CONNECTION_LIMIT = 2

connected_users = 0
connected = set()
websocket_is_open = {}
websocket_lock = asyncio.Lock()
shutdown_event = asyncio.Event()
websocket_task = None

async def public_key_request_test(websocket):
    try:
        user_public_key = await websocket.recv()
        if "#" in user_public_key:
            parts = user_public_key.split("#")
            if len(parts) == 2:
                user_public_key = test_decrypt_aes256_token(parts[0],parts[1])
                if user_public_key != False:
                    return user_public_key
                else:
                    return False
            else:
                return False
        else:
            return False
    except Exception as e:
        return False

async def authenticate(websocket,public_key):
    global private_key_pem
    try:
        user_password = await websocket.recv()
        user_password = await decryptDataserver(user_password,private_key_pem,public_key.encode())
        if "#" in user_password:
            parts = user_password.split("#")
            if len(parts) == 2:
                user_password = test_decrypt_aes256_token(parts[0],parts[1])
                if user_password != PASSWORD:
                    return False
                return True
            else:
                return False
        else:
            return False
    except Exception as e:
        return False

async def handler(websocket, path):
    global connected_users, encrypted_messages,__process_close__
    public_key = await public_key_request_test(websocket)
    if not public_key:
        await websocket.close()
        return
    authenticated = await authenticate(websocket,public_key)
    if not authenticated:
        await websocket.close()
        return
    async with websocket_lock:
        if connected_users >= CONNECTION_LIMIT:
            await websocket.close(1000,"connection_limit_exceeded")
            return
        connected_users += 1
        connected.add(websocket)
        websocket_is_open.update({websocket: True})
    await asyncio.create_task(some_coroutine(websocket))
    await websocket.send("connection_successful")
    key, iv = await get_key_and_iv(websocket,public_key)
    if key is None or iv is None:
        async with websocket_lock:
            connected.remove(websocket)
            websocket_is_open.pop(websocket, None)
        await websocket.close(1000,"error_occurred")
        return
    try:
        async for message in websocket:
            #print(str(websocket) + " => "+ message)
            islem=0
            message = await decryptDataserver(message,private_key_pem,public_key.encode())
            message_data = message.split(":")
            if len(message_data) >= 2:
                message1 = message_data[0]
                if message1.startswith("___PUBLICKEY___"):
                    message1 = message1.split("___PUBLICKEY___")[1]
                    islem=1
                target = message_data[1]
            else:
                target = None
            if islem==0:
                if hashlib.sha512(key).hexdigest() == server_memory_encrypt_key_Hash and hashlib.sha512(iv).hexdigest() == server_memory_encrypt_iv_Hash:
                    await mesajat(message1, key, iv, target,0)
                else:
                    async with websocket_lock:
                        connected.remove(websocket)
                        websocket_is_open.pop(websocket, None)
                        connected_users -= 1
                        return
            else:
                if hashlib.sha512(key).hexdigest() == server_memory_encrypt_key_Hash and hashlib.sha512(iv).hexdigest() == server_memory_encrypt_iv_Hash:
                    await mesajat(message1, key, iv, target,1)
                else:
                    async with websocket_lock:
                        connected.remove(websocket)
                        websocket_is_open.pop(websocket, None)
                        connected_users -= 1
                        return
            await broadcast(message, websocket, key, iv)
    except websockets.exceptions.ConnectionClosed:
        async with websocket_lock:
            connected.remove(websocket)
            websocket_is_open.pop(websocket, None)
            connected_users -= 1
            if __process_close__ == 0:
                __process_close__ = 1
                # Tüm soketleri kapatmak için önce kapatılabileceklerini kapatın
                tasks = [websocket.close() for websocket in connected if not websocket.closed]
                await asyncio.gather(*tasks, return_exceptions=True)
                # Kapatılamayan soketler için bekleyin
                for websocket in connected:
                    if not websocket.closed:
                        try:
                            await asyncio.wait_for(websocket.wait_closed(), timeout=2)
                        except asyncio.TimeoutError:
                            await websocket.close()
                encrypted_messages = []
                __process_close__ = 0
                return
    except asyncio.TimeoutError:
        async with websocket_lock:
            connected.remove(websocket)
            websocket_is_open.pop(websocket, None)
            connected_users -= 1
            if __process_close__ == 0:
                __process_close__ = 1
                # Tüm soketleri kapatmak için önce kapatılabileceklerini kapatın
                tasks = [websocket.close() for websocket in connected if not websocket.closed]
                await asyncio.gather(*tasks, return_exceptions=True)
                # Kapatılamayan soketler için bekleyin
                for websocket in connected:
                    if not websocket.closed:
                        try:
                            await asyncio.wait_for(websocket.wait_closed(), timeout=2)
                        except asyncio.TimeoutError:
                            await websocket.close()
                encrypted_messages = []
                __process_close__ = 0
                return
    finally:
        try:
            async with websocket_lock:
                connected.remove(websocket)
                websocket_is_open.pop(websocket, None)
                connected_users -= 1
                if __process_close__ == 0:
                    __process_close__ = 1
                    # Tüm soketleri kapatmak için önce kapatılabileceklerini kapatın
                    tasks = [websocket.close() for websocket in connected if not websocket.closed]
                    await asyncio.gather(*tasks, return_exceptions=True)
                    # Kapatılamayan soketler için bekleyin
                    for websocket in connected:
                        if not websocket.closed:
                            try:
                                await asyncio.wait_for(websocket.wait_closed(), timeout=2)
                            except asyncio.TimeoutError:
                                await websocket.close()
                    encrypted_messages = []
                    __process_close__ = 0
                    return
        except:
            pass
async def broadcast(message, sender, key, iv):
    global encrypted_messages
    messages = return_broadcast_messages(key, iv)
    if messages != None:
        tasks = []
        if connected.__len__() % 2 == 0:
            if not messages.startswith("___PUBLICKEY___"):
                encrypted_messages = []
        for websocket in list(connected):
            try:
                if websocket != sender and websocket_is_open.get(websocket, False):
                    task = websocket.send(messages)
                    tasks.append(task)
            except:
                pass
        await asyncio.gather(*tasks, return_exceptions=True)

async def some_coroutine(websocket):
    async with websocket_lock:
        websocket_is_open[websocket] = True

async def start_websocket_server(shutdown_event):
    global __process_close__
    async with websockets.serve(handler, host, WEBSOCKET_PORT):
        async with websocket_lock:
            for websocket in connected:
                websocket_is_open[websocket] = True
        while True:
            await asyncio.sleep(1) # her saniyede bir soketleri kontrol edin
            async with websocket_lock:
                for websocket in connected:
                    if not websocket.closed:
                        websocket_is_open[websocket] = True
            if shutdown_event.is_set():
                # Tüm soketleri kapatmak için önce kapatılabileceklerini kapatın
                if __process_close__ == 0:
                    __process_close__ = 1
                    tasks = [websocket.close() for websocket in connected if not websocket.closed]
                    await asyncio.gather(*tasks, return_exceptions=True)
                    # Kapatılamayan soketler için bekleyin
                    for websocket in connected:
                        if not websocket.closed:
                            try:
                                await asyncio.wait_for(websocket.wait_closed(), timeout=2)
                            except asyncio.TimeoutError:
                                await websocket.close()
                    __process_close__ = 0
                async with websocket_lock:
                    connected.clear()
                    websocket_is_open.clear()
                shutdown_event.clear()
                print(colored_write_ok(' >> WebSocket Server stopped.'))
                break


async def close_websocket_server():
    global shutdown_event
    shutdown_event.set()
    print(' >> Stopping WebSocket Server...')


async def main(shutdown_event):
    global websocket_task
    websocket_task = asyncio.create_task(start_websocket_server(shutdown_event))
    await shutdown_event.wait()
    await asyncio.gather(websocket_task, return_exceptions=True)

def start_server():
    asyncio.run(main(shutdown_event))

async def close_server():
    loop = asyncio.get_event_loop()
    await close_websocket_server()
    tasks = [task for task in asyncio.all_tasks() if task is not asyncio.current_task()]
    [task.cancel() for task in tasks]
    await asyncio.gather(*tasks, return_exceptions=True)
    loop.stop()

def start_x1(): # Start Function
    global server_thread1, shutdown_event
    shutdown_event = asyncio.Event()
    server_thread1 = threading.Thread(target=start_server)
    server_thread1.start()

def stop_x1(): # Stop Function
    global server_thread1
    asyncio.run(close_server())
    server_thread1.join()
    server_thread1 = None

async def get_key_and_iv(websocket,public_key):
    try:
        if not websocket.open:
            return False
        keyx = await websocket.recv()
        keyx = await decryptDataserver(keyx,private_key_pem,public_key.encode())
        if "#" in keyx:
            parts = keyx.split("#")
            if len(parts) == 2:
                keyx1 = test_decrypt_aes256_token(parts[0],parts[1])
                if keyx1:
                    key, iv = memory_key_generate(keyx1)
                    return key, iv
                else:
                    return None, None
            else:
                return None, None
        else:
            return None, None
    except Exception as e:
        logging.error(f"Error generating key and iv: {e}")
        return None, None


def colored_write(text):
    return '\033[31m' + text + '\033[0m'
    return colorama.Fore.RED + text + colorama.Style.RESET_ALL
def colored_write_ok(text):
    return '\033[32m' + text + '\033[0m'
    return colorama.Fore.GREEN + text + colorama.Style.RESET_ALL


global_list = {}

def init_global_list():
    global global_list
    with open('data.json', 'r') as file:
        global_list = json.load(file)
    if 'youtube-keywords' not in global_list:
        global_list['youtube-keywords'] = {}
        with open('data.json', 'w') as file:
            json.dump(global_list, file)

def get_title(url):
    r = requests.get(url) # sayfanın içeriğini alır
    soup = BeautifulSoup(r.text, features="html.parser")
    title = soup.title.get_text() # <title> etiketinin içindeki metni alır
    title = title[:-10] # başlığın son 10 harfini keser
    encoded = base64.b64encode(title.encode()) # başlığı base64 ile kodlar
    return encoded,title

def get_youtube_keyword(link):
    global global_list
    with open('data.json', 'r') as file:
        global_list = json.load(file)
    if 'youtube-keywords' not in global_list:
        global_list['youtube-keywords'] = {}
    keyword = link.split('watch?v=')[1].split('&')[0]
    if keyword in global_list['youtube-keywords']:
        return " >> Önceden Eklendi : " + base64.b64decode(global_list['youtube-keywords'][keyword]['n']).decode() + " k: " + keyword
    else:
        base_url = 'https://www.youtube.com/watch?v='
        search_string = keyword
        url = base_url + search_string
        encoded,title = get_title(url)
        # Default değerleri belirle
        data = {}
        data[keyword] = {}
        data[keyword]["n"] = encoded.decode()
        #data[keyword]["q"] = 0
        #data[keyword]["l"] = 0
        #data[keyword]["b"] = 0
        #data[keyword]["p"] = 0
        #data[keyword]["r"] = 0
        #data[keyword]["e"] = 0
        #data[keyword]["y"] = 0
        #data[keyword]["c"] = 0
        #data[keyword]["s"] = 0

        # Keyword'ü global_list["youtube-keywords"] sözlüğüne ekle
        global_list['youtube-keywords'][keyword] = data[keyword]

        # JSON dosyasını yazma modunda aç
        with open('data.json', 'w') as file:
            # Sözlük veri tipindeki JSON verisini dosyaya yaz
            json.dump(global_list, file)

        # İşlem başarılı mesajı ver
        return colored_write_ok(" >> Eklendi : " + title + " k: " + keyword)

def is_youtube_link(link):
    # Check if the link starts with "https://www.youtube.com/"
    if link.startswith("www.youtube.com/") or link.startswith("youtube.com/") or link.startswith("https://www.youtube.com/") or link.startswith("http://www.youtube.com/") or link.startswith("https://youtube.com/") or link.startswith("http://youtube.com/"):
        # Check if the link contains a video ID
        video_id = link.split("v=")[-1]
        if len(video_id) >= 11:
            return True
    return False


def change_youtube_keyword_link(link):
    global global_list
    if 'youtube-keywords' not in global_list:
        global_list['youtube-keywords'] = {}
    keyword = link.split('watch?v=')[1].split('&')[0]
    if keyword in global_list['youtube-keywords']:
        global_list["youtube-keywords"][keyword]["n"] = base64.b64encode(input("Video Adı: ").encode("utf-8")).decode("utf-8")
        #global_list["youtube-keywords"][keyword]["q"] = int(input("Kalite 0-10: "))
        #global_list["youtube-keywords"][keyword]["l"] = int(input("Dinlenilebilirlik 0-10: "))
        #global_list["youtube-keywords"][keyword]["b"] = int(input("Zaman Geçiricilik 0-10: "))
        #global_list["youtube-keywords"][keyword]["r"] = int(input("Hatıra 0-10: "))
        #global_list["youtube-keywords"][keyword]["e"] = int(input("Duygusal 0-10: "))
        #global_list["youtube-keywords"][keyword]["y"] = int(input("Enerjik 0-10: "))
        #global_list["youtube-keywords"][keyword]["c"] = int(input("Cringe 0-10: "))
        #global_list["youtube-keywords"][keyword]["s"] = int(input("Çekicilik 0-10: "))
        #global_list["youtube-keywords"][keyword]["p"] = int(input("Puan 0-10: "))
        with open("data.json", "w") as file:
            json.dump(global_list, file)
        print("İşlem başarılı")
    else:
        return colored_write(" >> Keyword Bulunamadı : " + keyword)

def check_port(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex((host, port)) != 0

def run_server(host, port):
    global httpd, namedecrypt_cache, namesubmit_cache, nametokenpost_cache
    a1, keyabc = generatekey_general_token("#decrypt")
    namedecrypt_cache = a1
    a2, keyabc = generatekey_general_token("#submit")
    namesubmit_cache = a2
    a3, keyabc = generatekey_general_token("#tokenpost")
    nametokenpost_cache = a3
    server_address = (host, port)
    httpd = HTTPServer(server_address, StaticServer)
    httpd.logRequests = False
    httpd.serve_forever()

async def stop_server():
    global httpd,tokens,invs, encrypted_messages, server_memory_encrypt_key_Hash, server_memory_encrypt_iv_Hash,PASSWORD,SALT,server_key,x1iv,__process_close__
    print(' >> Stopping server...')
    httpd.shutdown()
    #time.sleep(1)
    httpd.server_close()
    httpd.socket.close()
    del httpd
    asyncio.get_event_loop().stop()
    print(colored_write_ok(' >> Server stopped.'))
    encrypted_messages = []
    tokens = []
    invs = []
    server_memory_encrypt_key_Hash = None
    server_memory_encrypt_iv_Hash = None
    PASSWORD = generateToken_str()
    SALT = generateToken_str()
    server_key = None
    x1iv = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    __process_close__ = 0

start_keyword=['güzel','tatlı','yt','youtube','harika','bir','bana','play','playing','için','song']
music_keyword=['musık','musik','musıc','music','şarkı', 'sarkı','müzik', 'muzik','muzık', 'sarki','song','kpop','play']
ac_keyword=['play','ac','aç','söyle','soyle','link','lınk','ver','hemen','yonlendir','yönlendir','yonlendır','yolla','at','goster','göster','youtube','open','song','music']

def generate_net_rsa_4096():
    print(colored_write_ok("Generating RSA 4096 Bit Key..."))
    rsa_0_key = RSA.generate(4096)
    # private
    private_key_pem = rsa_0_key.export_key()
    # public
    public_key_pem = rsa_0_key.publickey().export_key()
    print(colored_write_ok("Private Key SHA512 : "+hashlib.sha512(private_key_pem).hexdigest()))
    print(colored_write_ok("Public Key SHA512 : "+hashlib.sha512(public_key_pem).hexdigest()))
    rsa_0_key = None
if __name__ == '__main__':
    banner()
    init_global_list()
    server_thread = None
    if len(sys.argv) > 1:
        if '-auto' in sys.argv:
            if not '-dev' in sys.argv:
                generate_net_rsa_4096()
            if check_port(host, port):
                server_thread = threading.Thread(target=run_server, args=(host, port))
                server_thread.start()
                nametoken_cache, keyabc = generatekey_general_token("#123")
                random_token = nametoken_cache
                print(colored_write_ok(f" >> Set Key: http://{host}:{port}/?token=" + random_token))
                webbrowser.open_new_tab(f"http://{host}:{port}/?token=" + random_token)
                print(colored_write_ok(f" >> Serving on http://{host}:{port} ..."))
                text1 = generate_inv()
                print(f"http://{host}:{port}/?inv="+ text1)
                start_x1()
                print(colored_write_ok(f" >> Websocket server started on ws://{host}:{WEBSOCKET_PORT}/"))
            else:
                print(colored_write(f" >> Port {port} is already in use."))
        else:
            if not '-dev' in sys.argv:
                generate_net_rsa_4096()
            iaxda = 0
            if '-s' in sys.argv:
                iaxda = 1
                host_index = sys.argv.index('-s') + 1
                host = sys.argv[host_index]
            if '-p' in sys.argv:
                iaxda = 1
                port_index = sys.argv.index('-p') + 1
                port = int(sys.argv[port_index])
            if '-wp' in sys.argv:
                iaxda = 1
                wpport_index = sys.argv.index('-wp') + 1
                WEBSOCKET_PORT = int(sys.argv[wpport_index])
            if iaxda == 1:
                if check_port(host, port):
                    server_thread = threading.Thread(target=run_server, args=(host, port))
                    server_thread.start()
                    nametoken_cache, keyabc = generatekey_general_token("#123")
                    random_token = nametoken_cache
                    print(colored_write_ok(f" >> Set Key: http://{host}:{port}/?token=" + random_token))
                    webbrowser.open_new_tab(f"http://{host}:{port}/?token=" + random_token)
                    print(colored_write_ok(f" >> Serving on http://{host}:{port} ..."))
                    text1 = generate_inv()
                    print(f"http://{host}:{port}/?inv="+ text1)
                    start_x1()
                    print(colored_write_ok(f" >> Websocket server started on ws://{host}:{WEBSOCKET_PORT}/"))
                else:
                    print(colored_write(f" >> Port {port} is already in use."))
    else:
        generate_net_rsa_4096()
    while True:
        user_input = input("EncryptedChat@Python > ")
        if not user_input.strip():
            continue
        args = user_input.split()
        if args[0].lower() == 'start':
            if server_thread is not None and server_thread.is_alive():
                print(' >> Server is already running. Please stop the server first to start a new instance.')
            else:
                if '-s' in args:
                    host_index = args.index('-s') + 1
                    host = args[host_index]
                if '-p' in args:
                    port_index = args.index('-p') + 1
                    port = int(args[port_index])
                if '-wp' in args:
                    wpport_index = args.index('-wp') + 1
                    WEBSOCKET_PORT = int(args[wpport_index])
                if check_port(host, port):
                    server_thread = threading.Thread(target=run_server, args=(host, port))
                    server_thread.start()
                    nametoken_cache, keyabc = generatekey_general_token("#123")
                    random_token = nametoken_cache
                    print(colored_write_ok(f" >> Set Key: http://{host}:{port}/?token=" + random_token))
                    webbrowser.open_new_tab(f"http://{host}:{port}/?token=" + random_token)
                    print(colored_write_ok(f" >> Serving on http://{host}:{port} ..."))
                    text1 = generate_inv()
                    print(f"http://{host}:{port}/?inv="+ text1)
                    text1 = generate_inv()
                    print(f"http://{host}:{port}/?inv="+ text1)
                    start_x1()
                    print(colored_write_ok(f" >> Websocket server started on ws://{host}:{WEBSOCKET_PORT}/"))
                else:
                    print(colored_write(f" >> Port {port} is already in use."))
        elif args[0].lower() == 'stop':
            if server_thread is not None:
                asyncio.run(stop_server())
                server_thread.join()
                server_thread = None
                stop_x1()
            else:
                print(colored_write(' >> Server is not running.'))
        elif args[0].lower() == 'token':
            list_tokens()
        elif args[0].lower() == 'inv':
            if server_thread is not None:
                if any(x in ('-new', '-create', '-add') for x in args):
                    text1 = generate_inv()
                    print(f"http://{host}:{port}/?inv="+ text1)
                else:
                    list_inv()
            else:
                print(colored_write(' >> Server is not running.'))
        elif args[0].lower() in ('backdoor','chatbot','magicword'):
            if '-c' in args:
                key_index = args.index('-c') + 1
                text = args[key_index]
                if text.lower() in ('kill','reset','change','delete','del'):
                    chatbotinvtext = ''.join(random.choices(string.ascii_letters + string.digits, k=512))
                    print(colored_write_ok(" >> Magic Word: Deleted"))
                else:
                    chatbotinvtext = text.strip()
                    print(colored_write_ok(" >> Magic Word: Changed"))
        elif args[0].lower() in ('rsa','rsareset','serverpublic','serverprivate'):
            if len(args) > 1:
                if args[1].lower() in ('-reset','-del','-delete','-change'):
                    if server_thread is not None:
                        asyncio.run(stop_server())
                        server_thread.join()
                        server_thread = None
                        stop_x1()
                        generate_net_rsa_4096()
                    else:
                        generate_net_rsa_4096()
                else:
                    print(colored_write_ok("Private Key SHA512 : "+hashlib.sha512(private_key_pem).hexdigest()))
                    print(colored_write_ok("Public Key SHA512 : "+hashlib.sha512(public_key_pem).hexdigest()))
            else:
                print(colored_write_ok("Private Key SHA512 : "+hashlib.sha512(private_key_pem).hexdigest()))
                print(colored_write_ok("Public Key SHA512 : "+hashlib.sha512(public_key_pem).hexdigest()))
        elif args[0].lower() in ('serverkey','key'):
            print_server_key()
        elif args[0].lower() in ('reskey', 'resserverkey','resetkey','keyres','keyreset','resetserverkey','resetpassword','resspassw','resspasw','respassw','resspass','respas','respass','resetpassw','respassword'):
            if server_thread is not None:
                nametoken_cache, keyabc = generatekey_general_token("#123")
                random_token = nametoken_cache
                print(colored_write_ok(f" >> Set Key: http://{host}:{port}/?token=" + random_token))
                webbrowser.open_new_tab(f"http://{host}:{port}/?token=" + random_token)
            else:
                print(colored_write(' >> Server is not running.'))
        elif args[0].lower() == 'data':
            if '-k' in args:
                key_index = args.index('-k') + 1
                text = args[key_index]
                if text == PASSWORD:
                    key, iv = memory_key_generate(server_key)
                    print_decrypted_messages(mesajlari_oku(key, iv,encrypted_messages))
                else:
                    print("Password Error")
            else:
                print_decrypted_messages("view")
        elif (((len(args) == 2) or (len(args) == 4 and '-s' in args)) and ((args[0].lower() in start_keyword and args[1].lower() in ac_keyword) or (args[0].lower() in music_keyword and args[1].lower() in ac_keyword))) or (((len(args) == 3) or (len(args) == 5 and '-s' in args)) and args[0].lower() in start_keyword and (((args[1].lower() in music_keyword) and args[2].lower() in ac_keyword) or ((args[1].lower() in start_keyword) and args[2].lower() in ac_keyword))):
            print(colored_write_ok(' >> Loading...'))
            all_music = 0
            if '-s' in args:
                sayi_index = args.index('-s') + 1
                if args[sayi_index].lower() in ('all','hepsi','herşey','tamamı','tümü','tüm','hepsini','toplam'):
                    sayi = len(list(global_list['youtube-keywords'].keys()))
                else:
                    sayi = int(args[sayi_index])
                if sayi > len(list(global_list['youtube-keywords'].keys())):
                    sayi = len(list(global_list['youtube-keywords'].keys()))
            else:
                sayi = 1
            played_videos = set()
            if all_music == 1:
                for video_id in global_list['youtube-keywords'].keys():
                    print(base64.b64decode(global_list['youtube-keywords'][video_id]['n']).decode())
                    url = f'https://www.youtube.com/watch?v={video_id}'
                    webbrowser.open_new_tab(url)
            else:
                for i in range(sayi):
                    while True:
                        random_video = random.choice(list(global_list['youtube-keywords'].keys()))
                        if random_video not in played_videos:
                            played_videos.add(random_video)
                            break
                    print(base64.b64decode(global_list['youtube-keywords'][random_video]['n']).decode())
                    url = f'https://www.youtube.com/watch?v={random_video}'
                    webbrowser.open_new_tab(url)
        elif args[0].lower() in ('youtube'):
            if '-c' in args:
                l_index = args.index('-c') + 1
                link = args[l_index]
                if is_youtube_link(link):
                    change_youtube_keyword_link(link)
            else:
                if '-s' in args:
                    default_link_count_index = args.index('-s') + 1
                    default_link_count = args[default_link_count_index]
                else:
                    default_link_count=20
                sayac = 0
                while True:
                    link = input("Youtube Link > ")
                    if link.strip():
                        sayac+=1
                        if is_youtube_link(link):
                            return_text = get_youtube_keyword(link)
                            print(return_text)
                        else:
                            args = link.split()
                            if args[0].lower() in('exit','çık','cık','kapat','cıkıs','çıkıs','cıkış','çıkış'):
                                break
                    if sayac == default_link_count:
                        break
        elif args[0].lower() in ('host','port','ip','test','check','checkup','link'):
            if server_thread is not None:
                print(colored_write_ok(f" >> Serving on http://{host}:{port} ..."))
            else:
                print(colored_write(' >> Server is not running.'))
        elif args[0].lower() in ('clear','cls'):
            if os.name == 'nt':
                os.system('cls')
            else:
                os.system('clear')
        elif args[0].lower() in ('exit','kill','die'):
            if server_thread is not None:
                asyncio.run(stop_server())
                server_thread.join()
                server_thread = None
                stop_x1()
                print(colored_write_ok(' >> Program terminated.'))
                os.kill(os.getpid(), 9)
            else:
                print(colored_write_ok(' >> Program terminated.'))
            break


    #parser = argparse.ArgumentParser()
    #parser.add_argument('--port', type=int, default=80, help='port to run the server on')
    #parser.add_argument('--start', action='store_true', help='start the server')
    #parser.add_argument('--stop', action='store_true', help='stop the server')
    #args = parser.parse_args()

    #if args.start:
    #    run_server(args.port)
    #elif args.stop:
    #    stop_server()
    #else:
    #    print('Please specify --start or --stop')
    #try:
    #    host = 'localhost'
    #    port = 80
    #    server_address = (host, port)
    #    httpd = HTTPServer(server_address, StaticServer)
    #    httpd.logRequests = False
    #    print(f"Serving on http://{host}:{port} ...")
    #    httpd.serve_forever()
    #except KeyboardInterrupt:
    #    print('Stopping server...')
    #    httpd.server_close()