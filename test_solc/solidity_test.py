import json
import web3
import binascii
import sys
import time
import pprint

from web3 import Web3, TestRPCProvider, IPCProvider
from solc import compile_source
from web3.contract import ConciseContract

contract_source_code = '''
pragma solidity ^0.4.0;

contract operate_re {
	struct server_operate {
		uint8 operate;
		uint64 operater_ip;
		uint64 timestamp;
		bytes32 pic_hash;
	}

	mapping (address => server_operate) public operate_all;
	
	address public proposals;

	constructor (){
		proposals = msg.sender;
		none_data = "no data";
	}

	function set_operate (address sender,uint8 _operate,uint64 _operater_ip,uint64 _timestamp,bytes32 _pic_hash) public {
		operate_all[sender].operate = _operate;
		operate_all[sender].operater_ip = _operater_ip;
		operate_all[sender].timestamp = _timestamp;
		operate_all[sender].pic_hash = _pic_hash;
		

	}

	bytes32 public none_data;

    function get_operate_test (address sender) constant returns (bytes32)  {
	
        return operate_all[sender].pic_hash;
    }

    function testtttt () returns (bytes8) {
	return "asdfasdf";
    }

    function ret2num () returns (uint){
		return 123456;
    }
}


'''
def deploy_contract(w3, contract_interface):
    tx_hash = w3.eth.contract(
        abi=contract_interface['abi'],
        bytecode=contract_interface['bin']).deploy()

    address = w3.eth.getTransactionReceipt(tx_hash)['contractAddress']
    return address



w3 = Web3(IPCProvider("/home/shura/Desktop/chain/geth.ipc"))

compiled_sol = compile_source(contract_source_code) # Compiled source code
#contract_interface = compiled_sol['<stdin>:Greeter']
contract_interface = compiled_sol['<stdin>:operate_re']

# web3.py instance


contract = w3.eth.contract(abi=contract_interface['abi'], bytecode=contract_interface['bin'])

tx_hash = contract.deploy(transaction={'from': w3.eth.accounts[0], 'gas': 410000})
tx_receipt = w3.eth.getTransactionReceipt(tx_hash)
#contract_address = tx_receipt['contractAddress']

store_var_contract = w3.eth.contract(
   address=address,
   abi=contract_interface['abi'])


gas_estimate = store_var_contract.functions.setVar(255).estimateGas()
print("Gas estimate to transact with setVar: {0}\n".format(gas_estimate))

if gas_estimate < 100000:
  print("Sending transaction to setVar(255)\n")
  tx_hash = store_var_contract.functions.setVar(255).transact()
  receipt = wait_for_receipt(w3, tx_hash, 1)
  print("Transaction receipt mined: \n")
  pprint.pprint(dict(receipt))
else:
  print("Gas cost exceeds 100000")


