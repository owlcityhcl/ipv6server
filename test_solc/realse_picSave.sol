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
    
        
    function del_pic (bytes32 _id_card,uint64 old_timestamp){
        for (uint i = all_operate [_id_card].length-1;i>0;i--){
            if (all_operate [_id_card][i].timestamp==old_timestamp){
                all_operate [_id_card][i].pic_hash=0;
                return;
            }
            if (i==0) break;
        }
    }
    
    function edit_pic (bytes32 _pic_hash,bytes32 _own_name,uint32 _pic_type,uint64 old_timestamp,uint32 _saved_pos,bytes32 _id_card,uint64 _timestamp){
        del_pic(_id_card,old_timestamp);
        operate memory tmp = operate(_pic_hash, _own_name, _pic_type , _timestamp, _saved_pos);
        set_operate(tmp,_id_card);
        
        
    }

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
