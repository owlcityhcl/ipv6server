import json
import web3
import binascii

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
		string pic_hash;
	}

	mapping (address => server_operate) public operate_all;
	
	address public proposals;

	constructor (){
		proposals = msg.sender;
		none_data = "no data";
	}

	function set_operate (address sender,uint8 _operate,uint64 _operater_ip,uint64 _timestamp,string _pic_hash) public {
		operate_all[sender].operate = _operate;
		operate_all[sender].operater_ip = _operater_ip;
		operate_all[sender].timestamp = _timestamp;
		operate_all[sender].pic_hash = _pic_hash;
		

	}

	bytes32 public none_data;

    function get_operate_test (address sender) constant returns (string) {
	
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

w3 = Web3(IPCProvider("/home/shura/Desktop/chain/geth.ipc"))
contract_address ="0x5e4a6db2308f85fc449dd3151df99d91d41abf88"

compiled_sol = compile_source(contract_source_code) 

contract_interface = compiled_sol['<stdin>:operate_re']

contract_instance = w3.eth.contract(abi=contract_interface['abi'], address=contract_address, ContractFactoryClass=ConciseContract)

#contract_instance.set_operate(w3.eth.accounts[0],1,123,456,Web3.toBytes(text="5645asdfasdf46456s"),transact={'from': w3.eth.accounts[0]})

# Getters + Setters for web3.eth.contract object
#contract_instance.setGreeting('12', transact={'from': w3.eth.accounts[0]})
#print('Setting value to: N')
print ('{0}'.format(w3.eth.accounts[0]))
#print('Contract value: {}'.format(contract_instance.get_operate_test(w3.eth.accounts[0])))
print (contract_instance.testtttt())
print (contract_instance.ret2num())