import hashlib

def calculate_hash(text):
    print("Calculating Hash...")
    m = hashlib.sha256()
    text = text.encode('utf-8')
    m.update(text)
    return m.hexdigest()