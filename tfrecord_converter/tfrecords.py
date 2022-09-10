import os
import io
import pandas as pd
import glob
import tensorflow as tf

# initialize path variables
TRAIN_PATH = os.path.join(os.getcwd(), 'files/json_files/train.json')
TRAIN_IMAGES = os.path.join(os.getcwd(), 'files/train')
TEST_PATH = os.path.join(os.getcwd(), 'files/json_files/test.json')
tfrecords_dir = os.path.join(os.getcwd(),'files/tfrecords')

# load json into a dataframe
train_df = pd.read_json(TRAIN_PATH) # = annotations

# initialize the number of tfrecords
num_samples = len(glob.glob(TRAIN_IMAGES + '/*.xml'))
num_tfrecods = len(train_df) // num_samples

if len(train_df) % num_samples:
    num_tfrecods += 1  # add one record if there are any remaining samples


# useless
if not os.path.exists(tfrecords_dir):
    os.makedirs(tfrecords_dir)  # creating TFRecords output folder


def create_example(example):
    feature = {
        "case_id": int64_feature(example['case_id']),
        "age": bytes_feature(example['age']),
        "sex": float_feature(example["sex"]),
        "composition": float_feature_list(example["composition"]),
        "echogenicity": int64_feature(example["echogenicity"]),
        "margins": int64_feature(example["margins"]),
        "calcifications": int64_feature(example["calcifications"]),
        "tirads": int64_feature(example["tirads"]),
        "reportbacaf": int64_feature(example["reportbacaf"]),
        "reporteco": int64_feature(example["reporteco"]),
        "image": int64_feature(example["image"]),
    }

    return tf.train.Example(features=tf.train.Features(feature=feature))


def parse_tfrecord_fn(example):
    feature_description = {
        "image": tf.io.FixedLenFeature([], tf.string),
        "path": tf.io.FixedLenFeature([], tf.string),
        "area": tf.io.FixedLenFeature([], tf.float32),
        "bbox": tf.io.VarLenFeature(tf.float32),
        "category_id": tf.io.FixedLenFeature([], tf.int64),
        "id": tf.io.FixedLenFeature([], tf.int64),
        "image_id": tf.io.FixedLenFeature([], tf.int64),
    }

    example = tf.io.parse_single_example(example, feature_description)
    example["image"] = tf.io.decode_jpeg(example["image"], channels=3)
    example["bbox"] = tf.sparse.to_dense(example["bbox"])

    return example




def image_feature(value):
    """Returns a bytes_list from a string / byte."""
    return tf.train.Feature(
        bytes_list=tf.train.BytesList(value=[tf.io.encode_jpeg(value).numpy()])
    )

def bytes_feature(value):
    """Returns a bytes_list from a string / byte."""
    return tf.train.Feature(
        bytes_list=tf.train.BytesList(value=[value.encode()])
    )


def float_feature(value):
    """Returns a float_list from a float / double."""
    return tf.train.Feature(
        float_list=tf.train.FloatList(value=[value])
    )


def int64_feature(value):
    """Returns an int64_list from a bool / enum / int / uint."""
    return tf.train.Feature(
        int64_list=tf.train.Int64List(value=[value])
    )


def float_feature_list(value):
    """Returns a list of float_list from a float / double."""
    return tf.train.Feature(
        float_list=tf.train.FloatList(value=value)
    )