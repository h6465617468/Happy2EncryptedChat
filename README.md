# Happy2EncryptedChat Beta Release
![SM](https://raw.githubusercontent.com/h6465617468/Happy2EncryptedChat/main/Screenshot_8.gif)
#### This is a secure messaging app that uses end-to-end encryption. Your messages are deleted from the server as soon as they are sent. You can also chat with a Chatbot if you want. This app allows only 2 people to chat at a time. The app works with websocket technology.

# Features
- End-To-End Encryption
- RSA Key Exchange, RSA Signature, RSA Encryption, AES 256 Encryption
- Data is kept in memory
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


| Name | End-To-End Encryption | Encryption Algorithms | Storage | Security
| :---: | :---: | :---: | :---: | :---: |
| Happy2EncryptedChat | Yes | RSA,AES-256 | Memory | I recommend the Tor browser.

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
```
### 3- Run cmd or Powershell
```cmd
py index.py
py index.py -auto
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
| `reskey` | Reset server key |
| `play music` | Youtube video play -s ( count ) |
| `youtube` | Add Music -s ( count ) |
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

# Usage
### This link provides a direct link. It cannot be reused.
http://(host):(port)/?inv=Kr9CBrwYElMND8cEHdUL5r5OWY5coXNMQzto1O_EWlods51yTmN7gzhexG7fvU03

![alt text](https://raw.githubusercontent.com/h6465617468/Happy2EncryptedChat/main/1.png?raw=true)
![alt text](https://raw.githubusercontent.com/h6465617468/Happy2EncryptedChat/main/2.png?raw=true)

# Browser To Server
![alt text](https://raw.githubusercontent.com/h6465617468/Happy2EncryptedChat/main/Screenshot_7.png?raw=true)
