# kitti_train_val.py
# 此代码和data文件夹同目录
import glob
# path = ''
def generate_train_and_val(image_path, txt_file):
    with open(txt_file, 'w') as tf:
        for jpg_file in glob.glob(image_path + '*.png'):
            tf.write(jpg_file + '\n')

generate_train_and_val( 'KATTI/JPEGImages/',  'KATTI/train.txt') # 生成的train.txt文件所在路径
generate_train_and_val('KATTI/JPEGImages/','KATTI/val.txt') # 生成的val.txt文件所在路径
