import os
import glob
import pandas as pd
import json
import numpy as np
import xml.etree.cElementTree as ET
from xml_to_csv import boundingbox


def create_bounding_box(svg_object):
    svg_array = json.loads(svg_object)
    b_boxes = []
    for svg in svg_array:
        points_array = np.array(svg['points'])  # svg_points_list convert to 2d array with numpy
        b_box = boundingbox.BoundingBox(points_array)
        b_boxes.append(b_box)

    return b_boxes

def xml_to_csv(path):
    xml_list = []
    for xml_file in glob.glob(path + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        svg = root.find('mark')[1].text
        bounding_boxes = create_bounding_box(svg)
        for b_box in bounding_boxes:
            value = (root.find('number').text,
                     root.find('age').text,
                     root.find('sex').text,
                     root.find('composition').text,
                     root.find('echogenicity').text,
                     root.find('margins').text,
                     root.find('calcifications').text,
                     root.find('tirads').text,
                     root.find('reportbacaf').text,
                     root.find('reporteco').text,
                     root.find('mark')[0].text,
                     b_box.minx,
                     b_box.miny,
                     b_box.maxx,
                     b_box.maxy
                     )
            xml_list.append(value)

    colum_names = ['number', 'age', 'sex', 'composition', 'echogenicity', 'margins', 'calcifications', 'tirads',
                   'reportbacaf', 'reporteco', 'image', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns=colum_names)
    return xml_df


def xml_to_json(path):
    json_list = []  # string list
    for xml_file in glob.glob(path + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        # svg = root.find('mark')[1].text
        images = root.findall('mark')
        bounding_boxes = create_bounding_box(images)
        case = {
            'case_id': root.find('number').text,
            'age': root.find('age').text,
            'sex': root.find('sex').text,
            'composition': root.find('composition').text,
            'echogenicity': root.find('echogenicity').text,
            'margins': root.find('margins').text,
            'calcifications': root.find('calcifications').text,
            'tirads': root.find('tirads').text,
            'reportbacaf': root.find('reportbacaf').text,
            'reporteco': root.find('reporteco').text,
            'image': root.find('mark')[0].text,
            'bbox': json.dumps(bounding_boxes),
        }
        json_string = json.dumps(case, indent=12)
        json_list.append(json_string + ',')

    create_json(json_list)


def create_json(json_list):
    final_json = ' { "cases": [ '
    for i in json_list:
        final_json += i

    final_json = final_json[:-1]
    final_json = final_json + "] }"
    save_json(final_json)


def save_json(final_json):
    text_file = open("/Users/klaudiaszucs/thesis_work/tfrecord_converter/files/json_files/test.json", "w")
    text_file.write(final_json)
    text_file.close()


def create_csv(name):
    file_path = 'files/' + name
    train_image_path = os.path.join(os.getcwd(), file_path)
    xml_df = xml_to_csv(train_image_path)

    csv_name = 'thyroid_nodule_' + name + '.csv'
    xml_df.to_csv(csv_name, index=None)
    print(name + ' images:Successfully converted xml to ' + csv_name)


def main():
    # create_csv("train")
    # create_csv("test")
    # create_csv("validation")
    file_path = 'files/' + 'test'
    xml_to_json(file_path)


main()
