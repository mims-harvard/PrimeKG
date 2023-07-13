import numpy as np
import pandas as pd

df_carrier = pd.read_csv('../data/drugbank/drugbank_all_carrier_polypeptide_ids.csv/all.csv').query('Species=="Humans"')
df_enzyme = pd.read_csv('../data/drugbank/drugbank_all_enzyme_polypeptide_ids.csv/all.csv').query('Species=="Humans"')
df_target = pd.read_csv('../data/drugbank/drugbank_all_target_polypeptide_ids.csv/all.csv').query('Species=="Humans"')
df_transporter = pd.read_csv('../data/drugbank/drugbank_all_transporter_polypeptide_ids.csv/all.csv').query('Species=="Humans"')

gene_vocab = pd.read_csv('../data/vocab/gene_map.csv', delimiter='\t')
db_vocab = pd.read_csv('../data/vocab/drugbank_vocabulary.csv')

up2ncbi = gene_vocab.get(['NCBI Gene ID(supplied by NCBI)', 'UniProt ID(supplied by UniProt)']).dropna().set_index('UniProt ID(supplied by UniProt)').to_dict()['NCBI Gene ID(supplied by NCBI)']
ncbi2up = gene_vocab.get(['NCBI Gene ID(supplied by NCBI)', 'UniProt ID(supplied by UniProt)']).dropna().set_index('NCBI Gene ID(supplied by NCBI)').to_dict()['UniProt ID(supplied by UniProt)']
dbid2name = db_vocab.get(['DrugBank ID', 'Common name']).dropna().set_index('DrugBank ID').to_dict()['Common name']

def add_col(df, dct, source, sink):
    missing = set()
    df[sink] = ''
    for idx, data in df.iterrows(): 
        if data[source] in dct: 
            df.at[idx,sink] = dct[data[source]]
        else: 
            df.at[idx,sink] = float("nan")
            missing.add(data[source])
    #print('missing: {}'.format(len(missing)))
    return df

df_carrier = add_col(df_carrier, up2ncbi, 'UniProt ID', 'NCBIGeneID')
df_enzyme = add_col(df_enzyme, up2ncbi, 'UniProt ID', 'NCBIGeneID')
df_target = add_col(df_target, up2ncbi, 'UniProt ID', 'NCBIGeneID')
df_transporter = add_col(df_transporter, up2ncbi, 'UniProt ID', 'NCBIGeneID')

def drugbank2edges(df, relation): 
    db = []
    for idx, data in df.iterrows(): 
        drugs = data['Drug IDs'].split('; ')
        for drug in drugs: 
            info = {
                'DrugBank':drug, 'relation':relation,
                'NCBIGeneID':data['NCBIGeneID'],
                'UniProtName':data['Name'],
                'UniProtID': data['UniProt ID'], 
            }
            db.append(info)
    return db

db = []
db.extend(drugbank2edges(df_carrier, 'carrier'))
db.extend(drugbank2edges(df_enzyme, 'enzyme'))
db.extend(drugbank2edges(df_target, 'target'))
db.extend(drugbank2edges(df_transporter, 'transporter'))
df_prot_drug = pd.DataFrame(db)
df_prot_drug = add_col(df_prot_drug, dbid2name, 'DrugBank', 'DrugBankName')

df_prot_drug.to_csv('../data/drugbank/drug_protein.csv', index=False)


