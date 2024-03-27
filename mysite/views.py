import hashlib
import os
import datetime
import uuid
import requests
import cv2
from django.conf import settings
import dlib
import time
import pandas as pd
import numpy as np
from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from .models import *
from .serializers import *
import json
@csrf_exempt
def login(request):
   if request.method == 'POST':
      data = json.loads(request.body)
      studentID = data.get('studentID')
      password = data.get('password')
      try:
         user = user_table.objects.get(studentID=studentID)
         if user.password == password:
            return JsonResponse({'status': 'success', 'message': '登录成功', 'user': {'studentID': user.studentID}})
         else:
            return JsonResponse({'status': 'error', 'message': '密码错误'})
      except user_table.DoesNotExist:
         return JsonResponse({'status': 'error', 'message': '用户名不存在'})
      else:
         return JsonResponse({'status': 'error', 'message': '请求方法错误'})
    #user=User.objects.all()
    #serializers=UserlistSerializers(user,many=True)
    #return JsonResponse(serializers.data,safe=False)
@csrf_exempt
def register(request):
   if request.method == 'POST':
      data = json.loads(request.body)
      studentID = data.get('studentID')
      password = data.get('password')
      sname = data.get('sname')
      sex = data.get('sex')
      authors = user_table.objects.filter(studentID=studentID)
      if (len(authors) > 0):
         return JsonResponse({'status': 'error','message': '用户名已存在'})
      else:
         user = user_table(studentID=studentID, sname=sname, sex=sex, password=password)
         user.save()
         return JsonResponse({'status': 'success','message': '注册成功'})
@csrf_exempt
def home(request):
   if request.method == 'POST':
      data = json.loads(request.body)
      studentID = data.get('studentID')
      home=user_table.objects.filter(studentID=studentID)
      table=UserSerializers(home,many=True)
      return JsonResponse(table.data, safe=False)
@csrf_exempt
def dormitory_information(request):
   if request.method == 'POST':
      data = json.loads(request.body)
      studentID=data.get('studentID')
      table = dormitory_table.objects.filter(studentID=studentID)
      table1=DormitorySerializers(table,many=True)
      print(table1)
      return JsonResponse(table1.data,safe=False)
@csrf_exempt
def dormitory2(request):
   if request.method == 'POST':
      data = json.loads(request.body)
      studentID = data.get('studentID')
      area = dormitory_table.objects.filter(studentID=studentID).values('area')
      build = dormitory_table.objects.filter(studentID=studentID).values('build')
      floor = dormitory_table.objects.filter(studentID=studentID).values('floor')
      number = dormitory_table.objects.filter(studentID=studentID).values('number')
      residency = dormitory_form.objects.filter(
         Q(area__contains=area) & Q(build__contains=build) & Q(floor__contains=floor) & Q(
            number__contains=number)).order_by()
      table2 = Dormitory_from_Serializers(residency, many=True)
      print(table2)
      return JsonResponse(table2.data,safe=False)
@csrf_exempt
def dormitory3(request):
   if request.method == 'POST':
      data = json.loads(request.body)
      studentID = data.get('studentID')
      area = dormitory_table.objects.filter(studentID=studentID).values('area')
      build = dormitory_table.objects.filter(studentID=studentID).values('build')
      floor = dormitory_table.objects.filter(studentID=studentID).values('floor')
      number = dormitory_table.objects.filter(studentID=studentID).values('number')
      student = dormitory_table.objects.filter(Q(area__contains=area) & Q(build__contains=build)&Q(floor__contains=floor)&Q(number__contains=number)).order_by('studentID')
      table3 = DormitorySerializers(student, many=True)
      print(table3)
      return JsonResponse(table3.data,safe=False)
@csrf_exempt
def water_rate(request):
   if request.method == 'POST':
      data = json.loads(request.body)
      studentID = data.get('studentID')
      table = dormitory_table.objects.filter(studentID=studentID)
      table1 = DormitorySerializers(table, many=True)
      return JsonResponse(table1.data,safe=False)
@csrf_exempt
def water_rate2(request):
   if request.method == 'POST':
      data = json.loads(request.body)
      studentID = data.get('studentID')
      area = dormitory_table.objects.filter(studentID=studentID).values('area')
      build = dormitory_table.objects.filter(studentID=studentID).values('build')
      floor = dormitory_table.objects.filter(studentID=studentID).values('floor')
      number = dormitory_table.objects.filter(studentID=studentID).values('number')
      water = water_table.objects.filter(
         Q(area__contains=area) & Q(build__contains=build) & Q(floor__contains=floor) & Q(
            number__contains=number) & Q(status__contains='未缴费')).order_by()
      table2 = WaterSerializers(water, many=True)
      return JsonResponse(table2.data,safe=False)
@csrf_exempt
def water_rate3(request):
   if request.method == 'POST':
      data = json.loads(request.body)
      studentID = data.get('studentID')
      area = dormitory_table.objects.filter(studentID=studentID).values('area')
      build = dormitory_table.objects.filter(studentID=studentID).values('build')
      floor = dormitory_table.objects.filter(studentID=studentID).values('floor')
      number = dormitory_table.objects.filter(studentID=studentID).values('number')
      water2 = water_table.objects.filter(
         Q(area__contains=area) & Q(build__contains=build) & Q(floor__contains=floor) & Q(
            number__contains=number)).order_by('-time')
      table3 = WaterSerializers(water2, many=True)
      return JsonResponse(table3.data,safe=False)
@csrf_exempt
def electric_rate(request):
   if request.method == 'POST':
      data = json.loads(request.body)
      studentID = data.get('studentID')
      table = dormitory_table.objects.filter(studentID=studentID)
      table1 = DormitorySerializers(table, many=True)
      return JsonResponse(table1.data,safe=False)
@csrf_exempt
def electric_rate2(request):
   if request.method == 'POST':
      data = json.loads(request.body)
      studentID = data.get('studentID')
      area = dormitory_table.objects.filter(studentID=studentID).values('area')
      build = dormitory_table.objects.filter(studentID=studentID).values('build')
      floor = dormitory_table.objects.filter(studentID=studentID).values('floor')
      number = dormitory_table.objects.filter(studentID=studentID).values('number')
      electric = electric_table.objects.filter(
         Q(area__contains=area) & Q(build__contains=build) & Q(floor__contains=floor) & Q(
            number__contains=number) & Q(status__contains='未缴费')).order_by()
      table2 = ElectricSerializers(electric, many=True)
      return JsonResponse(table2.data,safe=False)
@csrf_exempt
def electric_rate3(request):
   if request.method == 'POST':
      data = json.loads(request.body)
      studentID = data.get('studentID')
      area = dormitory_table.objects.filter(studentID=studentID).values('area')
      build = dormitory_table.objects.filter(studentID=studentID).values('build')
      floor = dormitory_table.objects.filter(studentID=studentID).values('floor')
      number = dormitory_table.objects.filter(studentID=studentID).values('number')
      electric2 = electric_table.objects.filter(
         Q(area__contains=area) & Q(build__contains=build) & Q(floor__contains=floor) & Q(
            number__contains=number)).order_by('-time')
      table3 = ElectricSerializers(electric2, many=True)
      return JsonResponse(table3.data,safe=False)

@csrf_exempt
def repair(request):
   if request.method == "POST":
      data = json.loads(request.body)
      studentID = data.get('studentID')
      area = dormitory_table.objects.filter(studentID=studentID).values('area')
      build = dormitory_table.objects.filter(studentID=studentID).values('build')
      floor = dormitory_table.objects.filter(studentID=studentID).values('floor')
      number = dormitory_table.objects.filter(studentID=studentID).values('number')
      repair = Repair_report_table.objects.filter(
         Q(area__contains=area) & Q(build__contains=build) & Q(floor__contains=floor) & Q(
            number__contains=number)).order_by('title')
      title = RepairSerializers(repair, many=True)
      return JsonResponse(title.data, safe=False)
@csrf_exempt
def repair2(request):
   if request.method == "POST":
      data = json.loads(request.body)
      title=data.get('title')
      area = data.get('area')
      build=data.get('build')
      floor=data.get('floor')
      number=data.get('number')
      repair_content=data.get('repair_content')
      keys = ['title', 'area', 'build','floor','number','repair_content']
      for key in keys:
         if key not in data or not data[key]:
            return JsonResponse({'message': f'{key} 不能为空'})
      # 处理数据并返回结果
      repair = Repair_report_table(area=area, build=build + '号楼', floor=floor + '楼', number=number + '号',
                                   title=title, content=repair_content)
      repair.save()
      return JsonResponse({'message': 'success'})
   return JsonResponse({'message': 'Invalid request method'})
@csrf_exempt
def tuition(request):
   if request.method == "POST":
      data = json.loads(request.body)
      studentID = data.get('studentID')
      t = tuition_table.objects.filter(Q(studentID__contains=studentID) & Q(tuition_status__contains='未缴费')).order_by()
      a = tuition_table.objects.filter(Q(studentID__contains=studentID) & Q(accommodation_status__contains='未缴费')).order_by()
      table =TuitionSerializers(t, many=True)
      return JsonResponse(table.data, safe=False)
@csrf_exempt
def tuition2(request):
   if request.method == "POST":
      data = json.loads(request.body)
      studentID = data.get('studentID')
      a = tuition_table.objects.filter(Q(studentID__contains=studentID) & Q(accommodation_status__contains='未缴费')).order_by()
      table =TuitionSerializers(a, many=True)
      return JsonResponse(table.data, safe=False)
@csrf_exempt
def personal(request):
   if request.method == 'POST':
      data = json.loads(request.body)
      studentID=data.get('studentID')
      table = user_table.objects.filter(studentID=studentID)
      table1=UserSerializers(table,many=True)
      print(table1)
      return JsonResponse(table1.data,safe=False)

@csrf_exempt
def personal2(request):
   if request.method == 'POST':
      data = json.loads(request.body)
      studentID=data.get('studentID')
      table = dormitory_table.objects.filter(studentID=studentID)
      table2=DormitorySerializers(table,many=True)
      print(table2)
      return JsonResponse(table2.data,safe=False)
@csrf_exempt
def change_face1(request):
   if request.method == 'POST':
      data = json.loads(request.body)
      studentID = data.get('studentID')
      user = user_table.objects.filter(studentID=studentID)
      table1 = UserSerializers(user, many=True)
      request.session['studentID']=studentID
      return JsonResponse(table1.data, safe=False)
@csrf_exempt
def change_face(request):
   if request.method == 'POST':
      file = request.FILES['image']
      fileName=request.session['studentID']
      # 保存文件
      data = fileName
      a = fileName + '.jpg'
      print(a)
      os.makedirs('D:/DjangoProject/djangoproject2/media/faceid/faces_from_camera/' + data, exist_ok=True)
      # 将要保存的地址和文件名称
      where = os.path.join('D:/DjangoProject/djangoproject2/media/faceid/faces_from_camera/' + data, a)
      # 分块保存image
      content = file.chunks()
      with open(where, 'wb') as f:
         for i in content:
            f.write(i)
      data1 = 'faceid/faces_from_camera/' + data + '/' + a
      studentID = request.session.get('studentID')
      user_table.objects.filter(studentID=studentID).update(face_image=data1)
      import cv2
      import dlib
      from skimage import io
      import csv
      # 要读取人脸图像文件的路径
      path_images_from_camera = "D:/DjangoProject/djangoproject2/media/faceid/faces_from_camera/"
      # Dlib 正向人脸检测器
      detector = dlib.get_frontal_face_detector()
      # Dlib 人脸预测器
      predictor = dlib.shape_predictor(
         "D:/DjangoProject/djangoproject2/media/faceid/model/shape_predictor_68_face_landmarks.dat")
      # Dlib 人脸识别模型
      # Face recognition model, the object maps human faces into 128D vectors
      face_rec = dlib.face_recognition_model_v1(
         "D:/DjangoProject/djangoproject2/media/faceid/model/dlib_face_recognition_resnet_model_v1.dat")

      # 返回单张图像的 128D 特征
      def return_128d_features(path_img):
         img_rd = io.imread(path_img)
         img_gray = cv2.cvtColor(img_rd, cv2.COLOR_BGR2RGB)
         # 提取人脸坐标
         faces = detector(img_gray, 1)
         # 因为有可能截下来的人脸再去检测，检测不出来人脸了
         # 所以要确保是 检测到人脸的人脸图像 拿去算特征
         if len(faces) != 0:
            # 提取人脸特征
            shape = predictor(img_gray, faces[0])
            # 通过特征点进行人脸识别
            face_descriptor = face_rec.compute_face_descriptor(img_gray, shape)
         else:
            face_descriptor = 0
         return face_descriptor

      # 将文件夹中照片特征提取出来, 写入 CSV
      def return_features_mean_person(path_faces_person):
         features_list_person = []
         photos_list = os.listdir(path_faces_person)
         if photos_list:
            for i in range(len(photos_list)):
               # 调用return_128d_features()得到128d特征
               features_128d = return_128d_features(path_faces_person + "/" + photos_list[i])
               # 遇到没有检测出人脸的图片跳过
               if features_128d == 0:
                  i += 1
               else:
                  # 把提取到的特征点加入列表
                  features_list_person.append(features_128d)
         else:
            print("文件夹内图像文件为空 / Warning: No images in " + path_faces_person + '/', '\n')
         print("有效人脸数量:", len(features_list_person))
         # 计算 128D 特征的均值
         if features_list_person:
            features_mean_person = np.array(features_list_person).mean(axis=0)
         else:
            features_mean_person = '0'
         return features_mean_person

      people = os.listdir(path_images_from_camera)
      people.sort()
      print("人名:", people)
      with open("D:/DjangoProject/djangoproject2/media/faceid/features_all.csv", "w", newline="") as csvfile:
         writer = csv.writer(csvfile)
         for person in people:
            print("正在计算" + person + "特征均值...")
            features_mean_person = return_features_mean_person(path_images_from_camera + person)
            writer.writerow(features_mean_person)
            print(person + "特征均值计算完毕")
            print("dlib特征均值 :", list(features_mean_person))
            print()
         print("所有录入人脸数据存入")
   studentID = request.session['studentID']
   user = user_table.objects.filter(studentID=studentID)
   table1 = UserSerializers(user, many=True)
   return JsonResponse(table1.data, safe=False)
@csrf_exempt
def record(request):
   data = json.loads(request.body)
   studentID = data.get('studentID')
   fac = faces_record.objects.filter(studentID=studentID).order_by('-time')
   table1 = RecordSerializers(fac, many=True)
   return JsonResponse(table1.data, safe=False)

@csrf_exempt
def getNewName(file_type):
   # 前面是file_type+年月日时分秒
   new_name = time.strftime('%Y%m%d%H%M%S', time.localtime())
   # 最后是5个随机数字
   # Python中的numpy库中的random.randint(a, b, n)表示随机生成n个大于等于a，小于b的整数
   ranlist = np.random.randint(0, 10, 5)
   for i in ranlist:
      new_name += str(i)
   # 加后缀名
   new_name += '.jpg'
   # 返回字符串
   return new_name
@csrf_exempt
def recognition(request):
   if request.method=='POST':
      # 人脸识别模型，提取128D的特征矢量
      # face recognition model, the object maps human faces into 128D vectors
      # Refer this tutorial: http://dlib.net/python/index.html#dlib.face_recognition_model_v1
      facerec = dlib.face_recognition_model_v1(
         "D:/DjangoProject/djangoproject2/media/faceid/model/dlib_face_recognition_resnet_model_v1.dat")

      # 计算两个128D向量间的欧式距离
      # compute the e-distance between two 128D features
      def return_euclidean_distance(feature_1, feature_2):
         feature_1 = np.array(feature_1)
         feature_2 = np.array(feature_2)
         dist = np.sqrt(np.sum(np.square(feature_1 - feature_2)))
         return dist

      # 处理存放所有人脸特征的 csv
      path_features_known_csv = "D:/DjangoProject/djangoproject2/media/faceid/features_all.csv"
      csv_rd = pd.read_csv(path_features_known_csv, header=None)

      # 用来存放所有录入人脸特征的数组
      # the array to save the features of faces in the database
      features_known_arr = []

      # 读取已知人脸数据
      # print known faces
      for i in range(csv_rd.shape[0]):
         features_someone_arr = []
         for j in range(0, len(csv_rd.iloc[i, :])):
            features_someone_arr.append(csv_rd.iloc[i, :][j])
         features_known_arr.append(features_someone_arr)
      print("Faces in Database：", len(features_known_arr))

      # Dlib 检测器和预测器
      # The detector and predictor will be used
      detector = dlib.get_frontal_face_detector()
      predictor = dlib.shape_predictor(
         'D:/DjangoProject/djangoproject2/media/faceid/model/shape_predictor_68_face_landmarks.dat')

      # 创建 cv2 摄像头对象
      url = ('rtsp://admin:1234@192.168.16.115:8554/live')
      cap = cv2.VideoCapture(url)

      # cap.set(propId, value)
      # 设置视频参数，propId 设置的视频参数，value 设置的参数值
      cap.set(3, 480)

      # cap.isOpened() 返回 true/false 检查初始化是否成功
      # when the camera is open
      while cap.isOpened():

         flag, img_rd = cap.read()
         kk = cv2.waitKey(1)

         # 取灰度
         img_gray = cv2.cvtColor(img_rd, cv2.COLOR_RGB2GRAY)
         # 人脸数 faces
         faces = detector(img_gray, 0)

         # 待会要写的字体 font to write later
         font = cv2.FONT_HERSHEY_COMPLEX

         # 存储当前摄像头中捕获到的所有人脸的坐标/名字
         # the list to save the positions and names of current faces captured
         pos_namelist = []
         name_namelist = []

         # 按下 ESC 键退出
         if kk == 27:
            break
         else:
            # 检测到人脸 when face detected
            if len(faces) != 0:
               # 获取当前捕获到的图像的所有人脸的特征，存储到 features_cap_arr
               # get the features captured and save into features_cap_arr
               features_cap_arr = []
               for i in range(len(faces)):
                  shape = predictor(img_rd, faces[i])
                  features_cap_arr.append(facerec.compute_face_descriptor(img_rd, shape))

               # 遍历捕获到的图像中所有的人脸
               # traversal all the faces in the database
               for k in range(len(faces)):
                  print("##### camera person", k + 1, "#####")
                  # 让人名跟随在矩形框的下方
                  # 确定人名的位置坐标
                  # 先默认所有人不认识，是 unknown
                  # set the default names of faces with "unknown"
                  name_namelist.append("unknown")

                  # 每个捕获人脸的名字坐标 the positions of faces captured
                  pos_namelist.append(
                     tuple([faces[k].left(), int(faces[k].bottom() + (faces[k].bottom() - faces[k].top()) / 4)]))

                  # 对于某张人脸，遍历所有存储的人脸特征
                  # for every faces detected, compare the faces in the database
                  e_distance_list = []
                  for i in range(len(features_known_arr)):
                     # 如果 person_X 数据不为空
                     if str(features_known_arr[i][0]) != '0.0':
                        print("with person", str(i + 1), "the e distance: ", end='')
                        e_distance_tmp = return_euclidean_distance(features_cap_arr[k], features_known_arr[i])
                        print(e_distance_tmp)
                        e_distance_list.append(e_distance_tmp)
                     else:
                        # 空数据 person_X
                        e_distance_list.append(999999999)
                  # 找出最接近的一个人脸数据是第几个
                  # Find the one with minimum e distance
                  similar_person_num = e_distance_list.index(min(e_distance_list))
                  print("Minimum e distance with person", int(similar_person_num) + 1)

                  # 计算人脸识别特征与数据集特征的欧氏距离
                  # 距离小于0.4则标出为可识别人物
                  if min(e_distance_list) < 0.4:
                     # 这里可以修改摄像头中标出的人名
                     # Here you can modify the names shown on the camera
                     # 1、遍历文件夹目录
                     folder_name = 'D:/DjangoProject/djangoproject2/media/faceid/faces_from_camera'
                     # 最接近的人脸
                     sum = similar_person_num + 1
                     key_id = 1  # 从第一个人脸数据文件夹进行对比
                     # 获取文件夹中的文件名:1wang、2zhou、3...
                     file_names = os.listdir(folder_name)
                     for name in file_names:
                        # print(name+'->'+str(key_id))
                        if sum == key_id:
                           # winsound.Beep(300,500)# 响铃：300频率，500持续时间
                           name_namelist[k] = name[0:]  # 人名删去第一个数字（用于视频输出标识）
                           studentID = request.session.get('studentID')
                           img1 = img_rd
                           name = getNewName('faces_record')
                           # 分块保存image
                           cv2.imwrite("D:/DjangoProject/djangoproject2/media/faceid/faces_record/" + name, img1)
                           # 上传文件名称到数据库
                           name1 = 'faceid/faces_record/' + name
                           time = datetime.datetime.now()
                           record1 = faces_record(studentID=studentID, time=time, record=name1)
                           record1.save()
                           # 释放摄像头 release camera
                           cap.release()
                           # 删除建立的窗口 delete all the windows
                           cv2.destroyAllWindows()
                        key_id += 1
                  else:
                     print("Unknown person")

                  # 矩形框
                  # draw rectangle
                  for kk, d in enumerate(faces):
                     # 绘制矩形框
                     cv2.rectangle(img_rd, tuple([d.left(), d.top()]), tuple([d.right(), d.bottom()]), (0, 255, 255),
                                   2)
                  print('\n')

               # 在人脸框下面写人脸名字
               # write names under rectangle
               for i in range(len(faces)):
                  cv2.putText(img_rd, name_namelist[i], pos_namelist[i], font, 0.8, (0, 255, 255), 1, cv2.LINE_AA)
         print("Faces in camera now:", name_namelist, "\n")
         # cv2.putText(img_rd, "Press 'q': Quit", (20, 450), font, 0.8, (84, 255, 159), 1, cv2.LINE_AA)
         cv2.putText(img_rd, "Face Recognition", (20, 40), font, 1, (0, 0, 255), 1, cv2.LINE_AA)
         cv2.putText(img_rd, "Visitors: " + str(len(faces)), (20, 100), font, 1, (0, 0, 255), 1, cv2.LINE_AA)
         # 窗口显示 show with opencv
         cv2.imshow("camera", img_rd)
         # 释放摄像头 release camera
      cap.release()
      # 删除建立的窗口 delete all the windows
      cv2.destroyAllWindows()
      return JsonResponse({"success":"识别成功"})

@csrf_exempt
def send_checkCode(requset):
   data = json.loads(requset.body)
   phone = data.get('phone')
   print(phone)
   url = 'https://api.netease.im/sms/sendcode.action'
   headers = {}
   headers['Content-Type'] = 'application/x-www-form-urlencoded;charset=utf-8'
   headers['AppKey'] = '7f297d157be4714dc504dca8606a2d8d'
   Nonce = str(uuid.uuid4()).replace('-', '')
   headers['Nonce'] = Nonce
   CurTime = str(int(time.time()))
   headers['CurTime'] = CurTime
   AppSecret = '95111da90110'
   CheckSum = hashlib.sha1((AppSecret + Nonce + CurTime).encode('utf-8')).hexdigest()
   headers['CheckSum'] = CheckSum
   response = requests.post(url=url, data={'mobile': phone}, headers=headers)
   json_result = response.json()
   if json_result.get('code') == 200:
      requset.session[phone] = json_result.get('obj')
      return JsonResponse({'msg': '短信发送成功！'})
   else:
      return JsonResponse({'msg': '短信发送失败！'})

@csrf_exempt
def modify_phone(request):
   if request.method == 'POST':
      data = json.loads(request.body)
      studentID = data.get('studentID')
      phone = data.get('phone')
      code = data.get('code')
      if request.session.get(phone) == code:
         user_table.objects.filter(studentID=studentID).update(phone=phone)
         return JsonResponse({'status': 'success','message': '手机号修改成功！'})
      else:
         return JsonResponse({'status': 'error','message': '验证码错误！'})
@csrf_exempt
def forget_password(request):
   if request.method == 'POST':
      data = json.loads(request.body)
      phone = data.get('phone')
      code = data.get('code')
      if request.session.get(phone) == code:
         return JsonResponse({'status': 'success','message': '验证成功！'})
      else:
         return JsonResponse({'status': 'error','message': '验证码错误！'})

@csrf_exempt
def modify_pwd(request):
   data = json.loads(request.body)
   pwd = data.get('pwd')
   studentID = data.get('studentID')
   user = user_table.objects.filter(studentID=studentID).first()
   user.password = pwd
   user.save()
   return JsonResponse({'message': '密码修改成功，请重新登录！'})
@csrf_exempt
def avatar1(request):
   if request.method == 'POST':
      data = json.loads(request.body)
      studentID = data.get('studentID')
      user = user_table.objects.filter(studentID=studentID)
      table1 = UserSerializers(user, many=True)
      request.session['studentID']=studentID
      return JsonResponse(table1.data, safe=False)
@csrf_exempt
def avatar(request):
   # 获取一个文件管理器对象
   studentID = request.session['studentID']
   file = request.FILES['image']
   # 保存文件
   new_name = getNewName('avatar')  # 具体实现在自己写的uploads.py下
   # 将要保存的地址和文件名称
   where = '%s/avatar/%s' % (settings.MEDIA_ROOT, new_name)
   # 分块保存image
   content = file.chunks()
   with open(where, 'wb') as f:
      for i in content:
         f.write(i)
   # 上传文件名称到数据库
   new_name1 = 'avatar/' + new_name
   user_table.objects.filter(studentID=studentID).update(avatar=new_name1)
   return JsonResponse({'message': '头像修改成功！'})