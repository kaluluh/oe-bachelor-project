import os
import io
import pandas as pd
import tensorflow as tf

df = pd.read_csv ('/Users/klaudiaszucs/thesis_work/tfrecord_converter/thyroid_nodule_train.csv')
df.to_json ('/Users/klaudiaszucs/thesis_work/tfrecord_converter/files/json_files/train.json')