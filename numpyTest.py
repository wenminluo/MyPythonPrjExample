import numpy as np



## 数组的索引， 切片
# 给定均值/标准差/未读的正态分布
# 正态生成4行5列的二维数组
arr = np.random.normal(1.75,0.1,(4,5));
print(arr);

# 均匀分布
# 创建指定形状数组(范围0-1之间)
arr_rand = (np.random.rand(4,5));
print("arr_rand:\n",arr_rand);

# 创建指定范围内的一个数
arr_un = np.random.uniform(4,5);
print("arr_un:\n",arr_un);

# 创建指定范围内的一个整数
arr_ranint = np.random.randint(4,5);
print("arr_ranint\n",arr_ranint);


# # 截取第1至第2行的第2至3列(从第0行算起)
# after_arr = arr[1:3,2:4]
# print( after_arr );


# # 使用 NumPy 生成假数据(phony data), 总共 100 个点.
# x_data = np.float32(np.random.rand(2, 100)) # 随机输入
# y_tmpdata = np.dot([0.100,0.200],x_data);
# y_data = np.dot([0.100, 0.200], x_data) + 0.300
#
# # print("x_data\n",x_data.size);
# # print("x_data\n",x_data.dtype);
# print("x_dataShap\n",x_data.shape);
# print("x_data\n",x_data );
#
# print( "y_tmpShape\n",y_tmpdata.shape );
# print( "y_tmpdata\n",y_tmpdata );
#
# print("y_dataShape\n",y_data.shape);
# print("y_data\n",y_data );