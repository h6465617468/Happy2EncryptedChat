# Happy2EncryptedChat Beta Release
This is a secure messaging app that uses end-to-end encryption. Your messages are deleted from the server as soon as they are sent. You can also chat with a Chatbot if you want. This app allows only 2 people to chat at a time. The app works with websocket technology.

# Download For Windows
[ https://github.com/h6465617468/Happy2EncryptedChat/tree/windows](https://github.com/h6465617468/Happy2EncryptedChat/tree/windows)

# Features
- End-To-End Encryption
- Elliptic Curve SECP256k1 Signature, RSA Signature, RSA Key Exchange, RSA Encryption, AES 256 Encryption
- Data is kept in memory
- Data is encrypted multiple times before being sent to the server.
- Provides high security if used mirrored on the Tor network
```
# C:\Users\(name)\Desktop\Tor Browser\Browser\TorBrowser\Data\Tor\torrc
HiddenServiceDir C:\Users\(name)\Desktop\Tor Browser\hidden_service
HiddenServicePort 80 127.0.0.1:80
HiddenServicePort 5678 127.0.0.1:5678
UseBridges 1
```
- No logs
- Provides security even without https://
- Chatbot can be integrated into the project
- Uses Websocket

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
