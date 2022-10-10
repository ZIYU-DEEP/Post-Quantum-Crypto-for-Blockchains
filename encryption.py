"""
Filename: encryption.py
Author: Ziyu Ye
Inputs:
    - private key
    - user id
    - kem algorithm
    - root of database
Returns:
    - info id (key index for the user)
    - KEM public key
    - KEM secret key
    - KEM ciphertext
    - SKE salt
    - encrypted private key

User will only need his user id, info id, the algorithm used of KEM,
and ciphertext_abs, while we save all.
"""

import qure
import argparse


# ############################################
# 0. Preparation
# ############################################
# ===========================================
# 0.0. Parameters
# ===========================================
# Initialize the parser
parser = argparse.ArgumentParser()

# Argument for user id
parser.add_argument('-u', '--user_id', type=str,
                    default='leviathan',
                    help='Your user id in SeQure.')

# Argument for the private key
parser.add_argument('-k', '--private_key', type=str,
                    default='217d5c81a38240e09ee05bc4ab3efce2eb91d24973162f9833ed18aa7b4460b9',
                    help='The private key used for transaction on blockchain.')

# Argument for the kem algorithm
parser.add_argument('-a', '--kem_algo', type=str,
                    default='Kyber512',
                    help='The KEM algorithm, e.g., Kyber1024.')

# Argument for the root of the database
parser.add_argument('-r', '--root', type=str,
                    default='./database',
                    help='The root of the database.')

# Parse the arguments
p = parser.parse_args()
user_id = p.user_id
message = p.private_key
kem_algo = p.kem_algo
root = p.root  # Remove this in future


# ######################################################################
# 1. PQC Message Encryption
# ######################################################################
if __name__ == '__main__':

    # Call package to encrypt and save info
    qure.safebox(p.user_id, p.private_key, p.kem_algo, p.root)
