import sys
sys.dont_write_bytecode = True

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
from chatbot import cevapla

# pip install pycryptodome
# pip install pycryptodomex
# pip install websockets
# pip install requests
# pip install beautifulsoup4

# Disable bytecode writing for the Crypto module
sys.modules['Cryptodome'].__dict__['__file__'] = ''

host = '127.0.0.1'
port = 80

PASSWORD = "123"

chatbotinvtext = "serverkey"

httpd = None
server_thread = None

def banner():
    print('''

                   ...
                 ;::::;              E2EE Chat
               ;::::; :;             
             ;:::::'   :;            Usage : start -s 127.0.0.1 -p 80
            ;:::::;     ;.                   stop
           ,:::::'       ;           OOO\    exit
           ::::::;       ;          OOOOO\         data -k (key)
           ;:::::;       ;         OOOOOOOO        key
          ,;::::::;     ;'         / OOOOOOO       token
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
def encrypt(key, iv, plaintext):
    try:
        # Create AES-CBC cipher.
        cipher = AES.new(key, AES.MODE_CBC, iv)

        # Encrypt and return the IV and ciphertext.
        ciphertext = cipher.encrypt(pad(plaintext.encode(), AES.block_size))
        return ciphertext
    except Exception as e:
        #print("Encryption error:", e)
        return None

def decrypt(key, iv, ciphertext):
    try:
        # Create AES-CBC cipher.
        cipher = AES.new(key, AES.MODE_CBC, iv)

        # Decrypt and return the plaintext.
        plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
        return plaintext.decode()
    except Exception as e:
        #print("Decryption error:", e)
        return None

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

# Global file_token list
file_token = {generateToken_str():"crypto-js.min.js",generateToken_str():"jquery-3.6.4.min.js",generateToken_str():"jsencrypt.min.js",generateToken_str():"abc.css",generateToken_str():"a.css",generateToken_str():"a1b.css",generateToken_str():"functions.js"}
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
    print(" ⟫ Token list:")
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
    random_inv = base64.urlsafe_b64encode(os.urandom(48)).decode()
    random_inv = random_inv.replace('-', 'x')
    
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
    print(" ⟫ invs list:")
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

def print_server_key():
    if server_memory_encrypt_key_Hash and server_memory_encrypt_iv_Hash:
        print(f' ⟫ Server Key Hash: {server_memory_encrypt_key_Hash}{server_memory_encrypt_iv_Hash}')
    else:
        print(f' ⟫ Server Key Hash: None')

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

def mesajlari_oku(key,iv):
    global server_memory_encrypt_key_Hash, server_memory_encrypt_iv_Hash
    if hashlib.sha512(key).hexdigest() == server_memory_encrypt_key_Hash and hashlib.sha512(iv).hexdigest() == server_memory_encrypt_iv_Hash:
        if len(key) != 32:
            return "Key size not suitable, must be 32 bytes"
        if len(iv) != 16:
            return "IV size is not appropriate, must be 16 bytes"
        decrypted_messages = []
        for message in encrypted_messages:
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
        print(" ⟫ Encrypted Data List:")
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
        print(" ⟫ Message List:")
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
                        <form method="post">
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
            inv = self.path.split('=')[1]
            if inv_login(inv):
                token1, token2, token3, token4, token5, token6, token7 = get_token_variables(file_token)
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
    <script src="/{token1}"></script>
    <script src="/{token2}"></script>
    <script type="text/javascript" src="/{token3}"></script>
    <link rel="stylesheet" href="/{token4}">
    <link rel="stylesheet" href="/{token5}">
    <link rel="stylesheet" href="/{token6}">
    <script src="/{token7}"></script>
</head>
<body style="background-color:black!important;">
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
</div><br><loading-durum style='color:white;margin:0 auto;font-size:24px;'>Bağlantı Bekleniyor</loading-durum></div></div>
<script>
var server_key = "{server_key}";
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
<script>
</script>
<form id="message-form"><input type="text" id="message-input" placeholder="Send Message" style="padding:15px;margin:0;font-size:16px;font-weight:1000;width:80%;border:0;background-color:transparent;margin-right:0;max-width:600px;height:auto;border:0;margin-right:0;border-bottom:2.5px solid dimgrey;margin:0;padding:16px;color:white!important;" autocomplete="off" autofocus required><input type="submit" value="❱" style="padding:16px;margin:0;font-size:16px;font-weight:1000;width:%5;border:0;background-color:transparent;margin-left:0;border-bottom:2.5px solid dimgrey;padding:16px;margin:0;color:white!important;">
<input type="text" id="target-input" value="a" style="display:none" required></form>
<div id="messages" style="word-wrap: break-word;"></div>
<button onclick="keychange()">Public,Private key Change</Button>
<script>
$(document).ready(function() {{
openloading();
}});


function sendMessage(message1, target, keyx,gorunum=1,latest=false) {{
  var payload = `${{message1}}:${{target}}:${{keyx}}`;
  socket.send(payload);
  if (gorunum==1){{
  var messages = document.querySelector('#messages');
  var messagex = document.createElement('div');
  messagex.style.display = "block";
  //message1="(Encrypted)";
  //messagex.innerHTML = "Mesaj Gönderildi => <textarea style='color:grey;overflow: hidden;resize: vertical;'>"+message1+"</textarea> "+getCurrentTime()+" ID: "+target;
  if(latest!=false){{
  messagex.innerHTML = "<p class='a lf'><label id='f1'>"+"You : " + latest + "</label></p><p class='rg' style='color:grey;border:none!important;z-index:2;'>" + getCurrentTime()+" ID: "+target+"</p>";
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
    var keyx=server_key;
    console.log('WebSocket connection is open');
    promptUser('Enter Password:')
  .then(passx => {{
    if(passx != "" && passx != null && passx != undefined && passx != " "){{
        socket.send(`${{passx}}`);
        socket.send(`${{keyx}}`);
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
    setTimeout(resolve, 100);
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
    }}, 100);
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
    message.innerHTML = "<p class='a rg'><label id='f1'>"+messagecbbtbtnrte+"</label></p><p class='rg' style='color:grey;border:none!important;z-index:2;'>"+sonradata+"</p>";
    messages.insertBefore(message, messages.firstChild);    
  }}


  }}else{{
  message.textContent = event.data;
  messages.insertBefore(message, messages.firstChild);
  }}
}}
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
    <textarea name="myrsapublic" id="myrsapublic"></textarea>
    <br>
    <label for="myrsaprivate">My Private Key:</label><br>
    <textarea name="myrsaprivate" id="myrsaprivate"></textarea>
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
        if self.path == '/submit':
            #self.send_error(404)
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
        elif self.path == '/token':
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
        elif self.path == '/decrypt':
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length)
            post_data = json.loads(post_data)
            token = post_data.get('token', None)
            #print("Token2:"+token)
            if token_login(token):
                keyx = post_data.get('key', None)
                #print("Keyx:"+keyx)
                key,iv=memory_key_generate(keyx)
                dec_server_data=return_decrypted_messages(mesajlari_oku(key, iv))
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
                self.send_response(404)
                return

        elif self.path == '/speech':
            global host,port
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length)
            post_data = parse_qs(post_data.decode())
            inv = post_data.get('speech', [''])[0]
            if inv == chatbotinvtext:
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
        elif self.path.startswith('/?token='):
            global random_token
            token = self.path.split('=')[1]
            if token == random_token:
                content_length = int(self.headers['Content-Length'])
                post_data = self.rfile.read(content_length)
                post_data = parse_qs(post_data.decode())
                new_server_key = post_data.get('server_key', [''])[0]
                set_memory_hash(new_server_key)
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
            else:
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

async def authenticate(websocket):
    try:
        await websocket.send("Enter password:")
        user_password = await websocket.recv()
        if user_password != PASSWORD:
            return False
        return True
    except Exception as e:
        return False

async def handler(websocket, path):
    global connected_users
    authenticated = await authenticate(websocket)
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

    key, iv = await get_key_and_iv(websocket)
    if key is None or iv is None:
        async with websocket_lock:
            connected.remove(websocket)
            websocket_is_open.pop(websocket, None)
        await websocket.close(1000,"error_occurred")
        return
    try:
        async for message in websocket:
            islem=0
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
                await mesajat(message1, key, iv, target,0)
            else:
                await mesajat(message1, key, iv, target,1)
            await broadcast(message, websocket, key, iv)
    except websockets.exceptions.ConnectionClosed:
        async with websocket_lock:
            connected.remove(websocket)
            websocket_is_open.pop(websocket, None)
            connected_users -= 1
    except asyncio.TimeoutError:
        async with websocket_lock:
            connected.remove(websocket)
            websocket_is_open.pop(websocket, None)
            connected_users -= 1
    finally:
        async with websocket_lock:
            connected.remove(websocket)
            websocket_is_open.pop(websocket, None)
            connected_users -= 1
async def broadcast(message, sender, key, iv):
    global encrypted_messages
    messages = return_broadcast_messages(key, iv)
    tasks = []
    if connected.__len__() % 2 == 0:
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
                tasks = [websocket.close() for websocket in connected if not websocket.closed]
                await asyncio.gather(*tasks, return_exceptions=True)
                # Kapatılamayan soketler için bekleyin
                for websocket in connected:
                    if not websocket.closed:
                        try:
                            await asyncio.wait_for(websocket.wait_closed(), timeout=2)
                        except asyncio.TimeoutError:
                            await websocket.close()
                async with websocket_lock:
                    connected.clear()
                    websocket_is_open.clear()
                shutdown_event.clear()
                print(colored_write_ok(' ⟫ WebSocket Server stopped.'))
                break


async def close_websocket_server():
    global shutdown_event
    shutdown_event.set()
    print(' ⟫ Stopping WebSocket Server...')


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

async def get_key_and_iv(websocket):
    try:
        await websocket.send("Please provide keyx:")
        if not websocket.open:
            return False
        keyx = await websocket.recv()
        key, iv = memory_key_generate(keyx)
        return key, iv
    except Exception as e:
        logging.error(f"Error generating key and iv: {e}")
        return None, None


def colored_write(text):
    return '\033[31m' + text + '\033[0m'
def colored_write_ok(text):
    return '\033[32m' + text + '\033[0m'


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
        return " ⟫ Önceden Eklendi : " + base64.b64decode(global_list['youtube-keywords'][keyword]['n']).decode() + " k: " + keyword
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
        return colored_write_ok(" ⟫ Eklendi : " + title + " k: " + keyword)

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
        return colored_write(" ⟫ Keyword Bulunamadı : " + keyword)



def check_port(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex((host, port)) != 0

def run_server(host, port):
    global httpd
    server_address = (host, port)
    httpd = HTTPServer(server_address, StaticServer)
    httpd.logRequests = False
    httpd.serve_forever()

async def stop_server():
    global httpd,tokens,invs, encrypted_messages, server_memory_encrypt_key_Hash, server_memory_encrypt_iv_Hash
    print(' ⟫ Stopping server...')
    httpd.shutdown()
    #time.sleep(1)
    httpd.server_close()
    httpd.socket.close()
    del httpd
    asyncio.get_event_loop().stop()
    print(colored_write_ok(' ⟫ Server stopped.'))
    encrypted_messages = []
    tokens = []
    invs = []
    server_memory_encrypt_key_Hash = None
    server_memory_encrypt_iv_Hash = None

start_keyword=['güzel','tatlı','yt','youtube','harika','bir','bana','play','playing','için','song']
music_keyword=['musık','musik','musıc','music','şarkı', 'sarkı','müzik', 'muzik','muzık', 'sarki','song','kpop','play']
ac_keyword=['play','ac','aç','söyle','soyle','link','lınk','ver','hemen','yonlendir','yönlendir','yonlendır','yolla','at','goster','göster','youtube','open','song','music']

if __name__ == '__main__':
    banner()
    init_global_list()
    server_thread = None
    if len(sys.argv) > 1:
        if '-auto' in sys.argv:
            if check_port(host, port):
                server_thread = threading.Thread(target=run_server, args=(host, port))
                server_thread.start()
                random_token = base64.urlsafe_b64encode(os.urandom(48)).decode()
                print(colored_write_ok(f" ⟫ Set Key: http://{host}:{port}/?token=" + random_token))
                webbrowser.open_new_tab(f"http://{host}:{port}/?token=" + random_token)
                print(colored_write_ok(f" ⟫ Serving on http://{host}:{port} ..."))
                text1 = generate_inv()
                print(f"http://{host}:{port}/?inv="+ text1)
                start_x1()
                print(colored_write_ok(f" ⟫ Websocket server started on ws://{host}:{WEBSOCKET_PORT}/"))
            else:
                print(colored_write(f" ⟫ Port {port} is already in use."))
        else:
            if '-s' in sys.argv:
                host_index = sys.argv.index('-s') + 1
                host = sys.argv[host_index]
            if '-p' in sys.argv:
                port_index = sys.argv.index('-p') + 1
                port = int(sys.argv[port_index])
            if '-wp' in args:
                wpport_index = args.index('-wp') + 1
                WEBSOCKET_PORT = int(args[wpport_index])
            if check_port(host, port):
                server_thread = threading.Thread(target=run_server, args=(host, port))
                server_thread.start()
                random_token = base64.urlsafe_b64encode(os.urandom(48)).decode()
                print(colored_write_ok(f" ⟫ Set Key: http://{host}:{port}/?token=" + random_token))
                webbrowser.open_new_tab(f"http://{host}:{port}/?token=" + random_token)
                print(colored_write_ok(f" ⟫ Serving on http://{host}:{port} ..."))
                text1 = generate_inv()
                print(f"http://{host}:{port}/?inv="+ text1)
                start_x1()
                print(colored_write_ok(f" ⟫ Websocket server started on ws://{host}:{WEBSOCKET_PORT}/"))
            else:
                print(colored_write(f" ⟫ Port {port} is already in use."))
    while True:
        user_input = input("EncryptedChat@Python ❱ ")
        if not user_input.strip():
            continue
        args = user_input.split()
        if args[0].lower() == 'start':
            if server_thread is not None and server_thread.is_alive():
                print(' ⟫ Server is already running. Please stop the server first to start a new instance.')
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
                    random_token = base64.urlsafe_b64encode(os.urandom(48)).decode()
                    print(colored_write_ok(f" ⟫ Set Key: http://{host}:{port}/?token=" + random_token))
                    webbrowser.open_new_tab(f"http://{host}:{port}/?token=" + random_token)
                    print(colored_write_ok(f" ⟫ Serving on http://{host}:{port} ..."))
                    text1 = generate_inv()
                    print(f"http://{host}:{port}/?inv="+ text1)
                    text1 = generate_inv()
                    print(f"http://{host}:{port}/?inv="+ text1)
                    start_x1()
                    print(colored_write_ok(f" ⟫ Websocket server started on ws://{host}:{WEBSOCKET_PORT}/"))
                else:
                    print(colored_write(f" ⟫ Port {port} is already in use."))
        elif args[0].lower() == 'stop':
            if server_thread is not None:
                asyncio.run(stop_server())
                server_thread.join()
                server_thread = None
                stop_x1()
            else:
                print(colored_write(' ⟫ Server is not running.'))
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
                print(colored_write(' ⟫ Server is not running.'))
        elif args[0].lower() in ('serverkey','key'):
            print_server_key()
        elif args[0].lower() in ('reskey', 'resserverkey','resetkey','keyres','keyreset','resetserverkey','resetpassword','resspassw','resspasw','respassw','resspass','respas','respass','resetpassw','respassword'):
            if server_thread is not None:
                random_token = base64.urlsafe_b64encode(os.urandom(48)).decode()
                print(colored_write_ok(f" ⟫ Set Key: http://{host}:{port}/?token=" + random_token))
                webbrowser.open_new_tab(f"http://{host}:{port}/?token=" + random_token)
            else:
                print(colored_write(' ⟫ Server is not running.'))
        elif args[0].lower() == 'data':
            if '-k' in args:
                key_index = args.index('-k') + 1
                text = args[key_index]
                key, iv = memory_key_generate(text)
                print_decrypted_messages(mesajlari_oku(key, iv))
            else:
                print_decrypted_messages("view")
        elif (((len(args) == 2) or (len(args) == 4 and '-s' in args)) and ((args[0].lower() in start_keyword and args[1].lower() in ac_keyword) or (args[0].lower() in music_keyword and args[1].lower() in ac_keyword))) or (((len(args) == 3) or (len(args) == 5 and '-s' in args)) and args[0].lower() in start_keyword and (((args[1].lower() in music_keyword) and args[2].lower() in ac_keyword) or ((args[1].lower() in start_keyword) and args[2].lower() in ac_keyword))):
            print(colored_write_ok(' ⟫ Loading...'))
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
                    link = input("Youtube Link ❱ ")
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
                print(colored_write_ok(f" ⟫ Serving on http://{host}:{port} ..."))
            else:
                print(colored_write(' ⟫ Server is not running.'))
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
                print(colored_write_ok(' ⟫ Program terminated.'))
                os.kill(os.getpid(), 9)
            else:
                print(colored_write_ok(' ⟫ Program terminated.'))
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