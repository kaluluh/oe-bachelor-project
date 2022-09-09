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


def json_converter(path):
    json_list = []
    for xml_file in glob.glob(path + '/*.xml'):
        print('hello')
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

    return json_list


def main():
    file_path = 'files/' + 'train'
    json = json_converter(file_path)


main()
