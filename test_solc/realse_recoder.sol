pragma solidity ^0.4.6;

    contract operate_recoder {
     
        bytes32[] pic_hash;
        uint64[] pic_timestamp;
        address[] operater_name;
        uint8[] operate_type;
        uint64[] operater_time;
        
        

        constructor () public {
            
        }
        
        function set_operate(bytes32 _pic_hash,uint64 _pic_timestamp,address _operater_name,uint8 _operate_type,uint64 _operate_time) public {
            uint length = pic_hash.length;
            
            pic_hash.length++;
            pic_timestamp.length++;
            operater_name.length++;
            operate_type.length++;
            operater_time.length++;
            
            pic_hash[length] = _pic_hash;
            pic_timestamp[length] = _pic_timestamp;
            operater_name[length] = _operater_name;
            operate_type[length] = _operate_type;
            operater_time[length] = _operate_time;
            
        }
        
        function getLatest_operate() constant returns (bytes32 _pic_hash,uint64 _pic_timestamp,address _operater_name,uint8 _operate_type,uint64 _operate_time){
            uint length = pic_hash.length-1;
            
            _pic_hash = pic_hash[length];
            _pic_timestamp = pic_timestamp[length];
            _operater_name = operater_name[length];
            _operate_type = operate_type[length];
            _operate_time = operater_time[length];
        }
        
        function getAll_opeate() constant returns (bytes32[] ,uint64[],address[] ,uint8[] ,uint64[] ){
            return (pic_hash,pic_timestamp,operater_name,operate_type,operater_time);
        }
        
        function getRange_list(uint list_length)constant returns (bytes32[] ,uint64[],address[] ,uint8[] ,uint64[],uint ){
            uint tempL = list_length;
            
            bytes32[] temp_hash;
            uint64[] temp_timestamp;
            address[] temp_operate_name;
            uint8[] temp_operate_type;
            uint64[] temp_operate_time;
            uint reserve;
            
            uint tempN = 0;
            for (uint i=pic_hash.length; i > 0;i--){
                temp_hash.length++;
                temp_timestamp.length++;
                temp_operate_name.length++;
                temp_operate_type.length++;
                temp_operate_time.length++;
                
                temp_hash[tempN] = pic_hash[i];
                temp_timestamp[tempN] = pic_timestamp[i];
                temp_operate_name[tempN] = operater_name[i];
                temp_operate_type[tempN] = operate_type[i];
                temp_operate_time[tempN] = operater_time[i];
                tempN++;
                tempL--;
                if (tempL==0) break;
                if (i==0) break;
            }
            return (temp_hash,temp_timestamp,temp_operate_name,temp_operate_type,temp_operate_time,tempN);
        }
        

    }