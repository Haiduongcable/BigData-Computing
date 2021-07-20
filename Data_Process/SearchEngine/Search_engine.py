
import os 
import numpy as np 
import editdistance

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
    print(top_idx_minscore)
    rs_query = []
    for index in top_idx_minscore:
        rs_query.append(database.iloc[index]["name"])
    print(rs_query)
    