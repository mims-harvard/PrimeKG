# PRIMARY DATA RESOURCE RETRIEVAL AND PROCESSING
# 2023-07-08
# Ayush Noori, Zitnik Lab
# anoori@college.harvard.edu

# This script downloads and processes the primary data resources used in the PrimeKG knowledge graph.
# Run this script from the datasets directory. Links have been updated to current versions as of 2023-07-08.

# Navigate to appropriate folder.
cd /n/data1/hms/dbmi/zitnik/lab/users/an252/PrimeKG/datasets

# Make required directories, if they don't already exist.
echo "Making required directories..."
mkdir data 
cd data
mkdir bgee ctd disgenet drugbank vocab drugcentral ncbigene go hpo mondo reactome sider uberon umls
cd ..

# GENE NAMES
# Using curl, we download gene names from https://www.genenames.org/download/custom/.
# We select the columns ()"Approved symbol", "Approved name", "Accession numbers", "RefSeq IDs", "NCBI Gene ID", "NCBI Gene ID(supplied by NCBI)", "UniProt ID(supplied by UniProt)", "OMIM ID(supplied by OMIM)"). See command below.
curl "https://www.genenames.org/cgi-bin/download/custom?col=gd_app_sym&col=gd_app_name&col=gd_pub_acc_ids&col=gd_pub_refseq_ids&col=gd_pub_eg_id&col=md_eg_id&col=md_prot_id&col=md_mim_id&status=Approved&hgnc_dbtag=on&order_by=gd_app_sym_sort&format=text&submit=submit" -o data/vocab/gene_names.csv

# BGEE
# Database: Bgee, Script: bgee.py, Output: anatomy_gene.csv
echo "Downloading and processing BGEE data..."
curl https://www.bgee.org/ftp/current/download/calls/expr_calls/Homo_sapiens_expr_advanced.tsv.gz -o data/bgee/Homo_sapiens_expr_advanced.tsv.gz
gunzip data/bgee/Homo_sapiens_expr_advanced.tsv.gz
cd processing_scripts
python bgee.py
cd ..

# COMPARATIVE TOXICOGENOMICS DATABASE
# Database: Comparative Toxicogenomics Database, Script: ctd.py, Output: exposure_data.csv
echo "Downloading and processing Comparative Toxicogenomics Database data..."
curl https://ctdbase.org/reports/CTD_exposure_events.csv.gz -o data/ctd/CTD_exposure_events.csv.gz
gunzip data/ctd/CTD_exposure_events.csv.gz
cd processing_scripts
python ctd.py
cd ..

# DISGENET
# Database: DisGeNET, Script: -, Output: curated_gene_disease_associations.tsv
echo "Downloading and processing DisGeNET data..."
curl https://www.disgenet.org/static/disgenet_ap1/files/downloads/curated_gene_disease_associations.tsv.gz -o data/disgenet/curated_gene_disease_associations.tsv.gz
gunzip data/disgenet/curated_gene_disease_associations.tsv.gz

# DRUGBANK
# Several files will need to be downloaded manually after authentication at go.drugbank.com.
# Here, we assume that those files have been placed at /n/data1/hms/dbmi/zitnik/lab/datasets/2023-07-DrugBank/data.
# Modify this directory to suit your purposes.

# Database: DrugBank, Script: drugbank_drug_drug.py, Output: drug_drug.csv
echo "Downloading and processing DrugBank drug-drug interaction data..."
cp /n/data1/hms/dbmi/zitnik/lab/datasets/2023-07-DrugBank/data/drugbank_all_full_database.xml.zip data/drugbank/drugbank_all_full_database.xml.zip
unzip data/drugbank/drugbank_all_full_database.xml.zip -d data/drugbank
rm data/drugbank/drugbank_all_full_database.xml.zip

# Database: DrugBank, Script: parsexml_drugbank.ipynb, Parsed_feature.ipynb, Output: 12 drug feature files
echo "Parsing DrugBank feature data..."
# TODO: run Parsed_feature.ipynb.

# Database: DrugBank, Script: drugbank_drug_protein.py, Output: drug_protein.csv
echo "Downloading and processing DrugBank drug-protein interaction data..."

# Get data for all carrier polypeptides.
cp /n/data1/hms/dbmi/zitnik/lab/datasets/2023-07-DrugBank/data/drugbank_all_carrier_polypeptide_ids.csv.zip data/drugbank/drugbank_all_carrier_polypeptide_ids.csv.zip
unzip data/drugbank/drugbank_all_carrier_polypeptide_ids.csv.zip -d data/drugbank/drugbank_all_carrier_polypeptide_ids.csv
rm data/drugbank/drugbank_all_carrier_polypeptide_ids.csv.zip

# Get data for all enzyme polypeptides.
cp /n/data1/hms/dbmi/zitnik/lab/datasets/2023-07-DrugBank/data/drugbank_all_enzyme_polypeptide_ids.csv.zip data/drugbank/drugbank_all_enzyme_polypeptide_ids.csv.zip
unzip data/drugbank/drugbank_all_enzyme_polypeptide_ids.csv.zip -d data/drugbank/drugbank_all_enzyme_polypeptide_ids.csv
rm data/drugbank/drugbank_all_enzyme_polypeptide_ids.csv.zip

# Get data for all target polypeptides.
cp /n/data1/hms/dbmi/zitnik/lab/datasets/2023-07-DrugBank/data/drugbank_all_target_polypeptide_ids.csv.zip data/drugbank/drugbank_all_target_polypeptide_ids.csv.zip
unzip data/drugbank/drugbank_all_target_polypeptide_ids.csv.zip -d data/drugbank/drugbank_all_target_polypeptide_ids.csv
rm data/drugbank/drugbank_all_target_polypeptide_ids.csv.zip

# Get data for all transporter polypeptides.
cp /n/data1/hms/dbmi/zitnik/lab/datasets/2023-07-DrugBank/data/drugbank_all_transporter_polypeptide_ids.csv.zip data/drugbank/drugbank_all_transporter_polypeptide_ids.csv.zip
unzip data/drugbank/drugbank_all_transporter_polypeptide_ids.csv.zip -d data/drugbank/drugbank_all_transporter_polypeptide_ids.csv
rm data/drugbank/drugbank_all_transporter_polypeptide_ids.csv.zip

# Get DrugBank vocabulary.
cp /n/data1/hms/dbmi/zitnik/lab/datasets/2023-07-DrugBank/data/drugbank_all_drugbank_vocabulary.csv.zip data/vocab/drugbank_all_drugbank_vocabulary.csv.zip
unzip data/vocab/drugbank_all_drugbank_vocabulary.csv.zip -d data/vocab/
mv "data/vocab/drugbank vocabulary.csv" data/vocab/drugbank_vocabulary.csv
rm data/vocab/drugbank_all_drugbank_vocabulary.csv.zip
## TODO: figure out where vocab/drugbank_atc_codes.csv comes from.

# Using curl, we download the mapping between NCBI Entrez IDs and UniProt IDs from https://www.genenames.org/download/custom/.
# We select only those two columns, and only entries with 'Approved' status. See command below.
curl "https://www.genenames.org/cgi-bin/download/custom?col=md_eg_id&col=md_prot_id&status=Approved&hgnc_dbtag=on&order_by=gd_app_sym_sort&format=text&submit=submit" -o data/vocab/gene_map.csv

# Run the script to get the drug-protein interactions.
cd processing_scripts
python drugbank_drug_protein.py
cd ..

# DRUG CENTRAL

# Database: Drug Central, Script: drugcentral_queries.txt, Output: drug_disease.csv
curl "https://unmtid-shinyapps.net/download/drugcentral.dump.05102023.sql.gz" -o data/drugcentral/drugcentral.dump.05102023.sql.gz
gunzip data/drugcentral/drugcentral.dump.05102023.sql.gz

# Initialize the PostgreSQL database.
module load postgresql/15.2
rm -rf /n/data1/hms/dbmi/zitnik/lab/users/an252/PrimeKG/datasets/data/drugcentral/db
initdb -D /n/data1/hms/dbmi/zitnik/lab/users/an252/PrimeKG/datasets/data/drugcentral/db
pg_ctl -D /n/data1/hms/dbmi/zitnik/lab/users/an252/PrimeKG/datasets/data/drugcentral/db -l logfile start
# Server should now be started! Check with:
pg_isready
# Create the Drug Central database.
createdb drugcentral
psql drugcentral < drugcentral.dump.05102023.sql
psql -d drugcentral -c "SELECT DISTINCT * FROM structures RIGHT JOIN (SELECT * FROM omop_relationship WHERE relationship_name IN ('indication', 'contraindication', 'off-label use')) AS drug_disease ON structures.id = drug_disease.struct_id;" -P format=csv -o drug_disease.csv

# Database: Drug Central, Script: drugcentral_feature.Rmd, Output: dc_features.csv
# TODO: run drugcentral_feature.Rmd.

# ENTREZ GENE
# Database: Entrez Gene, Script: ncbigene.py, Output: protein_go_associations.csv
curl https://ftp.ncbi.nlm.nih.gov/gene/DATA/gene2go.gz -o data/ncbigene/gene2go.gz
gunzip data/ncbigene/gene2go.gz
cd processing_scripts
python ncbigene.py
cd ..

# Database: Gene Ontology, Script: go.py, Output: go_terms_info.csv, go_terms_relations.csv
curl -L http://purl.obolibrary.org/obo/go/go-basic.obo -o data/go/go-basic.obo
cd processing_scripts
python go.py
cd ..

# Database: Human Phenotype Ontology, Script: hpo.py, hpo_obo_parser.py, Output: hp_terms.csv, hp_parents.csv, hp_references.csv
# Use the -L flag to follow all redirects.
curl -L http://purl.obolibrary.org/obo/hp.obo -o data/hpo/hp.obo
cd processing_scripts
python hpo.py
cd ..

# Database: Human Phenotype Ontology, Script: hpoa.py, Output: disease_phenotype_pos.csv, disease_phenotype_neg.csv
curl -L http://purl.obolibrary.org/obo/hp/hpoa/phenotype.hpoa -o data/hpo/phenotype.hpoa
cd processing_scripts
python hpoa.py
cd ..

# Database: MONDO, Script: mondo.py, mondo_obo_parser.py, Output: mondo_terms.csv, mondo_parents.csv, mondo_references.csv, mondo_subsets.csv, mondo_definitions.csv
curl -L http://purl.obolibrary.org/obo/MONDO.obo -o data/mondo/mondo.obo
cd processing_scripts
python mondo.py
cd ..

# Database: Reactome, Script: reactome.py, Output: reactome_ncbi.csv, reactome_terms.csv, reactome_relations.csv
curl https://reactome.org/download/current/ReactomePathways.txt -o data/reactome/ReactomePathways.txt
curl https://reactome.org/download/current/ReactomePathwaysRelation.txt -o data/reactome/ReactomePathwaysRelation.txt
curl https://reactome.org/download/current/NCBI2Reactome.txt -o data/reactome/NCBI2Reactome.txt
cd processing_scripts
python reactome.py
cd ..

# Database: SIDER, Script: sider.py, Output: sider.csv
curl http://sideeffects.embl.de/media/download/meddra_all_se.tsv.gz -o data/sider/meddra_all_se.tsv.gz
gunzip data/sider/meddra_all_se.tsv.gz
curl http://sideeffects.embl.de/media/download/drug_atc.tsv -o data/sider/drug_atc.tsv
cd processing_scripts
python sider.py
cd ..

# Database: UBERON, Script: uberon.py, Output: uberon_terms.csv, uberon_rels.csv, uberon_is_a.csv
curl -L http://purl.obolibrary.org/obo/uberon/ext.obo -o data/uberon/ext.obo
cd processing_scripts
python uberon.py
cd ..

# Database: UMLS, Script: umls.py, map_umls_mondo.py, Output: umls_mondo.csv
# The UMLS Metathesaurus will need to be downloaded manually after authentication at uts.nlm.nih.gov.
# Here, we assume that the files have been placed at /n/data1/hms/dbmi/zitnik/lab/users/yeh803/PLM/raw_data/umls.
# Modify this directory to suit your purposes.
cp /n/data1/hms/dbmi/zitnik/lab/users/yeh803/PLM/raw_data/umls/umls-2023AA-metathesaurus-full.zip data/umls/umls-2023AA-metathesaurus-full.zip
unzip data/umls/umls-2023AA-metathesaurus-full.zip -d data/umls/
cp data/umls/2023AA/META/MRCONSO.RRF data/umls/MRCONSO.RRF
cd processing_scripts
python umls.py
python map_umls_mondo.py
cd ..

# If needed, copy processed UMLS files back to original source.
# cp data/umls/umls.csv /n/data1/hms/dbmi/zitnik/lab/users/yeh803/PLM/raw_data/umls/umls.csv
# cp data/vocab/umls_mondo.csv /n/data1/hms/dbmi/zitnik/lab/users/yeh803/PLM/raw_data/umls/umls_mondo.csv

# Database: UMLS, Script: umls.ipynb, Output: umls_def_disorder_2021.csv, umls_def_disease_2021.csv
# TODO: run umls.ipynb.

# In preparation for building the knowledge graph, create a directory for the output files.
# Copy PPI data manually.
mkdir data/kg
mkdir data/kg/auxillary
mkdir data/ppi