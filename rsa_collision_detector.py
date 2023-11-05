from collections import defaultdict

# Dictionary to store key pairs and public keys
key_pairs = defaultdict(list)

# Read the key pair and public key files
for i in range(num_keys):
    key_name = "key{}".format(i)
    with open("{}.pem".format(key_name), "rb") as f:
        key_pair = f.read()
    with open("{}_public.pem".format(key_name), "rb") as f:
        public_key = f.read()

    # Store the key pair and public key in the dictionary
    key_pairs[key_pair].append(public_key)

# Check for collisions in the key pairs
for key_pair, public_keys in key_pairs.items():
    if len(public_keys) > 1:
        print("Collision detected in key pair {}".format(key_pair))
        print("Associated public keys: {}".format(public_keys))
