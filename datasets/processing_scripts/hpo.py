import os
import numpy as np
import pandas as pd
from hpo_obo_parser import OBOReader

pth = "../data/hpo/hp.obo"
data = [*iter(OBOReader(pth))]
hp_terms = pd.DataFrame([{'id':x.item_id, 
                             'name':x.name, 
                             'is_obsolete':x.is_obsolete,
                             'replacement_id': x.replaced_by} for x in data])
print(hp_terms.shape[0], "total terms")
print(hp_terms.query('is_obsolete==False').shape[0], 'not obsolete')

print('"is_a" relationships between hp terms')
hp_parents = []
for x in data: 
    if x._parents: 
        for parent in x._parents: 
            hp_parents.append({'parent':parent, 'child':x.item_id})           
hp_parents = pd.DataFrame(hp_parents).drop_duplicates()
hp_parents.head()

print("cross references from hp to other ontologies")
hp_xrefs = []
for x in data: 
    if x.xrefs:
        for xref in x.xrefs: 
            ont, name = xref.split(':')            
            hp_xrefs.append({'ontology_id':name, 'ontology':ont, 'hp_id':x.item_id})           
hp_xrefs = pd.DataFrame(hp_xrefs).drop_duplicates()
print('references to the following ontologies are available:')
print(np.unique(hp_xrefs.get('ontology').values))
print('references from hp to hp indicate equivalence/synonyms')

hp_terms.to_csv('../data/hpo/hp_terms.csv', index=False)
hp_parents.to_csv('../data/hpo/hp_parents.csv', index=False)
hp_xrefs.to_csv('../data/hpo/hp_references.csv', index=False)