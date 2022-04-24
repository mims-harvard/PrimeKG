#!pip install goatools
import numpy as np
import pandas as pd

from goatools.anno.genetogo_reader import Gene2GoReader
objanno_hsa = Gene2GoReader(filename='../data/ncbigene/gene2go', taxids=[9606]) #taxids for human
ns2assc_hsa1 = objanno_hsa.get_ns2assc()

gene_go_associations = []
# molecular function
for gene, goterms in ns2assc_hsa1['MF'].items(): 
    for go in goterms: 
        gene_go_associations.append((gene, go, 'molecular_function'))
# biological process        
for gene, goterms in ns2assc_hsa1['BP'].items(): 
    for go in goterms: 
        gene_go_associations.append((gene, go, 'biological_process'))
# cellular component
for gene, goterms in ns2assc_hsa1['CC'].items(): 
    for go in goterms: 
        gene_go_associations.append((gene, go, 'cellular_component'))
        
gene_go_associations = pd.DataFrame(gene_go_associations, columns=['ncbi_gene_id', 'go_term_id', 'go_term_type'])
gene_go_associations.loc[:, 'go_term_id'] = [str(int(x.split(':')[1])) for x in gene_go_associations.get(['go_term_id']).values.reshape(-1)]
gene_go_associations.to_csv('../data/ncbigene/protein_go_associations.csv', index=False)
