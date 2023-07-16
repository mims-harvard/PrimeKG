import os
import numpy as np
import pandas as pd

pth = "../data/uberon/ext.obo"
with open(pth, 'r') as f: 
    data = f.read()
data = data.split('[Term]\n')[1:-1]

data = [rec.split('\n') for rec in data]
data = [[x for x in rec if x] for rec in data]
data = [{x.split(': ')[0]:x.split(': ')[1] for x in rec} for rec in data]
data = [{k:v.split(' !')[0] for k,v in dct.items()} for dct in data]
data = pd.DataFrame(data)

relations = []
for x in data.get('relationship').values: 
    if type(x) == str: 
        r = tuple(x.split(' ')[0:2])
    else: 
        r = (None, None)
    relations.append(r)
relations = pd.DataFrame(relations, columns=['relation_type','relation_id'])

df = pd.concat([data, relations], axis=1)
df = df.query('is_obsolete!="true"')
df = df.drop(['is_obsolete', 'replaced_by', 'consider', 'created_by', 'creation_date'], axis=1)
# updated PrimeKG: drop two obsolete terms, UBERON:0039300 and UBERON:0039302 (not marked as obsolete in OBO file) 
df = df.dropna(subset=['is_a'])
df = df[df.get('id').str.startswith('UBERON')]
df = df.reset_index().drop('index', axis=1)

df_terms = df.get(['id', 'name', 'def'])
df_rels = df.get(['id','relation_type', 'relation_id']).dropna()
df_rels = df_rels[df_rels.get('relation_id').str.startswith('UBERON')]
df_is_a = df.get(['id', 'is_a'])
df_is_a = df_is_a[df_is_a.get('is_a').str.startswith('UBERON')]

df_terms.loc[:, 'id'] = [str(int(x.split(':')[1])) for x in df_terms.get(['id']).values.reshape(-1)]
df_is_a.loc[:, 'id'] = [str(int(x.split(':')[1])) for x in df_is_a.get(['id']).values.reshape(-1)]
df_is_a.loc[:, 'is_a'] = [str(int(x.split(' {')[0].split(':')[1])) for x in df_is_a.get(['is_a']).values.reshape(-1)]
df_rels.loc[:, 'id'] = [str(int(x.split(':')[1])) for x in df_rels.get(['id']).values.reshape(-1)]
df_rels.loc[:, 'relation_id'] = [str(int(x.split(':')[1])) for x in df_rels.get(['relation_id']).values.reshape(-1)]

df_terms.to_csv('../data/uberon/uberon_terms.csv', index=False)
df_rels.to_csv('../data/uberon/uberon_rels.csv', index=False)
df_is_a.to_csv('../data/uberon/uberon_is_a.csv', index=False)
