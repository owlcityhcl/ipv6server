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

    function set_operate (uint _number,uint _timestamp) internal constant returns (uint len) {
		len = all_operate[0].push(operate({pic_hash:"_pic_hash",number:_number,timestamp:_timestamp}));
    }

    function getLatest_pic_hash (address sender)internal constant returns (bytes32 _pic_hash,uint _number,uint _timestamp){
    	operate[] memory tmp = all_operate[0];
		_pic_hash =  tmp[0].pic_hash;
		_number = tmp[0].number;
		_timestamp = tmp[0].timestamp;
    }
    
    function user_set ()returns(uint){
        return set_operate(123,123);
    }

    function user_get () returns (bytes32 pic_hash,uint number,uint timestamp){
        (pic_hash,number,timestamp) = getLatest_pic_hash(proposals);
    }

}
