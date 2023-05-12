# Happy2EncryptedChat Beta Release
We are a project that provides a secure and private messaging service that works on the tor network. The tor network is a decentralized network that protects your identity and location from prying eyes by routing your traffic through multiple servers around the world. Our app uses end-to-end encryption to ensure that no one can access your messages except you and your chat partner. Our app also deletes your messages from the server as soon as they are sent, so there is no trace of your communication. Our app works with websocket technology, which enables reliable data transfer. Our mission is to offer a simple and easy-to-use messaging app that respects your privacy and freedom of expression.

# Download For Windows
[ https://github.com/h6465617468/Happy2EncryptedChat/tree/windows](https://github.com/h6465617468/Happy2EncryptedChat/tree/windows)

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
- Chatbot integration: the process of integrating a chatbot, a software program that simulates human conversation using natural language processing and artificial intelligence, which can provide automated responses and assistance to the users
- Communication protocol: the set of rules and standards that enable real-time and bidirectional communication between the client and the server, such as:
  - WebSocket protocol: a web technology that allows a persistent connection between the client and the server, enabling fast and efficient data transfer

```
# C:\Users\(name)\Desktop\Tor Browser\Browser\TorBrowser\Data\Tor\torrc
HiddenServiceDir C:\Users\(name)\Desktop\Tor Browser\hidden_service
HiddenServicePort 80 127.0.0.1:80
HiddenServicePort 5678 127.0.0.1:5678
UseBridges 1
```

This project is a secure communication system that uses end-to-end encryption to protect the data from unauthorized access. The system employs various cryptographic techniques, such as elliptic curve SECP256k1 signature, RSA signature, RSA key exchange, RSA encryption and AES 256 encryption, to ensure the confidentiality, integrity and authenticity of the data. The data is stored in memory and encrypted multiple times before being sent to the server. The system also provides high security if used mirrored on the Tor network, which anonymizes the traffic and prevents network surveillance. The system does not keep any logs of the communication, which enhances the privacy of the users. The system can operate even without HTTPS protocol, which adds another layer of security. The system also allows the integration of a chatbot, which can provide automated responses and assistance to the users. The system uses WebSocket protocol, which enables real-time and bidirectional communication between the client and the server.

# Public/Private Keys
![alt text](https://raw.githubusercontent.com/h6465617468/Happy2EncryptedChat/main/testa0b5c3.png?raw=true)

# Note
### I wrote these codes with the help of ChatGPT

# Setup
No need to mess with the database, it's very easy to set up as the data is in the computer memory. The estimated memory processing time of the encrypted message is 0.1 seconds, and it is deleted immediately after processing.
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
```
### 3- Run cmd or Powershell
```cmd
py index.py
py index.py -auto
py index.py -dev
```

# Commands
```
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

### When you're done, you can run the command that shreds the free space on this disk
If you don't know exactly what it does, don't use it.
[ https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/cipher](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/cipher)
```cmd
cipher /w:C:\
```

# Example
### This link provides a direct link. It cannot be reused.
http://(host):(port)/?inv=Kr9CBrwYElMND8cEHdUL5r5OWY5coXNMQzto1O_EWlods51yTmN7gzhexG7fvU03

![alt text](https://raw.githubusercontent.com/h6465617468/Happy2EncryptedChat/main/test0x1cvx0.png?raw=true)

# Browser To Server
![alt text](https://raw.githubusercontent.com/h6465617468/Happy2EncryptedChat/main/Screenshot_7.png?raw=true)
