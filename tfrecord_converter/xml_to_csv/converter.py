import os
import glob
import pandas as pd
import json
import numpy as np
import xml.etree.cElementTree as ET
from xml_to_csv import boundingbox


def create_bounding_box(svg_object):
    if svg_object is not None:
        svg_array = json.loads(svg_object)
        b_boxes = []
        for svg in svg_array:
            points_array = np.array(svg['points'])  # svg_points_list convert to 2d array with numpy
            b_box = boundingbox.BoundingBox(points_array)
            b_boxes.append(b_box)

        final_bbox = []
        unique_bbox = make_unique_bbox(b_boxes)
        for bbox in unique_bbox:
            temp_bbox = {
                'minx': bbox.minx,
                'miny': bbox.miny,
                'maxx': bbox.maxx,
                'maxy': bbox.maxy,
            }
            final_bbox.append(temp_bbox)

        return final_bbox


def make_unique_bbox(bounding_boxes):
    unique_bboxes = []
    for bbox in bounding_boxes:
        if bbox not in unique_bboxes:
            unique_bboxes.append(bbox)
    return unique_bboxes


def xml_to_json(path):
    temp_cases = []  # dictionary case object list
    for xml_file in glob.glob(path + '/*.xml'):
        temp = xml_file.split('/')
        file_name = temp[len(temp) - 1][:-4]
        tree = ET.parse(xml_file)
        root = tree.getroot()
        images = root.findall('mark')

        for image in images:
            number = image.find('image').text
            image_id = file_name + '_' + number

            temp_bboxes = image.find('svg').text
            bounding_boxes = create_bounding_box(temp_bboxes)

            case = {
                'image_id': image_id,
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
                'bbox': bounding_boxes,
            }
            temp_cases.append(case)

    cases = {
        'cases': temp_cases
    }
    save_json(json.dumps(cases))


def save_json(final_json):
    text_file = open("/Users/klaudiaszucs/thesis_work/tfrecord_converter/files/json_files/validation.json", "w")
    text_file.write(final_json)
    text_file.close()


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
    file_path = 'files/' + 'validation'
    xml_to_json(file_path)


main()
