import time 
from multiprocess import Process 

from __future__ import print_function
from __future__ import unicode_literals
import numpy as np 
import pandas as pd 
import os 
import time 
from tqdm import tqdm 
import numpy as np
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from multiprocessing import Pool
import multiprocessing as mp


def split_data(data_clean, number_split = 8):
    l_data_clean = np.array_split(data_clean, number_split)
    return l_data_clean


def split_product(product_name):
    type_product = product_name.split("/")[0]
    return type_product

def multithread_clean(index_data):
    data_clean = l_data_clean[index_data]
    log_group_product = []
    if type_data == 'laptop':
        log_group_product = ['Laptop - Máy Vi Tính - Linh kiện']
    elif type_data == 'nhacua':
        tmp_l = []
        for index, row in data_clean.iterrows():
            type_product = split_product(row["productset_group_name"])
            row["productset_group_name"] = type_product
            tmp_l.append(row)
        data_clean = pd.DataFrame(tmp_l)
        return data_clean
    elif type_data == 'thucpham':
        log_group_product = ['Bách Hóa Online']
    elif type_data == 'sach':
        log_group_product= ['Nhà Sách Tiki']
    elif type_data == 'dienthoai':
        log_group_product = ['Hàng Quốc Tế', 'Thiết Bị Số - Phụ Kiện Số', 'Điện Thoại - Máy Tính Bảng']
    
    tmp_l = []
    for index, row in data_clean.iterrows():
        type_product = split_product(row["productset_group_name"])
        row["productset_group_name"] = type_product
        if type_product not in log_group_product:
            print(type_product)
            continue
        else:
            tmp_l.append(row)
    data_clean = pd.DataFrame(tmp_l)
    q.append(data_clean)

def merge_result(l_data_clean):
    data_clean = l_data_clean[0]
    for i in range(1,len(l_data_clean)):
        data_clean = data_clean.merge(l_data_clean[i], axis = 1)
    return data_clean

def clean_data(number_worker = 2, number_process_per_worker = 2):
    global type_data 
    type_data = "nhacua"
    data = spark.read.parquet("hdfs://node-master:9000/user/hadoop/SparkData/data/product.csv", error_bad_lines = False)

    #drop error row and get specify columns
    data_clean = data[['id', 'name', 'url_key', 'url_path', 'type', 'short_description',\
                           'price', 'list_price', 'discount', 'discount_rate', 'rating_average',\
                           'review_count', 'order_count', 'thumbnail_url', 'productset_group_name',\
                           'categories']]

    #clean name
    name_column = data_clean["name"]
    for index, row in name_column.iteritems():
        name_clean = row.split(" - ")[0]
        print(name_clean)
        data_clean.iloc[index]["name"] = name_clean
    global l_data_clean 
    l_data_clean = split_data(data_clean)

    mp.set_start_method('spawn')
    global q
    q = mp.Queue()
    with Pool(8) as p:
        print(p.map(multithread_clean, [1, 2, 3,4,5,6,7,8]))
    
    #print(q.get())
    l_data_clean = q.get()
    data_clean = merge_result(l_data_clean)
    return data_clean
    
if __name__ == '__main__':
    from pyspark import SparkConf
    from pyspark import SparkContext

    conf = SparkConf()
    conf.setMaster('spark://10.144.212.63:7077')
    conf.setAppName('Extract rating average')
    sc = SparkContext(conf=conf)
    type_data = "nhacua"
    s_time = time.time()
    data_clean = clean_data(type_data = type_data)
    print("Done in: ", time.time() - s_time)
    #data_clean.to_csv("Clean_Data/" + type_data + ".csv", sep='\t', encoding='utf-8')
    