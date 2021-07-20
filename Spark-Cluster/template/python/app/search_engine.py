import pandas as pd 
import numpy as np 
import time 
import sklearn
import editdistance
import heapq


def search(keyword, database):
    '''
    get edit distance similarity score and sort
    '''
    l_score = []
    for index, row in database["name"].iteritems():
        score = editdistance.eval(keyword, row)
        l_score.append(score)
    l_score = np.array(l_score)
    top_idx_minscore = (l_score).argsort()[:20]
    #top_n_minscore = heapq.nsmallest(5, l_score)
    #print(top_idx_minscore)
    rs_query = []
    for index in top_idx_minscore:
        rs_query.append(database.iloc[index]["name"])
    
    while True:
        time.sleep(10)
        break
    return rs_query
    

if __name__ == '__main__':
    path_csv = ""
    csv_dienthoai =  pd.read_csv("/home/haiduong/Documents/Project_2/Data/data_dienthoai/product.csv"\
                        ,error_bad_lines=False)
    
    keyword = 'điện thoại'
    rs_query = search(keyword, csv_dienthoai)
    file = open("../result/rs_search_engine.txt", 'w')
    for value in rs_query:
        file.write(value + "\t")
    file.close()

    
    
    