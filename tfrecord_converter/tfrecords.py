import os
import glob
import dataset_util
import pandas as pd
import tf_slim as slim
import tensorflow as tf
import matplotlib.pyplot as plt

# INITIALIZE JSON PATH VARIABLES
JSON_FILE_PATH = os.path.join(os.getcwd(), 'files/json_files/main_test.json')
# INITIALIZE IMAGE PATH VARIABLES
IMAGES_PATH = os.path.join(os.getcwd(), 'files/dataset/main_test')
# INITIALIZE TFRECORD DIRECTORY
tfrecords_dir = os.path.join(os.getcwd(), 'files/tfrecords/main_test')
# LOAD JSON FILES TO DATAFRAME
df = pd.read_json(JSON_FILE_PATH)  # = annotations
# INITIALIZE THE NUMBER OF TFRECORDS DEPEND ON THE NUMBER OF SAMPLE IMAGES
num_samples = 1
# len(glob.glob(IMAGES_PATH + '/*.xml'))
num_tfrecords = len(df) // num_samples

if len(df) % num_samples:
    num_tfrecords += 1  # add one record if there are any remaining samples

if not os.path.exists(tfrecords_dir):
    os.makedirs(tfrecords_dir)


def create_feature_example(image, example):
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
        "bbox/xmin": dataset_util.float_feature_list(example["xmin"]),
        "bbox/xmax": dataset_util.float_feature_list(example["xmax"]),
        "bbox/ymin": dataset_util.float_feature_list(example["ymin"]),
        "bbox/ymax": dataset_util.float_feature_list(example["ymax"]),
        "bbox_number": dataset_util.float_feature_list(len(example["xmin"]))
    }

    return tf.train.Example(features=tf.train.Features(feature=feature))


def parse_tfrecord_fn(example):
    feature_description = {
        "image": tf.io.FixedLenFeature([], tf.string),
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
        "bbox/xmin": tf.io.VarLenFeature(tf.float32),
        "bbox/xmax": tf.io.VarLenFeature(tf.float32),
        "bbox/ymin": tf.io.VarLenFeature(tf.float32),
        "bbox/ymax": tf.io.VarLenFeature(tf.float32),
        "bbox_number": tf.io.FixedLenFeature([], tf.int64),
    }

    parsed_features = tf.io.parse_single_example(example, feature_description)
    parsed_features["image"] = tf.io.decode_jpeg(parsed_features["image"], channels=3)

    return parsed_features


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
                example = create_feature_example(image, sample)
                writer.write(example.SerializeToString())

    print('success - tfrecord has been created')


def generate_sample_from_tfrecord():
    raw_dataset = tf.data.TFRecordDataset(f"{tfrecords_dir}/file_00-{num_samples}.tfrec")
    parsed_dataset = raw_dataset.map(parse_tfrecord_fn)

    for features in parsed_dataset.take(1):
        for key in features.keys():
            if key != "image":
                print(f"{key}: {features[key]}")

        print(f"Image shape: {features['image'].shape}")
        plt.figure(figsize=(9, 9))
        plt.imshow(features["image"].numpy())
        plt.show()


def main():
    # create_tfrecord(df)
    generate_sample_from_tfrecord()


main()
