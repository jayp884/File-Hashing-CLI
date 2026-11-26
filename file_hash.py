import hashlib

def generate_hash(file_path):
    # Read the file in binary mode
    with open(file_path, "rb") as file:
        data = file.read()
    # Generate the SHA-256 hash
    hash_value=hashlib.sha256(data).hexdigest()
    # Return the hash value
    return hash_value

print(generate_hash("sample.txt"))