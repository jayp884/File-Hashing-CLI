import hashlib
import argparse

def generate_hash(file_path, algorithm):
    # Read the file in binary mode
    with open(file_path, "rb") as file:
        data = file.read()
    # Generate the hash using the selected algorithm
    hash_value = hashlib.new(algorithm, data).hexdigest()
    # Return the hash value
    return hash_value

parser = argparse.ArgumentParser(description="File Hashing Tool")
parser.add_argument("file", help="Path to the input file")
parser.add_argument(
    # Short and long options
    "-a", "--algorithm",
    # Supported choices
    choices=["md5", "sha1", "sha256", "sha512"],
    # Default algorithm
    default="sha256",
    # Help description
    help="Select hashing algorithm"
)
args = parser.parse_args()
print(generate_hash(args.file, args.algorithm))