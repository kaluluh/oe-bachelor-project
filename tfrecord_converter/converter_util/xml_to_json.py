import glob
import json
import os
import xml.etree.cElementTree as ET
from converter_util.bbox_util import create_bounding_box

FILE_PATH = "/Users/klaudiaszucs/thesis_work/tfrecord_converter/files/test"
JSON_FILE = "/Users/klaudiaszucs/thesis_work/tfrecord_converter/files/json_files/test.json"


# [ymin, xmin, ymax, xmax]
def xml_to_json(path):
    temp_cases = []  # dictionary case object list
    xml_files = glob.glob(path + '/*.xml', recursive=True)
    for xml_file in xml_files:
        temp = xml_file.split('/')
        file_name = temp[len(temp) - 1][:-4]
        print(file_name)
        tree = ET.parse(xml_file)
        root = tree.getroot()
        images = root.findall('mark')

        for image in images:
            number = image.find('image').text
            image_id = file_name + '_' + number

            temp_bboxes = image.find('svg').text
            bounding_boxes = create_bounding_box(temp_bboxes)
            xmin = []
            xmax = []
            ymin = []
            ymax = []
            if bounding_boxes is not None:
                for bbox in bounding_boxes:
                    xmin.append(bbox['minx'])
                    xmax.append(bbox['maxx'])
                    ymin.append(bbox['miny'])
                    ymax.append(bbox['maxy'])

            case = {
                'case_id': image_id,
                'age': root.find('age').text,
                'sex': root.find('sex').text,
                'composition': root.find('composition').text,
                'echogenicity': root.find('echogenicity').text,
                'margins': root.find('margins').text,
                'calcifications': root.find('calcifications').text,
                'tirads': root.find('tirads').text,
                'reportbacaf': root.find('reportbacaf').text,
                'reporteco': root.find('reporteco').text,
                # 'image': root.find('mark')[0].text,
                # 'bbox': bounding_boxes,
                'xmin': xmin,
                'xmax': xmax,
                'ymin': ymin,
                'ymax': ymax,
            }
            temp_cases.append(case)

    cases = {
        'cases': temp_cases
    }
    save_json(json.dumps(cases))


def save_json(final_json):
    text_file = open(JSON_FILE, "w")
    text_file.write(final_json)
    text_file.close()


def main():
    xml_to_json(FILE_PATH)

main()
