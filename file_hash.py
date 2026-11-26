import hashlib
import argparse

def generate_hash(file_path):
    # Read the file in binary mode
    with open(file_path, "rb") as file:
        data = file.read()
    # Generate the SHA-256 hash
    hash_value=hashlib.sha256(data).hexdigest()
    # Return the hash value
    return hash_value

parser = argparse.ArgumentParser(description="File Hashing Tool")
parser.add_argument("file", help="Path to the input file")
args = parser.parse_args()
print(generate_hash(args.file))