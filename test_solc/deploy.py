import json
import web3

from web3 import Web3, HTTPProvider, TestRPCProvider
from solc import compile_source
from web3.contract import ConciseContract


contract_source_code = '''
pragma solidity ^0.4.6;

contract pic_recoder {
    
    struct operate {
        bytes32 pic_hash;
        bytes32 own_name;
        uint32 pic_type;
        uint64 timestamp;
        uint32 saved_pos;
    }
    
    bytes32[] cache_picHash;
    bytes32[] cache_own_name;
    uint32[] cache_picType;
    uint64[] cache_timestamp;
    uint32[] cache_saved_pos;
    
    
    bytes32 last_addr;
    uint last_start;
    uint last_lenght;
    uint new_add;

    constructor () public {
        new_add++;
        last_addr ="0";
    }
    
    mapping (bytes32 => operate[]) all_operate;

    function set_operate (operate _operate,bytes32 id_card) internal constant returns (uint len) {
        new_add=new_add+1;
        len = all_operate[id_card].push(_operate);
    }

    function getLatest_operate (bytes32 id_card)internal constant returns (operate ret_str){
        operate[] memory tmp = all_operate[id_card];
        ret_str = tmp[tmp.length-1];
    }
    
    function set_cache (bytes32 sender)internal constant returns(uint){
       
        operate[] memory tmp = all_operate[sender];
        if (tmp.length==0) {
            return 0;
        }
       uint sum_length=0;
       
        for (uint i = tmp.length-1; i>=0 ;i--){
            if (sum_length >= cache_picHash.length){
                cache_picHash.length++;
                cache_picType.length++;
                cache_own_name.length++;
                cache_timestamp.length++;
                cache_saved_pos.length++;
            }
            
            cache_picHash[sum_length] = tmp[i].pic_hash;
            cache_own_name[sum_length] = tmp[i].own_name;
            cache_picType[sum_length] = tmp[i].pic_type;
            cache_timestamp[sum_length] = tmp[i].timestamp;
            cache_saved_pos[sum_length] = tmp[i].saved_pos;
            sum_length++;
            if (i==0) break;
            
        }
        return sum_length;
        
    }
    
    function user_set (bytes32 _pic_hash,bytes32 _own_name,uint32 _pic_type,uint64 _timestamp,uint32 _saved_pos,bytes32 _id_card)public{
        require(_pic_hash.length==32,"pic_hash is not correct!!");
        operate memory tmp = operate(_pic_hash, _own_name, _pic_type , _timestamp, _saved_pos);
        set_operate(tmp,_id_card);
    }

    function user_getlatest (bytes32 id_card) public returns (bytes32 _pic_hash,bytes32 _own_name,uint32 _pic_type,uint64 _timestamp,uint32 _saved_pos){
        operate memory tmp = getLatest_operate(id_card);
        _pic_hash = tmp.pic_hash;
        _pic_type = tmp.pic_type;
        _own_name = tmp.own_name;
        _timestamp = tmp.timestamp;
        _saved_pos = tmp.saved_pos;
    }
    
    function user_setlist(bytes32 addr)public{
        if (false && addr == last_addr ){
            return ;
        }
        else{
            uint all_length = set_cache( addr) ;
            last_addr = addr;
            last_lenght=all_length;
            new_add = 0;
        }
        
    }
    
    function user_getlist (bytes32 addr)public returns (bytes32[],bytes32[],uint32[],uint64[],uint32[],uint){
        require(addr == last_addr,"error !! wrong address !! ");
        return (cache_picHash,cache_own_name,cache_picType,cache_timestamp,cache_saved_pos,last_lenght);
    }

}
'''

compiled_sol = compile_source("") # Compiled source code
contract_interface = compiled_sol['<stdin>:pic_recoder']

# web3.py instance
w3 = Web3(HTTPProvider('http://127.0.0.1:8545'))

# Instantiate and deploy contract
contract = w3.eth.contract(abi=contract_interface['abi'], bytecode=contract_interface['bin'])

# Get transaction hash from deployed contract
w3.personal.unlockAccount(w3.eth.accounts[0],'hunter2')
tx_hash = contract.deploy(transaction={'from': w3.eth.accounts[0], 'gas': 3000000})

# Get tx receipt to get contract address
w3.eth.getTransactionReceipt(tx_hash)
contract_interface['abi']
print (tx_receipt)
print (abi)
contract_address = tx_receipt['contractAddress']
print (contract_address)

# Contract instance in concise mode
    


