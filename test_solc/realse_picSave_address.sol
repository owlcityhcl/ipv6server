pragma solidity ^0.4.6;

contract pic_recoder {
    
    struct operate {
        bytes32 pic_hash;
        bytes32 own_name;
        uint32 pic_type;
        uint64 timestamp;
        uint32 saved_pos;
        bytes32 id_card;
    }
    
    bytes32[] cache_picHash;
    bytes32[] cache_own_name;
    uint32[] cache_picType;
    uint64[] cache_timestamp;
    uint32[] cache_saved_pos;
    bytes32[] cache_id_card;
    
    
    address last_addr;
    uint last_start;
    uint last_lenght;
    uint new_add;

    constructor () public {
        new_add++;
        last_addr =0;
    }
    
    mapping (address => operate[]) all_operate;

    function set_operate (operate _operate) internal constant returns (uint len) {
        new_add=new_add+1;
        len = all_operate[msg.sender].push(_operate);
    }

    function getLatest_operate (address sender)internal constant returns (operate ret_str){
        operate[] memory tmp = all_operate[sender];
        ret_str = tmp[tmp.length-1];
    }
    
    function set_cache (address sender,uint list_start,uint list_length)internal constant returns(uint){
        operate[] memory tmp = all_operate[sender];
        uint reserve = tmp.length-1-list_start;
        uint sum_length = 0;
        uint min_num;
        
        if (reserve<list_length) {
            min_num=0;
        }
        else{
            min_num = reserve+1-list_length;
        }
        if (tmp.length<1+list_start){
            reserve = 0;
        }
        
        for (uint i = reserve; i>=0 && i>=min_num;i--){
            if (sum_length >= cache_picHash.length){
                cache_picHash.length++;
                cache_picType.length++;
                cache_own_name.length++;
                cache_timestamp.length++;
                cache_saved_pos.length++;
                cache_id_card.length++;
            }
            
            cache_picHash[sum_length] = tmp[i].pic_hash;
            cache_own_name[sum_length] = tmp[i].own_name;
            cache_picType[sum_length] = tmp[i].pic_type;
            cache_timestamp[sum_length] = tmp[i].timestamp;
            cache_saved_pos[sum_length] = tmp[i].saved_pos;
            cache_id_card[sum_length] = tmp[i].id_card;
            sum_length++;
            if (i==0) break;
            
        }
        return sum_length;
        
    }
    
    function user_set (bytes32 _pic_hash,bytes32 _own_name,uint32 _pic_type,uint64 _timestamp,uint32 _saved_pos,bytes32 _id_card)public{
        require(_pic_hash.length==32,"pic_hash is not correct!!");
        operate memory tmp = operate(_pic_hash, _own_name, _pic_type , _timestamp, _saved_pos,_id_card);
        set_operate(tmp);
    }

    function user_getlatest (address addr) public returns (bytes32 _pic_hash,bytes32 _own_name,uint32 _pic_type,uint64 _timestamp,uint32 _saved_pos,bytes32 _id_card){
        operate memory tmp = getLatest_operate(addr);
        _pic_hash = tmp.pic_hash;
        _pic_type = tmp.pic_type;
        _own_name = tmp.own_name;
        _timestamp = tmp.timestamp;
        _saved_pos = tmp.saved_pos;
        _id_card = tmp.id_card;
    }
    
    function user_setlist(address addr,uint list_start,uint list_length)public{
        if (false && addr == last_addr && last_start+new_add<=list_start && last_start+new_add+last_lenght>=list_start+list_length ){
            return ;
        }
        else{
            uint all_length = set_cache( addr, list_start, list_length) ;
            last_addr = addr;
            last_start=list_start;
            last_lenght=all_length;
            new_add = 0;
        }
        
    }
    
    function user_getlist (address addr)public returns (bytes32[],bytes32[],uint32[],uint64[],uint32[],bytes32[],uint){
        require(addr == last_addr,"error !! wrong address !! ");
        return (cache_picHash,cache_own_name,cache_picType,cache_timestamp,cache_saved_pos,cache_id_card,last_lenght);
    }

}
