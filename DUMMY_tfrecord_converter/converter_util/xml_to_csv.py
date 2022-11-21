import glob
import os
import pandas as pd
import xml.etree.cElementTree as ET

from converter_util.xml_to_json import create_bounding_box


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
