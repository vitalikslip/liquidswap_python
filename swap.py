from config import NODE_URL
from config import coins_map, pr_key


from liquidswap.client import LiquidSwapClient


#Инициализируем аккаунт
my_account = LiquidSwapClient(NODE_URL, coins_map, pr_key)

my_account.swap("amAPT", "APT", 0.10252649, 0.099)





#Перевод APT с аккаунта на аккаунт

# def main():
#     my_account = Account(
#             account_address=AccountAddress.from_key(private_key.public_key()),
#             private_key=private_key
#         )

#     print(my_account.address())

#     my_balance = rest_client.account_balance(my_account.address())
#     print(my_balance)

#     txn_hash = rest_client.transfer(my_account, "", 1_000_000_0) 
#     
#     print(txn_hash)


# main()