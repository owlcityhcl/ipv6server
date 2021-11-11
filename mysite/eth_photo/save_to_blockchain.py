from eth_photo.models import ImageModel
from eth_photo.models import eth_account
from .eth_connect import *
import logging
import struct,socket

# UploadedImageModel matching query does not exist.	

class save_to_blockchain(object):
	"""docstring for search_person"""
	def __init__(self, id_in, address):
		super(save_to_blockchain, self).__init__()
		self.id_in = id_in
		self.address = address
		# get address and password from the database
	
	def save(self,pic_hash, own_name ,pic_type , timestamp, saved_pos , id_card):
		account_using = None
		try:
			account_using = eth_account.objects.get(address = self.address)
		except Exception as e:
			logging.debug (e)
		if not account_using:
			logging.debug ("ERROR: can't find the address of eth in database")
			return None
		t = eth_connect(account_using.address, account_using.password)
		logging.debug(type(pic_hash))
		result = t.savePic_to_blockchain(pic_hash, own_name ,pic_type , timestamp, saved_pos , id_card)

		return result

