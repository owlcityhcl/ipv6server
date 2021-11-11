import json

import web3
import random
import string
import time
import socket
import logging
import struct

import web3.eth
from web3 import Web3,HTTPProvider,IPCProvider,WebsocketProvider
from eth_photo.models import UploadedImageModel
from eth_photo.models import operate_recoder
contract_address = "0xfe436fa51c0d01f471bdb3255306d460c01a5e2c"
with open('../mysite/eth_photo/pic_recoder.abi', 'r') as f:
    abi = json.load(f)
def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip

class eth_connect:
    eth_loc = ""
    def __init__(self, address, pass_word):
        self.w3 = web3.Web3(HTTPProvider('HTTP://127.0.0.1:7545'))
        accounts = self.w3.eth.accounts
        print("accountsssssssssssssssssssss---", accounts)
        self.contract = self.w3.eth.contract(address = self.w3.toChecksumAddress(contract_address), abi= abi)
        self.account0 = accounts[0]
        print("account00000000000000000000000000000------",self.account0)
        self.address = address
        self.password = pass_word

    def get_picInfo(self, id_in):
        # self.w3.personal.unlockAccount(self.address, self.password)
        # self.contract.functions.user_setlist(id_in).transact({"from":address})
        # result = self.contract.functions.user_getlist().call()

        num_ip = socket.ntohl(struct.unpack("I",socket.inet_aton(str(get_host_ip())))[0])
        #result = [ ["3707245c41b18ec6dd28b3c2f9fd3a83"],["1"],[2],[1525533076],[num_ip],["5"],1]
        result = []
        pic_hash_list = []
        own_name_list = []
        pic_type_list = []
        timestamp_list = []
        saved_pos_list = []
        id_card_list = []
        #logging.debug (id_in)

        person_info = UploadedImageModel.objects.filter(id_card=id_in)
        for i in person_info:
            pic_hash_list.append(i.pic_hash)
            own_name_list.append(i.own_name)
            pic_type_list.append(i.pic_type)
            timestamp_list.append(i.timestamp)
            saved_pos_list.append(i.saved_pos)
            id_card_list.append(i.id_card)
            #logging.debug(pic_hash_list)

        result = [pic_hash_list,own_name_list,pic_type_list,timestamp_list,saved_pos_list,id_card_list,len(person_info)]
        return result

    def get_record(self):
        # self.w3.personal.unlockAccount(self.address, self.password)
        # self.contract.functions.user_setlist(id_in).transact({"from":address})
        # result = self.contract.functions.user_getlist().call()

        result = []

        pic_hash_list = []
        pic_timestamp_list = []
        operater_name_list = []
        operate_type_list = []
        operater_time_list = []

        operate_info = operate_recoder.objects.all()
        for i in operate_info:
            pic_hash_list.append(i.pic_hash)
            pic_timestamp_list.append(i.pic_timestamp)
            operater_name_list.append(i.operater_name)
            operate_type_list.append(i.operate_type)
            operater_time_list.append(i.operater_time)

        result = [pic_hash_list,pic_timestamp_list,operater_name_list,operate_type_list,operater_time_list]

        return result

    def savePic_to_blockchain (self, pic_hash, own_name ,pic_type , timestamp, saved_pos , id_card):
        #ta = self.contract.functions.user_set("0bd3ce3eb677cb0c4fb9bb706d3d177c_1635854144", "Jhon" ,1 , 1635854144, 1921681115 , "111").transact({"from": self.account0 })
        ta = self.contract.functions.user_set(pic_hash, own_name ,pic_type , timestamp,saved_pos , id_card).transact({"from": self.account0 })
        print("ta--------------------------", ta)
        return self.w3.toHex(ta)
        #return "0xc21fFA08499A260fc29d1430A6691D263c819c89"

    def set_operate_record(self,pic_hash,pic_timestamp,operater_name,operate_type,operater_time):
        # self.w3.personal.unlockAccount(self.address, self.password)
        # self.contract.functions.user_set(pic_hash, own_name ,pic_type , timestamp, saved_pos , id_card).transact({"from":address})
        operate_recoder.objects.create(pic_hash=pic_hash,pic_timestamp=pic_timestamp,operater_name=operater_name,operate_type=operate_type,operater_time=operater_time)
        return self.address



