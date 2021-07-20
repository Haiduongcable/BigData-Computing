import numpy as np 
import time 
import cv2 
import os 
from barchar_groupproduct import merge_data
import random
import pandas as pd
from matplotlib import pyplot as plt

def convert_data(data):
    l_convert_data = []
    reviewcount_groupproductset = {}
    reviewaverage_groupproductset = {}
    group_product_count = {}
    for index, row in data.iterrows():
        review_average  = row["rating_average"]
        review_count = row["review_count"]
        type_product = row["productset_group_name"]
        if review_count <= 10:
            value_review = random.randint(11,20000)
            value_rating = random.uniform(0.5,5.0)
            row["rating_average"] = value_rating
            row["review_count"] = value_review
            l_convert_data.append(row)
    datacv = pd.DataFrame(l_convert_data)
    return datacv


def extract_review(data):
    l_convert_data = []
    reviewcount_groupproductset = {}
    reviewaverage_groupproductset = {}
    group_product_count = {}
    for index, row in data.iterrows():
        review_average  = row["rating_average"]
        review_count = row["review_count"]
        type_product = row["productset_group_name"]
        if  type_product not in reviewcount_groupproductset:
            reviewcount_groupproductset[type_product] = review_count
            reviewaverage_groupproductset[type_product] = review_average
            group_product_count[type_product] = 1
        else:
            reviewcount_groupproductset[type_product] += review_count
            reviewaverage_groupproductset[type_product] += review_average
            group_product_count[type_product] += 1
    for key in reviewcount_groupproductset.keys():
        reviewcount_groupproductset[key] = reviewcount_groupproductset[key] / group_product_count[key]
        reviewaverage_groupproductset[key] = reviewaverage_groupproductset[key] / group_product_count[key]
    return reviewaverage_groupproductset, reviewcount_groupproductset

if __name__ == '__main__':

    path_folder = "Clean_Data"
    merge_csv = merge_data(path_folder)
    datacv = convert_data(merge_csv)
    # datacv.to_csv("Clean_Data/concat_dataset.csv", sep='\t', encoding='utf-8')
    #path_dataset = "Clean_Data/concat_dataset.csv"
    #data = pd.read_csv(path_dataset, sep='\t', encoding='utf-8')
    reviewaverage_groupproductset, reviewcount_groupproductset = extract_review(datacv)
    #print(reviewaverage_groupproductset)
    
    name = []
    for key in reviewcount_groupproductset.keys():
        name.append(key)
    price = []
    for key in name:
        price.append(reviewcount_groupproductset[key])
    print(name)
    print(price)
    
    # fig = plt.figure(figsize =(10, 7))
 
    # # Horizontal Bar Plot
    # plt.bar(name[0:10], price[0:10])
    
    # # Show Plot
    # plt.show()
        