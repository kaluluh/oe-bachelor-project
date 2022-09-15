import numpy as np
import json
from converter_util import boundingbox


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
