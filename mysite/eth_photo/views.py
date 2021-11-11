from django.http import JsonResponse

from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.http.request import QueryDict
from django.contrib.auth import login
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from eth_photo.models import UploadedImageModel
from eth_photo.models import eth_account
from eth_photo.save_to_blockchain import save_to_blockchain
# Create your views here.

import  web3
from .forms import UploadedImageForm
#from .models import UploadedImageModel
import hashlib
import socket
import time
import datetime
import struct
from eth_photo.search_person import search_person
import json
import filetype
import os
import zlib
import requests
import random
import base64
from eth_photo.Operate_list import Operate_list

import logging

w3 = web3.Web3(web3.HTTPProvider('HTTP://127.0.0.1:7545'))
accounts = w3.eth.accounts
print("view.py---accounts---",accounts)

def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip

def index (request):
    return render (request,'home.html')

def test_login (request):
    return render (request,'login.html')

def img_request (request):
    if request.method=='POST':
        img_name = request.POST.get('img_name')
        print("img_name---------------", img_name)
        img_ip = request.POST.get('file_loc')
        #img_ip = "192.168.1.114"
        logging.debug('\n'+img_name)
        print("img-ip-------------------------", img_ip)
        file_name = str(random.random() * 65536)
        temp_file = open("tmp/" + file_name,'wb+')
        
        not_a_image = 0
        session_address = request.session.get('address', default = "")
        try:
            post_response = requests.post('http://'+img_ip+':25252/media/photos/'+img_name, timeout=3)
            file_data = post_response.content
            #logging.debug()

            file_content = zlib.decompress(file_data)
            print(" file_content----------------------  ", file_content)
            file_hash = hashlib.md5(file_content).hexdigest()
        except Exception as e:
            not_a_image = 1
            print(e)
        img_hash = img_name.split('_')[0]
        img_timestamp = img_name.split('_')[1]
        timestamp = int(time.time())
        #or file_hash != img_name.split('_')[0]
        if not_a_image :
            temp_file.close()
            os.remove("tmp/" + file_name)
            temp_file = open ("tmp/X-ray.jpeg","rb")
            b64_img = str(base64.b64encode(temp_file.read()),encoding='utf-8')
            temp_file.close()
            resp = "data:image/jpeg;base64,"+b64_img
            response_data = {"url":str(resp)}
            return JsonResponse(response_data)

        temp_file.write(file_content)
        temp_file.close()

        answer = filetype.guess("tmp/" + file_name)
        logging.debug(answer)
        os.remove("tmp/" + file_name)
        record_object = Operate_list (session_address)
        record_object.set (pic_hash=img_hash,pic_timestamp=img_timestamp,operater_name=session_address,operate_type=1,operater_time=timestamp)


        file_type = answer.mime
        if file_type == None:
            file_type = "image/png"
        base64_img = str(base64.b64encode(file_content),encoding='utf-8')
        resp = "data:" + str(file_type) + ";base64," + base64_img
        response_data = {"url":str(resp)}

        return JsonResponse(response_data)

    return HttpResponse (status=503)

def search (request):
    if request.method=='POST':
        search_id = request.POST.get('search_id')
        save_data = request.POST.get('save_data')
        logging.debug('\nsearch_id:'+search_id+'\nsave_data:'+save_data)
        print('\nsearch_id:'+search_id+'\nsave_data:'+save_data)
        search_object = search_person(search_id, save_data)
        retu_dic = search_object.solve()
        print("retu_dic-------------------", retu_dic)
        # return_str = retu_dic
        # if len(retu_dic) == 0 :
        #     return HttpResponse ("hello", status = 404)
        #
        # age = datetime.datetime.now().year - int(search_id[6:10])
        # logging.debug(int(search_id[6:9]))
        # if int(search_id[-2]) % 2 == 0:
        #     sex = '女'
        # else:
        #     sex = '男'
        #
        # logging.debug(retu_dic)
        # response_data = {'name':retu_dic[0]['own_name'],'age':age,'sex':sex,'img_list':retu_dic}
        response_data = {'name':retu_dic[0]['own_name'],'age':"25",'sex':"男",'img_list':retu_dic}
        return JsonResponse (response_data)

    return HttpResponse (status=503)

def app_login (request):
    print("inininininin------------------")
    print(request, request.method)
    if request.method=='POST':
        # post = QueryDict(request.get_full_path().split('?')[1])
        # print("ssssssssssssssssssssssssssssssssssssssss",post)
        # username = post.get('username')
        # old_password =post.get('password')
        username = request.POST['username']
        old_password =request.POST['password']
        # username = "1234"
        # old_password = 'owl12345'
        user = authenticate(username=username, password=old_password)
        if user is not None:
            if user.is_active:
                # address = eth_account.objects.all()[:1]
                # request.session['address'] = str(address[0])
                request.session['address'] = str(accounts[0])
                success_data={'jiaobaba':'nothing is true','save_data': str(accounts[0])}
                return JsonResponse(success_data)
        else:
            return HttpResponse('<h1>hello</h1>',status=403)
    return HttpResponse (status=503)





@login_required(login_url='/home')
def myview(request):
    return render_to_response('index.html')

 
@login_required(login_url='/home')
def UploadedImageView(request):
    if request.method == "POST":
        form = UploadedImageForm(request.POST, request.FILES)
        logging.debug(form)
        if form.is_valid():
            image = request.FILES.get('image')
            image_data = image.read()

            pic_hash = hashlib.md5(image_data).hexdigest()
            pic_type = form.cleaned_data['pic_type']
            own_name = form.cleaned_data['own_name']
            saved_pos = get_host_ip()
            saved_pos = str(socket.ntohl(struct.unpack("I",socket.inet_aton(str(saved_pos)))[0]))
            id_card = form.cleaned_data['id_card']
            timestamp = int(time.time())

            #logging.debug(os.getcwd())
            #image._set_name(pic_hash+'_'+str(timestamp))
            temp_file = open("media/photos/" + pic_hash+'_'+str(timestamp),"wb+")
            temp_file.write(zlib.compress(image_data, zlib.Z_BEST_COMPRESSION))
            temp_file.close()

            session_address = request.session.get('address', default = "")
            search_id = request.POST.get('search_id')
            # logging.debug("AAAAAAAAAAAAAAAAAAAAAAAAAAAA"+pic_hash)
            # logging.debug(type(pic_hash))
            #search_object = save_to_blockchain(search_id, session_address)
            print("own_name-----  "+own_name)
            print("pic_type-----  "+ str(pic_type))
            #result = search_object.save (own_name=str(own_name),pic_hash=str(pic_hash),pic_type= pic_type,saved_pos=int(saved_pos),id_card=str(id_card),timestamp=int(timestamp))
            record_object = Operate_list (session_address)
            record_object.set (pic_hash=pic_hash,pic_timestamp=timestamp,operater_name=session_address,operate_type=0,operater_time=timestamp)

            #logging.debug(result)

            UploadedImageModel.objects.create(own_name=own_name,pic_hash=pic_hash,pic_type=pic_type,saved_pos=saved_pos,id_card=id_card,timestamp=timestamp)

            upload_success = "上传成功！！"
            return render(request, 'image_solve.html',{'upload_success':upload_success})

    else:
        form = UploadedImageForm()
    
    #logging.debug(form)
    upload_success=""
    return render(request, 'image_solve.html',{'form':form})
 
@login_required(login_url='/home')
def success(request):
    return render(request, 'polls/success.html')

def home(request):
    return render(request,'login1.html')

@csrf_exempt
def get_pass(request):
    
    username =request.POST['logname']
    old_password =request.POST['logpass']
    user = authenticate(username=username, password=old_password)
    if user is not None:
        if user.is_active:
            login(request, user)
            print("#####################################################################in")
            #address = eth_account.objects.all()[:1]
            #logging.debug("AAAAAAAAAAAAAAAAAAAAAAAAAAAA"+" "+str(type(address))+" "+str(address))
            eth_account.objects.get_or_create(id="123",address=str(accounts[0]),password="password")
            request.session['address'] = str(accounts[0])
            return HttpResponseRedirect('/webLogin/upload/')
    else:
        return HttpResponse("wrong pass")

@login_required(login_url='/home')
def webSearch (request):
    if request.method=='POST':
        search_id = request.POST.get('search_id')
        session_address = request.session.get('address', default = "")
        logging.debug("AA"+str(search_id))
        search_object = search_person(search_id, session_address)
        retu_dic = search_object.solve()
        # return_str = retu_dic
        return_str = json.dumps(retu_dic)
        return HttpResponse (return_str, status = 200)
    return HttpResponse (status=503)


@login_required(login_url='/home')
def Search_recoder (request):
    if request.method == 'POST':
        page_type = request.POST.get('page_type')
        session_address = request.session.get('address', default = "")
        print("senssion_address+++++++++++++++++++++++++++++",session_address)
        if page_type.isdigit():
            record_object = Operate_list (session_address)

            if (int(page_type) == 0):
                retlist = record_object.get()
                retlist = json.dumps(retlist)
                return HttpResponse (retlist, status = 200)
            else:
                page = int(page_type)
                retlist = record_object.get_page(page_type)
                retlist = json.dumps(retlist)
                return HttpResponse (retlist,status = 200)
        else:
            return HttpResponse (status=404)

#data_time
#data_type
#data_account
#data_picname


# Create your views here.

