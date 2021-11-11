from eth_photo.models import ImageModel
from eth_photo.models import eth_account
from .eth_connect import *
import logging
import struct,socket
import time

# UploadedImageModel matching query does not exist.	

class search_person(object):
	"""docstring for search_person"""
	def __init__(self, id_in, address):
		super(search_person, self).__init__()
		self.id_in = id_in
		self.address = address
		# get address and password from the database
	
	def solve(self):
		account_using = None
		try:
			account_using = eth_account.objects.get(address = self.address)
			print("accout_using-----------",account_using)
		except Exception as e:
			logging.debug ("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee",e)
		if not account_using:
			logging.debug ("ERROR: can't find the address of eth in database")
			return None
		t = eth_connect(account_using.address, account_using.password)
		result = t.get_picInfo (self.id_in)
		if not result:
			logging.debug("WARNING: EMPTY")
			return []
		result_len = result[6]
		logging.debug(result_len)
		ret_dic = []
		for i in range(result_len):
			temp = {}
			temp['file_date'] = time.asctime( time.localtime(result[3][i]))
			temp['file_name'] = result[0][i] + "_" + str(result[3][i])
			temp['own_name'] = result[1][i]
			if result[2][i] == 0:
				temp['file_type'] = "X光图"
			elif result[2][i] == 1:
				temp['file_type'] = "CT图"
			else:
				temp['file_type'] = "普通图片"
			temp['file_loc'] =  socket.inet_ntoa(struct.pack('I',socket.htonl(int(result[4][i]))))
			ret_dic.append(temp)
			ImageModel.objects.get_or_create(own_name = result[1][i], pic_hash = result[0][i], pic_type = result[2][i], timestamp = result[3][i], saved_pos = result[4][i], id_card = result[5][i])

		# logging.debug("AAAAAAA")
		# logging.debug(ret_dic)
		return ret_dic

