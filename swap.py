from config import NODE_URL
from config import coins_map, pr_key

from liquidswap.client import LiquidSwapClient


#Инициализируем аккаунт
my_account = LiquidSwapClient(NODE_URL, coins_map, pr_key)







#МОЙ ПЕРВЫЙ КОД НЕ ИСПОЛЬЗУЯ SDK

# def main():
#     my_account = Account(
#             account_address=AccountAddress.from_key(private_key.public_key()),
#             private_key=private_key
#         )

#     print(my_account.address())

#     my_balance = rest_client.account_balance(my_account.address())
#     print(my_balance)

#     txn_hash = rest_client.transfer(my_account, "0xeb941767d006512bd091c4b2d0b52d19281eddb55f997babf0b83e2c201c0359", 1_000_000_0) 

#     await rest_client.wait_for_transaction(txn_hash)  
#     print(txn_hash)


# main()