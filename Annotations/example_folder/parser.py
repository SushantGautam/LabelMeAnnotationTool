import xmltodict
import pprint
import json
import cv2
import os

with open('img1.xml') as fd:
    doc = xmltodict.parse(fd.read())

# pp = pprint.PrettyPrinter(indent=4)
data= json.dumps(doc)
# pp.pprint(json.dumps(doc))
# print(data)

resp = json.loads(data)
# len(resp['annotation']['object'])

img = cv2.imread("img1.jpg")
for i in range(5):
    x_list = []
    y_list = []
    boundary_label = (resp['annotation']['object'][i]['name'])
    print(boundary_label)

    for j in (resp['annotation']['object'][i]['polygon']['pt']):
        x_list.append(j['x'])
        y_list.append(j['y'])

    temp=[min(x_list,key=float), min(y_list,key=float), max(x_list,key=float), max(y_list,key=float)]
    print(temp[0],temp[1] ,'\t',temp[2],temp[3])
    crop_img = img[int(temp[1]):int(temp[3]), int(temp[0]):int(temp[2])]
    
    path = "base_dir/"+boundary_label+"/"
   
    try:  
        os.makedirs(path)
    except OSError:
        print(OSError)
        print ("Creation of the directory %s failed" % path)
    else:
        print ("Successfully created the directory %s " % path)
    cv2.imwrite(path+str(boundary_label)+".png",crop_img)
