import hashlib


class Hash_Function:
    def hash_password(self, nickname, password):
        hash_body = hashlib.sha512()
        full_string = (password + nickname)
        hash_body.update(full_string.encode())
        result = hash_body.hexdigest()
        return result
