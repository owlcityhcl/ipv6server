import json
import time
import  web3
from web3 import Web3


#w3 = web3.Web3(web3.IPCProvider('/home/ub16ipv6/Downloads/mychain/mychain/geth.ipc'))
w3 = web3.Web3(web3.HTTPProvider('HTTP://127.0.0.1:7545'))
accounts = w3.eth.accounts
print("accounts---",accounts)
with open('../mysite/eth_photo/pic_recoder.abi', 'r') as f:
    abi = json.load(f)

with open('../mysite/eth_photo/pic_recoder.bin', 'r') as f:
    bin = f.read()

factory = w3.eth.contract(abi=abi,bytecode=bin)
tx_hash = factory.constructor().transact({'from':accounts[0]})
receipt = w3.eth.waitForTransactionReceipt(tx_hash)
print(receipt)

# addr = 0xC1951BFA13A2840758b4F85D2e4381D2ABEa13b3
#
# factory = w3.eth.contract(abi=abi,address=Web3.toChecksumAddress(addr))
#
# tmail = factory.functions.user_set("0xa2056a0479c464a2f0a62d10229a68de6f7c7f05", "1",1,4, 27, str(1234)).transact({'from':accounts[0]})
# #tmail2 = factory.functions.user_getlist(2).call()
# print(w3.toHex(tmail))
# account = "0x99ff43e3a793ea1bdf987549d9e8e75bb2188a1d"
# contract = w3.eth.contract(abi=abi, bytecode=code)
# option = {'from': account, 'gas': 1000000}
# tx_hash = contract.deploy(transaction={'from': "0x99ff43e3a793ea1bdf987549d9e8e75bb2188a1d", 'gas': 3000000})
# tx_hash = contract.constructor().transact(option)
#
# # 等待挖矿使得交易成功
# tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
# print(tx_receipt.contractAddress)
#
# # Get tx receipt to get contract address
# w3.eth.getTransactionReceipt(tx_hash)
# print("deploy-----------------hash", w3.eth.getTransactionReceipt(tx_hash))
# false = False
# new_address = w3.toChecksumAddress("0xD7ACd2a9FD159E69Bb102A1ca21C9a3e3A5F771B")
#
# t = w3.eth.contract(address = new_address, abi = abi)
#
# print ("ttttttttttttttttttttttttttttttttttttttt",t)
# # t.functions.user_set("0xa2056a0479c464a2f0a62d10229a68de6f7c7f05", 4, 27, new_address).call()
# # sec = w3.toChecksumAddress("0x15f39bf19f8380d10ab34272a5d45b67a88c72c5")
# # t.functions.user_set("0xa2056a0479c464a2f0a62d10229a68de6f7c7f05", 4, 27, sec).call()
# # t.functions.user_set("0xa2056a0479c464a2f0a62d10229a68de6f7c7f05", 4, 27, new_address).transact({"from": w3.toChecksumAddress("0xa3dcFc709BB133113f807fA47777d8277EAbcdf5")})
# tmail = t.functions.user_set("0xa2056a0479c464a2f0a62d10229a68de6f7c7f05", "1",1,4, 27, new_address).transact({"from": w3.toChecksumAddress("0x406DE924e6b2FC9E41625ED7bd1EE0c6bb3f0224")})
# tx = w3.eth.waitForTransactionReceipt(tmail)
# print("txxxxxxxxxxxxxxxxxxxxxxxxxxx",tx)
# tmail2 = t.functions.user_getlist(0).call()
#
# print ("call------------------------------------",tmail2)
# #t.functions.user_set("0xa2056a0479c464a2f0a62d10229a68de6f7c7f05", 4, 27, sec).call()
