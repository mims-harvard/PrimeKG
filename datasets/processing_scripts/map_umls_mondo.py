import os
import numpy as np
import pandas as pd

df_mondo_terms = pd.read_csv('../data/mondo/mondo_terms.csv').get(['name','id'])
df_mondo_xref = pd.read_csv('../data/mondo/mondo_references.csv')
df_umls = pd.read_csv('../data/umls/umls.csv')

map_direct = df_mondo_xref.query('ontology=="UMLS"').get(['ontology_id','mondo_id']).rename(columns={'ontology_id':'umls_id'})

df_umls_join = df_umls.get(['cui','source_cui', 'source_descriptor_dui', 'source', 'source_code']).drop_duplicates()

map1 = pd.merge(df_umls_join, df_mondo_xref, 'inner', left_on='source_cui', right_on='ontology_id')
map2 = pd.merge(df_umls_join, df_mondo_xref, 'inner', left_on='source_descriptor_dui', right_on='ontology_id')
map3 = pd.merge(df_umls_join, df_mondo_xref, 'inner', left_on='source_code', right_on='ontology_id')

map_all = pd.concat([map1, map2, map3]).drop_duplicates()

valid = []
pairs = [('OMIM','OMIM'),
         #('OMIM','OMIMPS'),
         #('NCI_NICHD','NCIT'),
         #('NCI_FDA','NCIT'),
         #('NCI_CTRP','NCIT'),
         ('NCI','NCIT'),
         #('MTHICD9','ICD9'),
         ('MSH','MESH'),
         ('MDR','MedDRA'),
         #('ICD10CM','ICD10'),
         ('ICD10','ICD10'),
         ('SNOMEDCT_US','SCTID')]

for s,o in pairs: 
    valid.append(map_all.query('source==@s and ontology==@o'))
    
map_indirect = pd.concat(valid).rename(columns={'cui':'umls_id'})


df_umls_mondo = pd.concat([map_direct, map_indirect.get(['umls_id', 'mondo_id'])]).drop_duplicates()
print(df_umls_mondo.head(1))
print(df_umls_mondo.shape)


df_umls_mondo.to_csv('../data/vocab/umls_mondo.csv', index=False)
