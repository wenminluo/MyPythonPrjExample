#Filename e:MNISTTest.py

import os
import struct
import numpy as np

# load_mnist 函数返回两个数组, 第一个是一个 n x m 维的 NumPy array(images), 这里的 n 是样本数(行数), m 是特征数(列数)
# . 训练数据集包含 60,000 个样本, 测试数据集包含 10,000 样本. 在 MNIST 数据集中的每张图片由 28 x 28 个像素点构成,
#   每个像素点用一个灰度值表示. 在这里, 我们将 28 x 28 的像素展开为一个一维的行向量, 这些行向量就是图片数组里的行
#   (每行 784 个值, 或者说每行就是代表了一张图片). load_mnist 函数返回的第二个数组(labels) 包含了相应的目标变量,
#    也就是手写数字的类标签(整数 0-9).
def load_mnist(path, kind='train'):
    """Load MNIST data from `path`"""
    labels_path = os.path.join(path,
                               '%s-labels-idx1-ubyte'
                               % kind)
    images_path = os.path.join(path,
                               '%s-images-idx3-ubyte'
                               % kind)
    with open(labels_path, 'rb') as lbpath:
        magic, n = struct.unpack('>II',
                                 lbpath.read(8))
        labels = np.fromfile(lbpath,
                             dtype=np.uint8)

    with open(images_path, 'rb') as imgpath:
        magic, num, rows, cols = struct.unpack('>IIII',
                                               imgpath.read(16))
        images = np.fromfile(imgpath,
                             dtype=np.uint8).reshape(len(labels), 784)

    return images, labels


# # 下载MNIST数据并解压
from  tensorflow.examples.tutorials.mnist   import   input_data
mnist  =  input_data.read_data_sets ( "MNIST_data/",  one_hot=True )

#训练集的张量
print ( mnist.train.images.shape )

#训练集标签的张量
print ( mnist.train.labels.shape )

#验证集的张量
print ( mnist.validation.images.shape )

#验证集标签的张量
print ( mnist.validation.labels.shape )

#测试集的张量
print ( mnist.test.images.shape )

#测试集标签的张量
print ( mnist.test.labels.shape )