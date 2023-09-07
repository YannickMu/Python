import secrets
import string

#print(secrets.token_bytes())
#print(secrets.token_hex())
#print(secrets.token_urlsafe())
chars = string.digits + string.ascii_letters + string.punctuation
print(''.join(secrets.choice(chars) for _ in range(40)))
