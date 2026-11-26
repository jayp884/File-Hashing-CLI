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

def save_hash(hash_value, output_file):
    # Open the output file in write mode
    with open(output_file, "w") as file:
        # Write the generated hash to the file
        file.write(hash_value)

    # Display a confirmation message
    print("Hash saved to:", output_file)

def compare_hash(hash_value, saved_file):
    # Read the previously saved hash
    with open(saved_file, "r") as file:
        saved_hash = file.read().strip()

    # Compare both hash values
    if hash_value == saved_hash:
        print("Hash Match: File integrity verified.")
    else:
        print("Hash Mismatch: File contents or hashing algorithm may differ.")

parser = argparse.ArgumentParser(description="File Hashing Tool")


parser.add_argument("file", help="Path to the input file")

parser.add_argument(
    # Short and long options
    "-s", "--save",
    # Help description
    help="File to save the hash"
)

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
parser.add_argument(
    "-c", "--compare",
    help="File containing the saved hash"
)

# Allow the user to display the generated hash
parser.add_argument(
    "-p", "--print",
    action="store_true",
    help="Display the hash"
)

args = parser.parse_args()

hash_value = generate_hash(args.file, args.algorithm)

if args.compare:
    compare_hash(hash_value, args.compare)

if args.save:
    save_hash(hash_value, args.save)

# Display the hash when requested or by default
if args.print or (not args.save and not args.compare):
    print("Algorithm:", args.algorithm)
    print("File:", args.file)
    print("Hash:", hash_value)