from web3 import Web3
from eth_account import Account
import secrets

# Connect to Avalanche C-Chain
avalanche_url = "https://api.avax-test.network/ext/bc/C/rpc"
w3 = Web3(Web3.HTTPProvider(avalanche_url))
w3.eth.chain_id = 43113

def create_wallet():
    # Generate a private key
    private_key = "0x" + secrets.token_hex(32)
    
    # Create account from private key
    account = Account.from_key(private_key)
    print("address " + account.address)
    print("private " + private_key)
    
    return {
        "address": account.address,
        "private_key": private_key
    }

def get_balance(address: str) -> str:
    """
    Get AVAX balance for an address
    Returns balance in AVAX (not Wei)
    """
    try:
        # Get balance in Wei
        balance_wei = w3.eth.get_balance(address)
        # Convert Wei to AVAX (18 decimals)
        balance_avax = w3.from_wei(balance_wei, 'ether')
        return balance_avax
    except Exception as e:
        print(f"Error getting balance: {e}")
        return 0
# Example usage
def main():
    wallet = create_wallet()
    print(f"New Avalanche C-Chain Address: {wallet['address']}")
    print(f"Private Key: {wallet['private_key']}")
    
    # Verify connection
    print(f"Connected to Avalanche: {w3.is_connected()}")
    
if __name__ == "__main__":
    main()