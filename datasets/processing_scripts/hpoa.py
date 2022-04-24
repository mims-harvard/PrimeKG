import os
import numpy as np
import pandas as pd

# reading annotations file 
with open('../data/hpo/phenotype.hpoa', 'r') as f: 
    data = f.readlines()

data_str = ''
for line in data[4:]: 
    data_str += line 
    
with open('phenotype_formatted.hpoa', 'w') as f:
    f.write(data_str)
    
df = pd.read_csv('phenotype_formatted.hpoa', sep='\t').rename(columns={'#DatabaseID':'DatabaseID'})

for x in df.itertuples(): 
    ont, ont_id = x.DatabaseID.split(':')
    df.loc[x.Index, 'disease_ontology'] = ont
    df.loc[x.Index, 'disease_ontology_id'] = ont_id
    df.loc[x.Index, 'hp_id'] = str(int(x.HPO_ID.split(':')[1]))

df.query('Qualifier=="NOT"').get(['hp_id', 'disease_ontology', 'disease_ontology_id']).drop_duplicates().to_csv('../data/hpo/disease_phenotype_neg.csv', index=False)

df.query('Qualifier!="NOT"').get(['hp_id', 'disease_ontology', 'disease_ontology_id']).drop_duplicates().to_csv('../data/hpo/disease_phenotype_pos.csv', index=False)

os.system('rm phenotype_formatted.hpoa')