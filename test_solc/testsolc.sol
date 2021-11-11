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

    function get_operate_test (address sender) constant returns (bytes32) {
	
        return operate_all[sender].pic_hash;
    }

    function testtttt () returns (bytes8) {
	return "asdfasdf";
    }

    function ret2num () returns (uint){
		return 123456;
    }
}
