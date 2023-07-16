import numpy as np
import pandas as pd

df = pd.read_csv('../data/bgee/Homo_sapiens_expr_advanced.tsv', sep='\t')

df = df[df.get('Anatomical entity ID').str.startswith('UBERON')]

df = df.get(['Gene ID', 'Gene name', 'Anatomical entity ID',
       'Anatomical entity name', 'Expression', 'Call quality', 'Expression rank'])

df = df.rename(columns={'Gene ID':'gene_id',
                   'Gene name':'gene_name',
                   'Anatomical entity ID':'anatomy_id',
                   'Anatomical entity name':'anatomy_name',
                   'Expression':'expression',
                   'Call quality':'call_quality',
                   'Expression rank': 'expression_rank'})

df = df.query('call_quality=="gold quality"')
df = df.query('expression_rank<25000')

# updated PrimeKG: remove rows that specify cell type within a particular tissue
df = df[~df['anatomy_id'].str.contains("∩")]

df.loc[:, 'anatomy_id'] = [str(int(x.split(':')[1])) for x in df.get(['anatomy_id']).values.reshape(-1)]
df.to_csv('../data/bgee/anatomy_gene.csv', index=False)

