import os
import pandas as pd
import glob
import tensorflow as tf

import dataset_util

# INITIALIZE JSON PATH VARIABLES
JSON_FILE_PATH = os.path.join(os.getcwd(), 'files/json_files/validation.json')

# INITIALIZE IMAHE PATH VARIABLES
IMAGES_PATH = os.path.join(os.getcwd(), 'files/validation')

# INITIALIZE TFRECORD DIRECTORY
tfrecords_dir = os.path.join(os.getcwd(), 'files/tfrecords/validation')

# LOAD JSON FILES TO DATAFRAME
df = pd.read_json(JSON_FILE_PATH)  # = annotations

# INITIALIZE THE NUMBER OF TFRECORDS DEPEND ON THE NUMBER OF SAMPLE IMAGES
num_samples = len(glob.glob(IMAGES_PATH + '/*.xml'))
num_tfrecords = len(df) // num_samples

if len(df) % num_samples:
    num_tfrecords += 1  # add one record if there are any remaining samples

if not os.path.exists(tfrecords_dir):
    os.makedirs(tfrecords_dir)  # creating TFRecords output folder


# CREATE TRAIN FEATURE EXAMPLE
def create_example(image,example):
    feature = {
        "image": dataset_util.image_feature(image),
        "case_id": dataset_util.bytes_feature(example['case_id']),
        "age": dataset_util.bytes_feature(example['age']),
        "sex": dataset_util.bytes_feature(example["sex"]),
        "composition": dataset_util.bytes_feature(example["composition"]),
        "echogenicity": dataset_util.bytes_feature(example["echogenicity"]),
        "margins": dataset_util.bytes_feature(example["margins"]),
        "calcifications": dataset_util.bytes_feature(example["calcifications"]),
        "tirads": dataset_util.bytes_feature(example["tirads"]),
        "reportbacaf": dataset_util.bytes_feature(example["reportbacaf"]),
        "reporteco": dataset_util.bytes_feature(example["reporteco"]),
        "xmin": dataset_util.float_feature_list(example["xmin"]),
        "xmax": dataset_util.float_feature_list(example["xmax"]),
        "ymin": dataset_util.float_feature_list(example["ymin"]),
        "ymax": dataset_util.float_feature_list(example["ymax"]),
    }

    return tf.train.Example(features=tf.train.Features(feature=feature))


# HOW TO USE THE CREATED FEATURE EXAMPLE
def parse_tfrecord_fn(example):
    feature_description = {
        "image": tf.io.FixedLenFeature([],tf.string),
        "case_id": tf.io.FixedLenFeature([], tf.string),
        "age": tf.io.FixedLenFeature([], tf.string),
        "sex": tf.io.FixedLenFeature([], tf.string),
        "composition": tf.io.FixedLenFeature([], tf.string),
        "echogenicity": tf.io.FixedLenFeature([], tf.string),
        "margins": tf.io.FixedLenFeature([], tf.string),
        "calcifications": tf.io.FixedLenFeature([], tf.string),
        "tirads": tf.io.FixedLenFeature([], tf.string),
        "reportbacaf": tf.io.FixedLenFeature([], tf.string),
        "reporteco": tf.io.FixedLenFeature([], tf.string),
        "xmin": tf.io.FixedLenFeature([], tf.float32),
        "xmax": tf.io.FixedLenFeature([], tf.float32),
        "ymin": tf.io.FixedLenFeature([], tf.float32),
        "ymax": tf.io.FixedLenFeature([], tf.float32),
    }

    example = tf.io.parse_single_example(example, feature_description)
    example["image"] = tf.io.decode_jpeg(example["image"], channels=3)
    example["bbox"] = tf.sparse.to_dense(example["bbox"])

    return example


def create_tfrecord(df):
    for tfrec_num in range(num_tfrecords):
        samples = df[(tfrec_num * num_samples): ((tfrec_num + 1) * num_samples)]
        print(tfrec_num)

        with tf.io.TFRecordWriter(
                tfrecords_dir + "/file_%.2i-%i.tfrec" % (tfrec_num, len(samples))
        ) as writer:
            for sample in samples['cases']:
                image_path = IMAGES_PATH + "/" + sample["case_id"] + ".jpg"
                image = tf.io.decode_jpeg(tf.io.read_file(image_path))
                example = create_example(image,sample)
                writer.write(example.SerializeToString())

    print('success - tfrecord has been created')

def main():
    create_tfrecord(df)


main()
