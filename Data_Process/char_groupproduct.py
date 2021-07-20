import numpy as np 
import os 
import time 
import cv2 
import matplotlib.pyplot as plt 
import pandas as pd

def merge_data(path_folder):
    l_csv = []
    for csv in os.listdir(path_folder):
        path_csv = path_folder + "/" + csv
        print(path_csv)
        csv_file = pd.read_csv(path_csv, sep='\t', encoding='utf-8')
        l_csv.append(csv_file)
    merge_csv = l_csv[0]
    for i in range(1, len(l_csv)):
        merge_csv = merge_csv.append(l_csv[i])
    return merge_csv

def extract_group_prob(csv_file):
    product_count = {}
    for index, row in csv_file.iterrows():
        groupproduct = row["productset_group_name"]
        if groupproduct not in product_count:
            product_count[groupproduct] = 1
        else:
            product_count[groupproduct] += 1
    total_product = 0
    for key in product_count.keys():
        total_product += product_count[key]
    product_prob = {}
    for key in product_count.keys():
        product_prob[key] = product_count[key] / total_product
    return product_prob

if __name__ == '__main__':
    import matplotlib.pyplot as plt
    import numpy as np
    path_folder = "Data_Clean"
    merge_csv = merge_data(path_folder)
    product_count = extract_group_prob(merge_csv)
    print(product_count)


    y = []
    mylabels = []
    count = 0
    for key in product_count.keys():
        value_prob = product_count[key]
        y.append(value_prob)
        mylabels.append(key)
    y = np.array(y)

    plt.figure(dpi=1500)
    plt.pie(y, labels = mylabels)
    plt.legend(title = "Prob:", loc = "upper right", fontsize = 3)
    plt.show()

    
