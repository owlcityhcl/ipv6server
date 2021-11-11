from eth_photo.models import ImageModel
from eth_photo.models import eth_account
from eth_photo.models import operate_recoder
from .eth_connect import *
import logging
import struct,socket

# UploadedImageModel matching query does not exist.	

class Operate_list(object):
	"""docstring for search_person"""
	def __init__(self, address):
		super(Operate_list, self).__init__()
		self.address = address
		# get address and password from the database
	def get_page (self,page):
		result = []

		pic_hash_list = []
		pic_timestamp_list = []
		operater_name_list = []
		operate_type_list = []
		operater_time_list = []

		recoder = operate_recoder.objects.all().order_by('-operater_time')[20*(page-1):20*(page)]
		for i in operate_info:
			pic_hash_list.append(i.pic_hash)
			pic_timestamp_list.append(i.pic_timestamp)
			operater_name_list.append(i.operater_name)
			operate_type_list.append(i.operate_type)
			operater_time_list.append(i.operater_time)

		result = [pic_hash_list,pic_timestamp_list,operater_name_list,operate_type_list,operater_time_list]

		result_len = len(result[0])
		ret_dic = []
		for i in range(result_len):
			data_time = time.asctime( time.localtime( result[1][i]) ) 
			data_picname = str(result[0][i]) + '_' + str(result[1][i])
			if str(result[3][i]) == '0':
				data_type = "上传" 
			else:
				data_type = "查看"
			temp={"data_time":data_time,"data_type":data_type,"data_account":result[2][i],"data_picname":data_picname}
			ret_dic.append(temp)
		return ret_dic

	
	def get(self):
		account_using = None
		try:
			account_using = eth_account.objects.get(address = self.address)
		except Exception as e:
			logging.debug (e)
		if not account_using:
			logging.debug ("ERROR: can't find the address of eth in database")
			return None
		t = eth_connect(account_using.address, account_using.password)
		#logging.debug(type(pic_hash))
		result = t.get_record()
		result_len = len(result[0])
		ret_dic = []
		for i in range(result_len):
			data_time = time.asctime( time.localtime( result[1][i])  )
			data_picname = str(result[0][i]) + '_' + str(result[1][i])
			logging.debug(str(data_time)+'      '+str(data_picname))
			if str(result[3][i]) == '0':
				data_type = "上传" 
			else:
				data_type = "查看"
			temp={"data_time":data_time,"data_type":data_type,"data_account":result[2][i],"data_picname":data_picname}
			ret_dic.append(temp)
			if i == 20: 
				break

		return ret_dic

	def set (self,pic_hash,pic_timestamp,operater_name,operate_type,operater_time):
		account_using = None
		try:
			account_using = eth_account.objects.get(address = self.address)
		except Exception as e:
			logging.debug (e)
		if not account_using:
			logging.debug ("ERROR: can't find the address of eth in database")
			return None
		t = eth_connect(account_using.address, account_using.password)
		#logging.debug(type(pic_hash))
		result = t.set_operate_record(pic_hash,pic_timestamp,operater_name,operate_type,operater_time)

		return result
