pragma solidity ^0.4.6;

contract operate_recoder {
    
    struct operate {
		bytes32 pic_hash;
		uint32 pic_type;
		uint8 operate;
		uint64 timestamp;
		uint32 saved_pos;
    }

    address proposals;

    constructor () public {
	    proposals = msg.sender;
    }
    
    mapping (address => operate[]) all_operate;

    function set_operate (operate _operate) internal constant returns (uint len) {
		len = all_operate[msg.sender].push(_operate);
    }

    function getLatest_pic_hash (address sender)internal constant returns (operate ret_str){
    	operate[] memory tmp = all_operate[sender];
    	ret_str = tmp[tmp.length-1];
    }
    
    function user_set (bytes32 _pic_hash,uint32 _pic_type,uint8 _operate,uint64 _timestamp,uint32 _saved_pos)returns(uint){
        require(_pic_hash.length==32,"pic_hash is not correct!!");
        operate memory tmp = operate(_pic_hash, _pic_type, _operate, _timestamp, _saved_pos);
        return (set_operate(tmp));
    }

    function user_getlatest (address addr) returns (bytes32 _pic_hash,uint32 _pic_type,uint8 _operate,uint64 _timestamp,uint32 _saved_pos){
        operate memory tmp = getLatest_pic_hash(addr);
        _pic_hash = tmp.pic_hash;
        _pic_type = tmp.pic_type;
        _operate = tmp.operate;
        _timestamp = tmp.timestamp;
        _saved_pos = tmp.saved_pos;
    }

}
