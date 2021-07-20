import numpy as np 
import time 
import cv2 
import os 
from barchar_groupproduct import merge_data
import random
import pandas as pd
from matplotlib import pyplot as plt


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

    path_folder = "Data_Clean"
    datacv = merge_data(path_folder)
    reviewaverage_groupproductset, reviewcount_groupproductset = extract_review(datacv)
    
    name = []
    for key in reviewcount_groupproductset.keys():
        name.append(key)
    price = []
    for key in name:
        price.append(reviewcount_groupproductset[key])
    print(name)
    print(price)
    
    fig, ax = plt.subplots(figsize =(16, 9), dpi = 200)
    # Horizontal Bar Plot
    ax.barh(name, price)
    
    # Remove axes splines
    for s in ['top', 'bottom', 'left', 'right']:
        ax.spines[s].set_visible(False)
    
    # Remove x, y Ticks
    ax.xaxis.set_ticks_position('none')
    ax.yaxis.set_ticks_position('none')
    
    # Add padding between axes and labels
    ax.xaxis.set_tick_params(pad = 5)
    ax.yaxis.set_tick_params(pad = 10)
    
    # Add x, y gridlines
    ax.grid(b = True, color ='grey',
            linestyle ='-.', linewidth = 0.5,
            alpha = 0.2)
    
    # Show top values
    ax.invert_yaxis()
    
    # Add annotation to bars
    for i in ax.patches:
        plt.text(i.get_width()+0.05, i.get_y()+0.5,
                str(round((i.get_width()), 2)),
                fontsize = 10, fontweight ='bold',
                color ='grey')
    
    # Add Plot Title
    ax.set_title('Group product and their average review point',
                loc ='left', )
    
    # Add Text watermark
    fig.text(0.9, 0.15, 'Average point', fontsize = 12,
            color ='grey', ha ='right', va ='bottom',
            alpha = 0.7)
    
    # Show Plot
    plt.show()
        