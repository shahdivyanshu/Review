import pandas as pd
from thefuzz import fuzz, process
from sqlalchemy import Column, Integer, String
import csv
df=pd.read_csv("C:\\Users\\Admin\\Desktop\\citymall\\static\\query_result_2022-02-02T05_06_34.764057Z.csv")

df.loc[:, 'user_name'] = df.user_name.astype(str)
def get_ids(reviewer_name:str, column_users='user_name', column_id='user_id', limit=100, min_prob=100):
    names = list(df[column_users])
    best_match = list(set(process.extractBests(reviewer_name, names, score_cutoff=min_prob, limit=limit)))
    user_ids_from_database = []
    for found_name, prob in best_match:
      user_ids_from_database.extend(df[df[column_users] == found_name][column_id].values)
    return set(user_ids_from_database), best_match

#ids_r, names_r = get_ids(reviewer_name=name_to_find, df_curr=df, column_users='user_name', column_id='user_id', limit=(df.shape[0])//10000, min_prob=100)
