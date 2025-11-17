import hashlib
import base64

def generate_short_url(long_url: str) -> str:
    long_url = str(long_url) 
    hash_val = hashlib.sha256(long_url.encode()).digest()
    encoded = base64.urlsafe_b64encode(hash_val).decode()[:7]
    return encoded

