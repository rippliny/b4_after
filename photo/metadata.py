# from PIL import Image
# from PIL.ExifTags import TAGS

# def get_photo_info(img_name) :
#         image_path = "media\\" + str(img_name)
#         image = Image.open(image_path) #이미지 파일 경로 또는 주소 입력
#         info = image._getexif()
#         image.close()

#         taglabel = {}

#         if info == None:
#             return "데이터 정보가 없습니다!"
#         else:
#             for tag, value in info.items():
#                 decoded = TAGS.get(tag, tag)
#                 taglabel[decoded] = value

#         # print(taglabel['DateTimeOriginal'])  # 촬영 시각
#         # print(taglabel['Make'], taglabel['Model'])  # 카메라 기종

#         # 촬영 위치
#         exifGPS = taglabel['GPSInfo']
#         latData = exifGPS[2]  # 위도(latitude)만 불러오기
#         lonData = exifGPS[4]  # 경도(longitude)만 불러오기

#         # 도(Degree), 분(Minute), 초(Second) 계산
#         latDeg = latData[0]
#         latMin = latData[1]
#         latSec = latData[2]

#         lonDeg = lonData[0]
#         lonMin = lonData[1]
#         lonSec = lonData[2]

#         # 도, 분, 초로 나타내기
#         Lat = str(int(latDeg)) + "°" + str(int(latMin)) + "'" + str(latSec) + "\"" + exifGPS[1]
#         Lon = str(int(lonDeg)) + "°" + str(int(lonMin)) + "'" + str(lonSec) + "\"" + exifGPS[3]

#         print(Lat, Lon)

#         # 도 decimal로 나타내기
#         # 위도 계산
#         Lat = (latDeg + (latMin + latSec / 60.0) / 60.0)
#         # 북위, 남위인지를 판단, 남위일 경우 -로 변경
#         if exifGPS[1] == 'S': Lat = Lat * -1

#         # 경도 계산
#         Lon = (lonDeg + (lonMin + lonSec / 60.0) / 60.0)
#         # 동경, 서경인지를 판단, 서경일 경우 -로 변경
#         if exifGPS[3] == 'W': Lon = Lon * -1
        
#         DateTime = taglabel['DateTimeOriginal']
#         ExifImageHeight = taglabel['ExifImageHeight']
#         ExifImageWidth = taglabel['ExifImageWidth']
#         ShutterSpeedValue = taglabel['ShutterSpeedValue']
#         FNumber = taglabel['FNumber']
#         Make = taglabel['Make']
#         Model = taglabel['Model']
#         LensModel = taglabel['LensModel']

#         context = {
#             'DateTime': DateTime,
#             'ExifImageHeight': ExifImageHeight,
#             'ExifImageWidth': ExifImageWidth,
#             'ShutterSpeedValue': ShutterSpeedValue,
#             'FNumber': FNumber,
#             'Make': Make,
#             'Model': Model,
#             'LensModel': LensModel,
#             'Lat' : Lat,
#             'Lon' : Lon,
#         }

#         # return render(request, img_info.html, context)
#         return context