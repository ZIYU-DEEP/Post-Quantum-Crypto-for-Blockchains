"""
Filename: request.py
Author: Ziyu Ye

User will only need his user id, info id, the algorithm used of KEM,
and ciphertext_abs, along with the transaction details (e.g., value)
to make the transaction. The private key will never be transmitted.
"""

import qure
import argparse


# ############################################
# Preparation
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

# Argument for info id
parser.add_argument('-i', '--key_id', type=str,
                    default='0',
                    help='Your info id for this key in SeQure.')

# Argument for ciphertext
parser.add_argument('-ca', '--ciphertext_abs', type=str,
                    default='7f9da539c7ca9cbab104cb2a76d93be0',
                    help='The corresponding ciphertext for this info.')

# Argument for url
parser.add_argument('-url', '--url', type=str,
                    default='https://eth-goerli.g.alchemy.com/v2/fss_yq1JH8COJapGjbQCuaCD77JrjQRp',
                    help='The url used to connect to web3.')

parser.add_argument('-ci', '--chain_id', type=int,
                    default=5,
                    help='See docs.alchemy.com/docs/how-to-add-alchemy-rpc-endpoints-to-metamask#step-4-fill-in-the-network-details')

# Argument for account address
parser.add_argument('-af', '--account_from', type=str,
                    default='0xA5b372E60a60A70f2c6ACB87710eba30Ecc4D479',
                    help='The account of the payer.')

parser.add_argument('-at', '--account_to', type=str,
                    default='0xA059250F4b97bbB3C081f6D9e1fC7249c6Ea2A0c',
                    help='The account of the receiver.')

# Argument for the value in this transaction
parser.add_argument('-v', '--value', type=float,
                    default=0.0001,
                    help='The value used in transaction')

# Below can be omitted
parser.add_argument('-g', '--gas', type=int,
                    default=21000,
                    help='The gas used in transaction')

parser.add_argument('-gp', '--gas_price', type=int,
                    default=200000000,
                    help='The gas price used in transaction')

# Argument for the root of the database
parser.add_argument('-r', '--root', type=str,
                    default='./database',
                    help='The root of the database.')

# Parse the arguments
p = parser.parse_args()


# ######################################################################
# 1. PQC Transaction
# ######################################################################
if __name__ == '__main__':

    # Call package to encrypt and save info
    qure.safe_transaction(p.user_id,
                          p.key_id,
                          p.ciphertext_abs,
                          p.account_from,
                          p.account_to,
                          p.value,
                          p.url,
                          p.chain_id,
                          p.gas,
                          p.gas_price,
                          p.root)
