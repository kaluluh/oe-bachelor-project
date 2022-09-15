import os
import io
import pandas as pd
import glob
import tensorflow as tf

# initialize path variables
TRAIN_PATH = os.path.join(os.getcwd(), 'files/json_files/train.json')
TRAIN_IMAGES = os.path.join(os.getcwd(), 'files/train')
TEST_PATH = os.path.join(os.getcwd(), 'files/json_files/test.json')
tfrecords_dir = os.path.join(os.getcwd(), 'files/tfrecords')

# load json into a dataframe
train_df = pd.read_json(TRAIN_PATH)  # = annotations

# initialize the number of tfrecords
num_samples = len(glob.glob(TRAIN_IMAGES + '/*.xml'))
num_tfrecods = len(train_df) // num_samples

if len(train_df) % num_samples:
    num_tfrecods += 1  # add one record if there are any remaining samples

if not os.path.exists(tfrecords_dir):
    os.makedirs(tfrecords_dir)  # creating TFRecords output folder


# create train feature example
def create_example(example):
    feature = {
        "case_id": bytes_feature(example['case_id']),
        "age": int64_feature(example['age']),
        "sex": bytes_feature(example["sex"]),
        "composition": bytes_feature(example["composition"]),
        "echogenicity": bytes_feature(example["echogenicity"]),
        "margins": bytes_feature(example["margins"]),
        "calcifications": bytes_feature(example["calcifications"]),
        "tirads": bytes_feature(example["tirads"]),
        "reportbacaf": bytes_feature(example["reportbacaf"]),
        "reporteco": bytes_feature(example["reporteco"]),
        "image": int64_feature(example["image"]),
        "xmin": _int64_list_feature(example["xmin"]),
        "xmax": _int64_list_feature(example["xmax"]),
        "ymin": _int64_list_feature(example["ymin"]),
        "ymax": _int64_list_feature(example["ymax"]),
    }

    return tf.train.Example(features=tf.train.Features(feature=feature))


# how to use the created feature example
def parse_tfrecord_fn(example):
    feature_description = {
        "case_id": tf.io.FixedLenFeature([], tf.string),
        "age": tf.io.FixedLenFeature([], tf.int64),
        "sex": tf.io.FixedLenFeature([], tf.string),
        "composition": tf.io.FixedLenFeature([], tf.string),
        "echogenicity": tf.io.FixedLenFeature([], tf.string),
        "margins": tf.io.FixedLenFeature([], tf.string),
        "calcifications": tf.io.FixedLenFeature([], tf.string),
        "tirads": tf.io.FixedLenFeature([], tf.string),
        "reportbacaf": tf.io.FixedLenFeature([], tf.string),
        "reporteco": tf.io.FixedLenFeature([], tf.string),
        "image": tf.io.FixedLenFeature([], tf.int64),
        "xmin": tf.io.FixedLenFeature([], tf.int64),
        "xmax": tf.io.FixedLenFeature([], tf.int64),
        "ymin": tf.io.FixedLenFeature([], tf.int64),
        "ymax": tf.io.FixedLenFeature([], tf.int64),
    }

    example = tf.io.parse_single_example(example, feature_description)

    return example


def bytes_feature(value):
    """Returns a bytes_list from a string / byte."""
    return tf.train.Feature(
        bytes_list=tf.train.BytesList(value=[value.encode()])
    )


def int64_feature(value):
    """Returns an int64_list from a bool / enum / int / uint."""
    return tf.train.Feature(
        int64_list=tf.train.Int64List(value=[value])
    )


def _int64_list_feature(value):
    return tf.train.Feature(int64_list=tf.train.Int64List(value=value))
