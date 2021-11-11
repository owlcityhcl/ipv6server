pragma solidity ^0.4.6;

contract operate_recoder {
    
    struct operate {
		bytes32 pic_hash;
		uint number;
		uint timestamp;
    }

    address proposals;

    constructor () public {
	    proposals = msg.sender;
    }
    
    mapping (address => operate[]) all_operate;

    function set_operate (bytes32 _pic_hash,uint _number,uint _timestamp,address sender) internal constant returns (uint len) {
		len = all_operate[sender].push(operate({pic_hash:_pic_hash,number:_number,timestamp:_timestamp}));
    }

    function getLatest_pic_hash (address sender)internal constant returns (bytes32 _pic_hash,uint _number,uint _timestamp){
    	operate[] memory tmp = all_operate[sender];
		_pic_hash =  tmp[tmp.length-1].pic_hash;
		_number = tmp[tmp.length-1].number;
		_timestamp = tmp[tmp.length-1].timestamp;
    }
    
    function user_set (bytes32 _pic_hash,uint _number,uint _timestamp,address sender)returns(uint){
        return set_operate(_pic_hash,_number,_timestamp,sender);
    }

    function user_get (address addr) returns (bytes32 pic_hash,uint number,uint timestamp){
        (pic_hash,number,timestamp) = getLatest_pic_hash(addr);
    }

}
