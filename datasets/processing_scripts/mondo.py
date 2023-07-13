import os
import numpy as np
import pandas as pd
from mondo_obo_parser import OBOReader

pth = "../data/mondo/mondo.obo"
data = [*iter(OBOReader(pth))]
mondo_terms = pd.DataFrame([{'id':x.item_id, 
                             'name':x.name, 
                             'definition':x.definition,
                             'is_obsolete':x.is_obsolete,
                             'replacement_id': x.replaced_by} for x in data])
print(mondo_terms.shape[0], "total terms")
print(mondo_terms.query('is_obsolete==False').shape[0], 'not obsolete')

print('"is_a" relationships between mondo terms')
mondo_parents = []
for x in data: 
    if x._parents: 
        for parent in x._parents: 
            mondo_parents.append({'parent':parent, 'child':x.item_id})           
mondo_parents = pd.DataFrame(mondo_parents).drop_duplicates()

print("cross references from mondo to other ontologies")
mondo_xrefs = []
for x in data: 
    if x.xrefs:
        for xref in x.xrefs: 
            if xref is not None:
                ont, name = xref.split(':')            
                mondo_xrefs.append({'ontology_id':name, 'ontology':ont, 'mondo_id':x.item_id})            
mondo_xrefs = pd.DataFrame(mondo_xrefs).drop_duplicates()
print('references to the following ontologies are available:')
print(np.unique(mondo_xrefs.get('ontology').values))
print('references from mondo to mondo indicate equivalence/synonyms')

print("groupings of mondo terms")
mondo_subsets = []
for x in data: 
    if x.subsets: 
        for sub in x.subsets: 
            mondo_subsets.append({'id':x.item_id, 'subset':sub})           
mondo_subsets = pd.DataFrame(mondo_subsets).drop_duplicates()
print('available subsets by count:')
mondo_subsets.groupby('subset').count().sort_values('id',ascending=False)

mondo_def = mondo_terms.get(['id','name','definition']).fillna('').copy()
for x in mondo_def.itertuples(): 
    if x.definition:
        mondo_def.loc[x.Index, 'definition'] =  x.definition.split('\"')[1]
    else: 
        mondo_def.loc[x.Index, 'definition'] = float('nan')
mondo_def = mondo_def.dropna()
mondo_terms = mondo_terms.drop('definition', axis=1)

mondo_terms.to_csv('../data/mondo/mondo_terms.csv', index=False)
mondo_parents.to_csv('../data/mondo/mondo_parents.csv', index=False)
mondo_xrefs.to_csv('../data/mondo/mondo_references.csv', index=False)
mondo_subsets.to_csv('../data/mondo/mondo_subsets.csv', index=False)
mondo_def.to_csv('../data/mondo/mondo_definitions.csv', index=False)