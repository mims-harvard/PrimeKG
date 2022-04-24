import os
import pandas as pd
from bs4 import BeautifulSoup

soup = BeautifulSoup(open("../data/drugbank/full database.xml"),"xml")

sep = ","
with open('interactions_edges.txt', 'w') as f:
    for drug in soup.findAll("drug"):
        drugName = drug.find("drugbank-id").text
        interactions = drug.findAll("drug-interaction")
        if not interactions:
            continue
        for i in interactions:
            toPrint = drugName + sep + i.find("drugbank-id").text + '\n'
            f.write(toPrint)
            
pd.read_csv('interactions_edges.txt', names=['drug1','drug2']).to_csv('../data/drugbank/drug_drug.csv', index=False)

os.remove('interactions_edges.txt')