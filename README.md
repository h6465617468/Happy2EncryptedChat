# Happy 2 Encrypted Chat
It has end-to-end encryption. It doesn't save the incoming message anywhere, it just memorizes it, encrypts it, sends it and deletes it back. Not suitable for illegal or personal use.

# Setup
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
cd Desktop
cd Server
py index.py
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
```cmd
py index.py -auto
```
| Command | Description |
| --- | --- |
| start | Starts the server, -p ( server port ), -s ( host ), -wp ( Websocket Port ) -auto Quick Start |
| stop | Stops the server |
| exit | Force close |
| inv | Send a link to your friend and message 2 people. Don't forget to change the host part -add new invite link |
| reskey | Reset server key |
| play music | Youtube video play -s ( count ) |
| youtube | Add Music -s ( count ) |
| cls | Clear command prompt |
| data | Display Encrypted Messages ( It will return null because it is deleted instantly. ) -k ( decrypt key ) |
| key | View Server Key |
| token | ( It will return null because it is deleted instantly. ) |

# Usage
### This link provides a direct link. It cannot be reused.
http://(host):(port)/?inv=Kr9CBrwYElMND8cEHdUL5r5OWY5coXNMQzto1O_EWlods51yTmN7gzhexG7fvU03

![alt text](https://raw.githubusercontent.com/h6465617468/Happy2EncryptedChat/main/1.png?raw=true)
![alt text](https://raw.githubusercontent.com/h6465617468/Happy2EncryptedChat/main/2.png?raw=true)
