import base64
import hashlib
import random
import secrets
import string


class Generator:
    def __init__(self, initial_id=0, key_length=32):
        self.url_to_code = {}
        self.code_to_url = {}
        self.current_id = initial_id
        self.key_length = key_length
        self.characters_cript = string.ascii_letters + string.digits

    def generate_short_url(self, long_url):
        if long_url in self.url_to_code:
            return self.url_to_code[long_url]

        hash_md5 = hashlib.md5(long_url.encode())
        short_code = base64.urlsafe_b64encode(hash_md5.digest()[:6]).decode()

        while short_code in self.code_to_url:
            hash_md5.update(b'x')
            short_code = base64.urlsafe_b64encode(hash_md5.digest()[:6])\
                .decode()

        self.url_to_code[long_url] = short_code
        self.code_to_url[short_code] = long_url

        return f'www.bitshn.com/{short_code}'
    
    def generate_password(self, length=12, include_uppercase=True,
                          include_numbers=True, include_symbols=True):
        character_groups = {
            string.ascii_letters: include_uppercase,
            string.digits: include_numbers,
            string.punctuation: include_symbols,
        }

        characters = ''.join(characters for characters, value in
                             character_groups.items() if value)

        if not characters:
            raise ValueError("At least one character group must be included")

        password = ''.join(random.choice(characters) for _ in range(length))
        return password
    
    def generate_unique_id(self):
        unique_id = self.current_id
        self.current_id += 1
        return unique_id
    
    def generate_key(self):
        key = ''.join(secrets.choice(self.characters_cript) for _ in
                      range(self.key_length))
        return key
    

if __name__ == "__main__":
    gerador = Generator()

    url_longa_1 = "https://www.example.com/pagina1"
    url_longa_2 = "https://www.example.com/pagina2"
    url_longa_3 = "https://www.example.com/pagina3"

    codigo_curto_1 = gerador.generate_short_url(url_longa_1)
    codigo_curto_2 = gerador.generate_short_url(url_longa_2)
    codigo_curto_3 = gerador.generate_short_url(url_longa_3)

    print(codigo_curto_1)
    print(codigo_curto_2)
    print(codigo_curto_3)

    for _ in range(5):
        new_id = gerador.generate_unique_id()
        print(f"Novo ID exclusivo gerado: {new_id}")

    for _ in range(5):
        new_key = gerador.generate_key()
        print(f"New unique cryptographic key: {new_key}")