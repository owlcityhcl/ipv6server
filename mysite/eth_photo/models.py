from django.db import models
import time

# Create your models here.


class medical_users (models.Model):
    username = models.CharField (max_length=100,blank=False,unique=True)
    block = models.BooleanField(default=False)
    passhash = models.CharField(max_length=260,blank=False)
    def __str__ (self):
        return self.username



class UploadedImageModel(models.Model):
    PIC_TYPE = (
        (0, 'X光图'),
        (1, 'CT图'),
        (2,'普通图片'), 
    )

    own_name = models.CharField ( 'own_name',max_length=30,null=False )
    pic_hash = models.CharField('pic_hash', max_length=32,null=False)
    pic_type = models.IntegerField ('pic_type', default=0,choices=PIC_TYPE)   
    timestamp = models.BigIntegerField('timestamp',null=False)
    saved_pos = models.CharField('saved_pos', max_length=50, blank=False)
    id_card = models.CharField ( 'id_card',max_length=40,null=False )
    #image = models.ImageField('photos', upload_to='photos', blank=False,null=False)
    status = models.IntegerField('status', default=0, choices=PIC_TYPE) # 0进行中,1已完成
    
 
    class Meta:
         db_table = "uploadedimage"
 
    def __str__(self):
         return self.pic_hash

class eth_account(models.Model):
    """docstring for eth_account"""
    address = models.CharField(max_length=80,unique=True)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.address

class ImageModel(models.Model):
    PIC_TYPE = (
        (0, 'X光图'),
        (1, 'CT图'),
        (2,'普通图片'), 
    )
    """docstring for ImageModel"""
    own_name = models.CharField ( 'own_name',max_length=30,null=False )
    pic_hash = models.CharField('pic_hash', max_length=32,null=False)
    pic_type = models.IntegerField ('pic_type', default=0,choices=PIC_TYPE)   
    timestamp = models.BigIntegerField('timestamp',null=False)
    saved_pos = models.CharField('saved_pos', max_length=50, blank=False)
    id_card = models.CharField ( 'id_card',max_length=40,null=False )

class operate_recoder(models.Model):
    pic_hash = models.CharField(max_length=32,null=False)
    pic_timestamp = models.BigIntegerField(null=False)
    operater_name = models.CharField(max_length=80,null=False)
    operate_type = models.IntegerField(null=False)
    operater_time = models.BigIntegerField(null=False)



