# Happy2EncryptedChat Beta Release
We are a project that provides a secure and private messaging service that works on the tor network. The tor network is a decentralized network that protects your identity and location from prying eyes by routing your traffic through multiple servers around the world. Our app uses end-to-end encryption to ensure that no one can access your messages except you and your chat partner. Our app also deletes your messages from the server as soon as they are sent, so there is no trace of your communication. Our app works with websocket technology, which enables reliable data transfer. Our mission is to offer a simple and easy-to-use messaging app that respects your privacy and freedom of expression.

## Your site looks like this:
bwxxrajkvaykw2lsrovajjd54aam2cpw4ffdgxvtvb3cgncwkesstxyd.onion

The Tor network provides anonymity and privacy against government surveillance, but it does not guarantee immunity from criminal investigations. For instance, a computer expert may be able to detect that you are using this application, but they will never be able to decrypt your messages. However, the inability to decrypt the messages is not a valid defense in court, and the mere usage of this application may be considered as suspicious or incriminating. Therefore, you should use this application with caution and responsibility.
### But this solution might work, but still can't completely cover the blame :
This command is used to remove data from available unused disk space on a volume. If you don't know exactly what it does, don't use it.
[ https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/cipher](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/cipher)
```cmd
cipher /w:C:\
```

### It is very easy to open a site on the Tor network.
### Create this folder here
![alt text 1](https://raw.githubusercontent.com/h6465617468/Happy2EncryptedChat/main/images/123123.png?raw=true)
### Open this file and add the following to the last lines.
```
HiddenServiceDir C:\Users\(name)\Desktop\Tor Browser\hidden_service
HiddenServicePort 80 127.0.0.1:80
HiddenServicePort 5678 127.0.0.1:5678
UseBridges 1
```
![alt text 2](https://raw.githubusercontent.com/h6465617468/Happy2EncryptedChat/main/images/asd123123.png?raw=true)
### Open Tor Browser and go to any site. If something like this occurs in this folder, then the process is complete. Check inside the "hostname" file.
![alt text 3](https://raw.githubusercontent.com/h6465617468/Happy2EncryptedChat/main/images/asdsa123123.png?raw=true)

### [ Download For Windows](https://github.com/h6465617468/Happy2EncryptedChat/archive/refs/heads/windows.zip) - [ Download Tor Browser](https://www.torproject.org/download/)

# Features
- Secure communication system with end-to-end encryption: a technique that encrypts data and information as it passes from device to device, so that only the sender and the receiver can see the original contents1
- Cryptographic techniques: various mathematical algorithms that ensure the confidentiality, integrity and authenticity of the data, such as:
  - Elliptic curve SECP256k1 signature: a digital signature scheme based on an elliptic curve that provides high security and fast verification
  - RSA signature: a digital signature scheme based on the RSA algorithm that provides strong authentication and non-repudiation
  - RSA key exchange: a key exchange protocol based on the RSA algorithm that allows two parties to securely establish a shared secret key
  - RSA encryption: an encryption scheme based on the RSA algorithm that allows public-key encryption and decryption
  - AES 256 encryption: an encryption scheme based on the Advanced Encryption Standard (AES) algorithm that uses a 256-bit key to provide strong symmetric encryption
- Data storage: the process of storing data in memory and encrypting it multiple times before sending it to the server, which adds another layer of protection
- Network security: the process of securing the network traffic and preventing network surveillance, such as:
  - Tor network mirroring: a technique that uses the Tor network, a decentralized network of servers that route the data through multiple hops, making it difficult to trace the source or destination of the communication
  - HTTPS protocol optional: a technique that allows the system to operate even without HTTPS protocol, a secure version of HTTP protocol that encrypts the data in transit between the client and the server
- Communication protocol: the set of rules and standards that enable real-time and bidirectional communication between the client and the server, such as:
  - WebSocket protocol: a web technology that allows a persistent connection between the client and the server, enabling fast and efficient data transfer

This project shows the encrypted messages that come from the browser to the server side. The encrypted messages are created using end-to-end encryption technique to protect the data from unauthorized access. The encrypted messages are stored in memory and encrypted multiple times before being sent to the server.
![alt text](https://raw.githubusercontent.com/h6465617468/Happy2EncryptedChat/main/Screenshot_7.png?raw=true)

# Note
### I wrote these codes with the help of ChatGPT

# Setup
### 1- Install Python
### 2- Run cmd as Administrator
```cmd
pip install pycryptodome
pip install pycryptodomex
pip install websockets
pip install requests
pip install beautifulsoup4
pip install ecdsa
pip install elliptic
pip install colorama
```
### 3- Run cmd or Powershell
```cmd
py index.py
py index.py -auto
py index.py -dev
```

# Commands
```
Python To Exe
pyinstaller.exe --onefile index.py --uac-admin --add-data "www;www" --add-data "cb1.json;." --add-data "data.json;."

start
start -auto
start -s 127.0.0.1 -p 80 -wp 5678
stop
exit
inv -add
inv
reskey
rsa -reset
rsa
play music
play music -s 3
youtube
youtube -s 3
cls
data
data -k (decrypt key)
key
token
```
-auto Quick Start
```cmd
py index.py -auto
```
| Command | Description |
| --- | --- |
| `start` | Starts the server, -p ( server port ), -s ( host ), -wp ( Websocket Port ) |
| `stop` | Stops the server |
| `exit` | Force close |
| `inv` | Send a link to your friend and message 2 people. Don't forget to change the host part -add new invite link |
| `reskey` | Reset server AES-256 key |
| `play music` | Youtube video play -s ( count ) |
| `youtube` | Add Music -s ( count ) |
| `backdoor` | Backdoor -c ( Magic Word ) When entering the address 127.0.0.1, the magic word can be connected to the chat when entered. |
| `rsa` | Add Music -delete ( Reset RSA 4096 Bit Server Key ) |
| `cls` | Clear command prompt |
| `data` | Display Encrypted Messages ( It will return null because it is deleted instantly. ) -k ( decrypt key ) |
| `key` | View Server Key |
| `token` | Display Tokens ( It will return null because it is deleted instantly. ) |

# Example
### This link provides a direct link. It cannot be reused.
http://(host):(port)/?inv=Kr9CBrwYElMND8cEHdUL5r5OWY5coXNMQzto1O_EWlods51yTmN7gzhexG7fvU03

![alt text](https://raw.githubusercontent.com/h6465617468/Happy2EncryptedChat/main/test0x1cvx0.png?raw=true)

# Public/Private Keys
![alt text](https://raw.githubusercontent.com/h6465617468/Happy2EncryptedChat/main/testa0b5c3.png?raw=true)
