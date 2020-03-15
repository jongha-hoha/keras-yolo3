import cv2
object_map = dict()

filename = "/home/willook/data/coco/annotations/instances_val2017.json"
datapath = "/home/willook/data/coco/val2017/"
outputfilename = "/home/willook/data/coco/annotations/instances_val2017.txt"

def print_with_json(filename):
    import json
    with open(filename) as json_file:
        json_data = json.load(json_file)
        for json_key in json_data.keys():
            #if "bbox" not in json_data[key]:
            #    continue
            inner_data = json_data[json_key]
            if isinstance(inner_data,dict):
                print_dict(inner_data)
            else :
                print_list(inner_data)    

def print_dict(dict_data):
    if "bbox" not in dict_data.keys():
        return
    #print("image_id", dict_data["image_id"])
    #print("category_id", dict_data["category_id"])
    #print("bbox", dict_data["bbox"])
    #outfile.write(str_id+",".join(dict_data["bbox"])+","+dict_data["category_id"])
    #show_bbox(dict_data["image_id"], dict_data["bbox"])
    key, value = data2str(dict_data["image_id"], dict_data["bbox"], dict_data["category_id"])
    if key in object_map:
        object_map[key].append(value)
    else:
        object_map[key] = [value]

    #input("> next?")

def data2str(image_id,bbox,category_id):
    str_id = id2name(image_id)
    x1 = int(bbox[0])
    y1 = int(bbox[1])
    x2 = int(bbox[0] + bbox[2])
    y2 = int(bbox[1] + bbox[3])
    line = "{},{},{},{},{}".format(x1, y1, x2, y2,category_id)
    return str_id, line
    
def id2name(image_id):
    return datapath+str(image_id).zfill(12)+".jpg"
    
def print_list(list_data):
    for dict_data in list_data:
        print_dict(dict_data)

def show_bbox(image_id, bbox):
    str_id = id2name(image_id)
    img = cv2.imread(str_id)
    x1 = int(bbox[0])
    y1 = int(bbox[1])
    x2 = int(bbox[0] + bbox[2])
    y2 = int(bbox[1] + bbox[3])
    
    img = cv2.line(img, (x1,y1), (x1,y2), (255,0,0))
    img = cv2.line(img, (x1,y1), (x2,y1), (255,0,0))
    img = cv2.line(img, (x2,y2), (x1,y2), (255,0,0))
    img = cv2.line(img, (x2,y2), (x2,y1), (255,0,0))
    #print(">name", str_id)
    #print(">size", img.shape)
    #print(">bbox", x1,y1,x2,y2)
    
    cv2.imshow(str_id, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
if __name__ == '__main__':
    #filename = "captions_train2017.json"
    #filename = "/home/willook/data/coco/annotations/instances_train2017.json"
    #filename = "/home/willook/data/coco/annotations/instances_val2017.json"
    #filename = "person_keypoints_train2017.json"
    print_with_json(filename)
    #outputfilename = filename.replace("json","txt")
    outputfile = open(outputfilename, "w")
    for key in object_map.keys():
        line = key+" "+" ".join(object_map[key])+"\n"
        outputfile.write(line)
        
    print("done.")
