function base64_encode(array) {
    var base64 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=';
    var result = '';
    var i, j, triplet;
  
    for (i = 0; i < array.length; i += 3) {
      triplet = (array[i] << 16) | (array[i + 1] << 8) | array[i + 2];
      for (j = 0; j < 4; j += 1) {
        if (i * 8 + j * 6 <= array.length * 8) {
          result += base64.charAt((triplet >> 18 - j * 6) & 0x3F);
        } else {
          result += '==';
        }
      }
    }
    return result.replace(/=*$/, '');
  }
function base64_decode(str) {
    const lookup = { '+': 62, '/': 63 };
    let buffer = [];
    let bits = 0;
    let value = 0;
    let index = 0;
    for (let i = 0; i < str.length; i++) {
      const charCode = str.charCodeAt(i);
      let digit = charCode > 64 && charCode < 91 ? charCode - 65
        : charCode > 96 && charCode < 123 ? charCode - 71
        : charCode > 47 && charCode < 58 ? charCode + 4
        : charCode === 43 ? 62
        : charCode === 47 ? 63
        : -1;
      if (digit !== -1) {
        value = (value << 6) | digit;
        bits += 6;
        if (bits >= 8) {
          buffer[index++] = (value >> (bits - 8)) & 255;
          bits -= 8;
        }
      }
    }
    return new Uint8Array(buffer);
  }



  function promptUser(message) {
    return new Promise((resolve, reject) => {
      function prompt() {
        const input = window.prompt(message);
        if (input === null) {
          killpage();
          reject('User cancelled prompt');
        } else {
          resolve(input);
        }
      }
  
      prompt();
    });
  }
  
  



  function getCurrentTime() {
    var date = new Date();
    var timeString = date.toLocaleTimeString();
    var dateString = date.toLocaleDateString();
    return `${timeString} ${dateString}`;
  }
  

  function generateToken() {
    var now = new Date();
    var year = now.getFullYear().toString();
    var month = (now.getMonth() + 1).toString().padStart(2, '0');
    var day = now.getDate().toString().padStart(2, '0');
    var hour = now.getHours().toString().padStart(2, '0');
    var minute = now.getMinutes().toString().padStart(2, '0');
    var second = now.getSeconds().toString().padStart(2, '0');
    var randomPassword = '';
    var possibleChars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    for (var i = 0; i < 64; i++) {
      randomPassword += possibleChars.charAt(Math.floor(Math.random() * possibleChars.length));
    }
    var token = year + month + day + hour + minute + second + randomPassword + "x";
    return token;
  }
  
  // SCRIPT 1 START
  var token1 = generateToken();
  (()=>{
    var dataasdasdas="";
  // Gönderilecek veri
  let data = {
      token: token1
    };
    
    // Fetch ile post işlemi
    fetch("/token", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(data)
    })
      .then((response) => {
        // Sunucudan gelen yanıtın durumuna göre işlem yap
        if (response.ok) {
          // Yanıtı metin olarak oku
          return dataasdasdas;
        } else {
          // Hata mesajı fırlat
          throw new Error("Sunucu hatası: " + response.status);
        }
      })
      .then((tokentext) => {
  // Gönderilecek veri
  let data1 = {
      token: token1,
      key: decrypt_server_key_x
    };
    
    // Fetch ile post işlemi
    fetch("/decrypt", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(data1)
    })
      .then(async (response) => {
  // Sunucudan gelen yanıtın durumuna göre işlem yap
  
  if (response.ok) {
    dataasdasdas = await response.text();
      // Verinin gelip gelmediğini kontrol etmek için bir değişken tanımla
      var veriGeldi = false;
      // Her saniye verinin gelip gelmediğini kontrol et
      var interval = setInterval(() => {
        // Eğer dataasdasdas içinde veri varsa
        if (dataasdasdas.length > 4) {
          // Ekrana merhaba yazdır
          console.log("Bağlandı");
          // Verinin geldiğini belirt
          veriGeldi = true;
        }
        if (veriGeldi) {
          clearInterval(interval);
          var message = document.createElement('div');
          
          if (dataasdasdas.includes("___PUBLICKEY___") && dataasdasdas.includes("___END_PUBLICKEY___")) {
            closeloading();
            var startIndex = dataasdasdas.indexOf("___PUBLICKEY___") + "___PUBLICKEY___".length;
            var endIndex = dataasdasdas.indexOf("___END_PUBLICKEY___");
            var messagexx = dataasdasdas.slice(startIndex, endIndex);
          
            // En üstteki anahtarı almak için:
            var firstKeyIndex = dataasdasdas.indexOf("___PUBLICKEY___");
            var firstKeyEndIndex = dataasdasdas.indexOf("___END_PUBLICKEY___", firstKeyIndex);
            var firstKey = dataasdasdas.slice(firstKeyIndex + "___PUBLICKEY___".length, firstKeyEndIndex);
          
            var div = document.getElementById("targetpublic");
            if(safe_retry_rsa==true){
              safe_retry_rsa=false;
              div.innerHTML = firstKey;
              var encryptedMsg = dataasdasdas.slice(0, startIndex).replaceAll("___text___", "<textarea style='color:grey;overflow: hidden;resize: vertical;'>").replaceAll("___end_text___", "</textarea>").replaceAll("___PUBLICKEY___", "") + "Public Key Successful" + dataasdasdas.slice(endIndex).replaceAll("___text___", "<textarea style='color:grey;overflow: hidden;resize: vertical;'>").replaceAll("___end_text___", "</textarea>").replaceAll("___END_PUBLICKEY___", "");
              var messages = document.querySelector('#messages');
              message.innerHTML = encryptedMsg;
              messages.insertBefore(message, messages.firstChild);
            }
            dataasdasdas="";
          } else {
            console.log("TARGET PUBLIC KEY ERROR:")
            console.log(dataasdasdas)
            var messages = document.querySelector('#messages');
            message.innerHTML = dataasdasdas;
            messages.insertBefore(message, messages.firstChild);
            dataasdasdas="";
          }
        }
      }, 100);



      

  } else {
    // Hata mesajı fırlat
    throw new Error("Sunucu hatası: " + response.status);
  }
})

      .catch((error) => {
        // Oluşan hatayı ekrana yazdır
        console.error(error);
      });
      })
      .catch((error) => {
        // Oluşan hatayı ekrana yazdır
        console.error(error);
      });
  })()
  
  // SCRIPT 1 END
  
    function sendToken() {
      var token = generateToken();
      fetch('/token', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({token: token})
      })
      .then(result => {
        document.getElementById('resulttoken').innerHTML = result;
      })
      .catch(error => {
        console.error('Error:', error);
      });
      return false;
    }
    function sendForm() {
  var message = document.getElementById('message').value;
  var serverkey = document.getElementById('key').value;
  var target = document.getElementById('target').value;
  var token = generateToken();

  fetch('/token', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({token: token})
  })
  .then(result => {
  //token = result;

  fetch('/submit', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: 'message=' + encodeURI(message) + '&key=' + encodeURI(serverkey) + '&target=' + encodeURI(target) + '&token=' + encodeURI(token)
    })
    .then(result => {
    document.getElementById('result').innerHTML = result;
    })
    .catch(error => {
    console.error('Error:', error);
    });


  })
  .catch(error => {
  console.error('Error:', error);
  });

  return false;
  }
  function decrypt() {
  var serverkey = document.getElementById('serverkey').value;
  var token = generateToken();
  fetch('/token', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({token: token})
  })
  .then(result => {
  //token = result;
  })
  .catch(error => {
  //console.error('Error:', error);
  });
  fetch('/decrypt', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    key: serverkey,
    target: target,
    token: token // Add the token to the form data
  })
  
  })
  .then(result => {
  document.getElementById('resultmessage').innerHTML = result.text();
  })
  .catch(error => {
  //console.error('Error:', error);
  });
  return false;
  }


  var Base64={_keyStr:"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=",encode:function(e){var t="";var n,r,i,s,o,u,a;var f=0;e=Base64._utf8_encode(e);while(f<e.length){n=e.charCodeAt(f++);r=e.charCodeAt(f++);i=e.charCodeAt(f++);s=n>>2;o=(n&3)<<4|r>>4;u=(r&15)<<2|i>>6;a=i&63;if(isNaN(r)){u=a=64}else if(isNaN(i)){a=64}t=t+this._keyStr.charAt(s)+this._keyStr.charAt(o)+this._keyStr.charAt(u)+this._keyStr.charAt(a)}return t},decode:function(e){var t="";var n,r,i;var s,o,u,a;var f=0;e=e.replace(/[^A-Za-z0-9\+\/\=]/g,"");while(f<e.length){s=this._keyStr.indexOf(e.charAt(f++));o=this._keyStr.indexOf(e.charAt(f++));u=this._keyStr.indexOf(e.charAt(f++));a=this._keyStr.indexOf(e.charAt(f++));n=s<<2|o>>4;r=(o&15)<<4|u>>2;i=(u&3)<<6|a;t=t+String.fromCharCode(n);if(u!=64){t=t+String.fromCharCode(r)}if(a!=64){t=t+String.fromCharCode(i)}}t=Base64._utf8_decode(t);return t},_utf8_encode:function(e){e=e.replace(/\r\n/g,"\n");var t="";for(var n=0;n<e.length;n++){var r=e.charCodeAt(n);if(r<128){t+=String.fromCharCode(r)}else if(r>127&&r<2048){t+=String.fromCharCode(r>>6|192);t+=String.fromCharCode(r&63|128)}else{t+=String.fromCharCode(r>>12|224);t+=String.fromCharCode(r>>6&63|128);t+=String.fromCharCode(r&63|128)}}return t},_utf8_decode:function(e){var t="";var n=0;var r=c1=c2=0;while(n<e.length){r=e.charCodeAt(n);if(r<128){t+=String.fromCharCode(r);n++}else if(r>191&&r<224){c2=e.charCodeAt(n+1);t+=String.fromCharCode((r&31)<<6|c2&63);n+=2}else{c2=e.charCodeAt(n+1);c3=e.charCodeAt(n+2);t+=String.fromCharCode((r&15)<<12|(c2&63)<<6|c3&63);n+=3}}return t}}

function UpperKelime(string) {
  return string.charAt(0).toUpperCase() + string.slice(1).toLowerCase();
}
function escapeHtml(text) {
var map = {
  '&': '&amp;',
  '<': '&lt;',
  '>': '&gt;',
  '"': '&quot;',
  "'": '&#039;'
};
return text.replace(/[&<>"']/g, function(m) { return map[m]; });
}
function str_splitx (string, splitLength) {
  if (splitLength === null) {
    splitLength = 1
  }
  if (string === null || splitLength < 1) {
    return false
  }
  string += ''
  const chunks = []
  let pos = 0
  const len = string.length
  while (pos < len) {
    chunks.push(string.slice(pos, pos += splitLength))
  }
  return chunks
}

  function encryptData(cache_x_RSA,key,myprivate){
    var cache_signp="";
      var cache_109=str_splitx(cache_x_RSA,128);
      var crypted0193=[];
      var asjdasjdajs=[];
      cache_109.forEach(function(data5) {
    var crypt123123123 = new JSEncrypt();
    crypt123123123.setPrivateKey(myprivate);
    var fsdkjf34o2it2=Base64.encode(data5);
    cache_signp=crypt123123123.sign(fsdkjf34o2it2, CryptoJS.SHA256, "sha256");
    asjdasjdajs.push({"text":fsdkjf34o2it2,"sign":cache_signp});
    delete fsdkjf34o2it2;
        });
            var cache_123123=JSON.stringify(asjdasjdajs);
                var cryptedasdasdas1111=[];
                cache_12312asdasdas3=str_splitx(cache_123123,128);
                cache_12312asdasdas3.forEach(function(data10, index1) {
                  var crypt = new JSEncrypt();
                  crypt.setPublicKey(key);
                  cryptedasdasdas1111.push(Base64.encode(crypt.encrypt(data10)));
                });
                crypted0193.push(Base64.encode(JSON.stringify(cryptedasdasdas1111)));
      delete cache_109;
           return Base64.encode(JSON.stringify(crypted0193));
          }
          function decryptData(encryptedData, key, myprivate) {
            var decryptedData = "";
            try {
            var crypted0193 = JSON.parse(Base64.decode(encryptedData));
            var cryptedasdasdas1111 = JSON.parse(Base64.decode(crypted0193[0]));
            var asjdasjdajs = [];
            var asdasdasd="";
            cryptedasdasdas1111.forEach(function(data10, index1) {
            var crypt = new JSEncrypt();
            crypt.setPrivateKey(myprivate);
            var decryptedData1 = crypt.decrypt(Base64.decode(data10));
            asdasdasd=asdasdasd+decryptedData1;
            delete decryptedData1;
            });
            asjdasjdajs = asjdasjdajs.concat(JSON.parse(asdasdasd));
            asjdasjdajs.forEach(function(data5) {
            var crypt123123123 = new JSEncrypt();
            crypt123123123.setPublicKey(key);
            var signature = data5.sign;
            var plaintext = data5.text;
            var isSignatureValid = crypt123123123.verify(plaintext, signature, CryptoJS.SHA256);
            if (isSignatureValid) {
            decryptedData += Base64.decode(plaintext);
            } else {
            throw new Error("Invalid signature!");
            }
            delete signature, plaintext;
            });
            } catch (e) {
            //throw new Error("Decryption failed! " + e.message);
            }
            return decryptedData;
            }




function key_gen_main(mode=false){
    var crypt9 = new JSEncrypt({default_key_size: 2048});
    new Promise((resolve)=>{
    setTimeout(resolve, 100);
    }).then( ()=>{
        crypt9.getKey();
    }).finally(() => {
      var publicasdasdas=crypt9.getPublicKey();
        $('myprivate').html(crypt9.getPrivateKey());
        $('mypublic').html(publicasdasdas);
        if(mode==false){
        sendMessage("___PUBLICKEY___"+publicasdasdas, "a", server_key,0);
        return true;          
        }
    });
}

function encrypt_1(key, iv, plaintext) {
  try {
    const keyHex = CryptoJS.enc.Hex.parse(key);
    const ivHex = CryptoJS.enc.Hex.parse(iv);
    const encrypted = CryptoJS.AES.encrypt(plaintext, keyHex, {
      iv: ivHex,
      mode: CryptoJS.mode.CBC,
      padding: CryptoJS.pad.Pkcs7,
    });
    return encrypted.ciphertext.toString(CryptoJS.enc.Base64);
  } catch (e) {
    console.error("Encryption error:", e);
    return null;
  }
}

function decrypt_1(key, iv, ciphertext) {
  try {
    const keyHex = CryptoJS.enc.Hex.parse(key);
    const ivHex = CryptoJS.enc.Hex.parse(iv);
    const decrypted = CryptoJS.AES.decrypt({
      ciphertext: CryptoJS.enc.Base64.parse(ciphertext),
    }, keyHex, {
      iv: ivHex,
      mode: CryptoJS.mode.CBC,
      padding: CryptoJS.pad.Pkcs7,
    });
    return decrypted.toString(CryptoJS.enc.Utf8);
  } catch (e) {
    console.error("Decryption error:", e);
    return null;
  }
}