import os
import numpy as np
import pandas as pd

drug_atc = pd.read_csv('../data/sider/drug_atc.tsv', sep='\t', header=None)
drug_atc.columns = ['stitch', 'atc']
all_se = pd.read_csv('../data/sider/meddra_all_se.tsv', sep='\t', header=None)
all_se.columns = ['stitch_id_1', 'stitch_id_2', 'UMLS_from_label', 
                  'meddra_concept_type', 'UMLS_from_meddra', 'side_effect_name']

all_se = all_se.query('meddra_concept_type=="PT"')

side_effects = pd.merge(drug_atc, all_se, left_on='stitch', right_on='stitch_id_1').get(['atc', 'UMLS_from_label', 'UMLS_from_meddra','side_effect_name'])
side_effects.to_csv('../data/sider/sider.csv', index=False)