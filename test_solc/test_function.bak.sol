pragma solidity ^0.4.6;

contract test_function {
    
    struct simple_struct {
		bytes32 pic_hash;
		uint number;
		address sender;
    }
    
    bytes10 none_data;
    address proposals;
    uint count;
    simple_struct[] ssss;

    constructor () public {
	    proposals = msg.sender;
	    none_data = "no data";
	    count=0;
    }


    function set_test ()internal constant returns (uint len,bytes32 lenn) {
		len =ssss.push(simple_struct({pic_hash:"123",number:123,sender:msg.sender}));
		
		lenn = ssss[0].pic_hash;
    }
    

    function get_pic_hash (uint pos)internal constant returns (bytes32 pic_hash){
    	
		pic_hash = ssss[0].pic_hash;
		uint number = ssss[0].number;
		address sender = ssss[0].sender;
	
    }
    
    function sss ()returns(uint len,bytes32 lenn){
        return set_test();
    }
    
    function gggt (uint pos) constant returns (bytes32 ttt){
        
        ttt = get_pic_hash(pos);
    }

}
