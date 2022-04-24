#!pip install goatools
import numpy as np
import pandas as pd
from goatools.obo_parser import GODag
godag = GODag("../data/go/go-basic.obo")

all_go_terms = set()
for k,v in godag.items(): 
    term = (v.item_id, v.name, v.namespace)
    all_go_terms.add(term)  
all_go_terms = pd.DataFrame(all_go_terms, columns=['go_term_id','go_term_name','go_term_type'])

# adding children for each go term
edges = set()
for _, x in all_go_terms.iterrows(): 
    parent = x.go_term_id
    children = godag[parent].children
    for child in children: 
        edges.add((parent, child.id))
edges = pd.DataFrame(edges, columns=['x','y'])

all_go_terms.loc[:, 'go_term_id'] = [str(int(x.split(':')[1])) for x in all_go_terms.get(['go_term_id']).values.reshape(-1)]
edges.loc[:, 'x'] = [str(int(x.split(':')[1])) for x in edges.get(['x']).values.reshape(-1)]
edges.loc[:, 'y'] = [str(int(x.split(':')[1])) for x in edges.get(['y']).values.reshape(-1)]

all_go_terms.to_csv('../data/go/go_terms_info.csv', index=False)
edges.to_csv('../data/go/go_terms_relations.csv', index=False)