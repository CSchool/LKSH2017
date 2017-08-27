from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from os import urandom
import codecs

BS = 16
enc_key = "62563423552c7e6f47502e3a6450797e"
pad = lambda s: s + (BS - len(s) % BS) * bytes(bytearray((BS - len(s) % BS,)))
unpad = lambda s : s[0:-s[-1]]

class AESCipher:
    def __init__( self, key ):
        """
        Requires hex encoded param as a key
        """
        self.key = codecs.decode(key, "hex")

    def encrypt( self, raw ):
        raw = pad(raw)
        iv = urandom(AES.block_size);
        cipher = AES.new( self.key, AES.MODE_CBC, iv )
        encrypted = ( iv + cipher.encrypt( raw ) ).hex()
        h = SHA256.new()
        h.update(self.key)
        h.update(encrypted.encode('ascii'))
        sig = h.hexdigest()
        return encrypted + "-" + sig

    def decrypt( self, data ):
        try:
            enc, sig = data.split('-')
            h = SHA256.new()
            h.update(self.key)
            h.update(enc.encode('ascii'))
            if h.hexdigest() != sig:
                return None
            enc = codecs.decode(enc, "hex")
            iv = enc[:16]
            enc= enc[16:]
            cipher = AES.new(self.key, AES.MODE_CBC, iv )
            return unpad(cipher.decrypt( enc))
        except:
            return None