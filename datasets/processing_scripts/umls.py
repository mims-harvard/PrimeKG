import os
import numpy as np
import pandas as pd

with open('../data/umls/MRCONSO.RRF', 'r') as f: 
    data = f.readlines()
data = [x.split('|') for x in data]

columns = ['cui', 'language', 'term_status', 'lui', 'string type', 'string_identifier', 'is_preferred',
          'aui', 'source_aui', 'source_cui', 'source_descriptor_dui', 'source', 
          'source_term_type', 'source_code', 'source_name', 'x', 'x', 'x', 'x']

df_umls = pd.DataFrame(data, columns = columns)
df_umls = df_umls.query('language=="ENG"')
df_umls.head()

df_umls.to_csv('../data/umls/umls.csv', index=False)