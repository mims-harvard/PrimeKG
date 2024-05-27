# PrimeKG
----

[![website](https://img.shields.io/badge/website-live-brightgreen)](https://zitniklab.hms.harvard.edu/projects/PrimeKG/)
[![GitHub Repo stars](https://img.shields.io/github/stars/mims-harvard/PrimeKG)](https://github.com/mims-harvard/PrimeKG/stargazers)
[![GitHub Repo forks](https://img.shields.io/github/forks/mims-harvard/PrimeKG)](https://github.com/mims-harvard/PrimeKG/network/members)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

[**Lab Website**](https://zitniklab.hms.harvard.edu/projects/PrimeKG/) | [**Nature Publication**](https://www.nature.com/articles/s41597-023-01960-3) | [**Harvard Dataverse**](https://doi.org/10.7910/DVN/IXA7BM)

## TL;DR
**Precision Medicine Knowledge Graph (PrimeKG)** presents a holistic view of diseases. PrimeKG integrates 20
high-quality biomedical resources to describe 17,080 diseases with 4,050,249 relationships representing ten major
biological scales. We accompany PrimeKG’s graph structure with text descriptions of clinical guidelines for drugs and
diseases to enable multimodal analyses. Download [this CSV file](https://dataverse.harvard.edu/api/access/datafile/6180620)
to get started!

## News and Updates
- [Dec 2023] PrimeKG is extended to improve coverage of OMIM data.
  
    <details><summary>Details:</summary>

    ### December 2023 update
  
    In December 2023, an updated version of PrimeKG that includes complete entries from the Online Mendelian Inheritance in Man
    (OMIM) database in a standardized data format was prepared.

    #### Changes to PrimeKG
    As discussed in [issue #9](https://github.com/mims-harvard/PrimeKG/issues/9), OMIM phenotypes and genes were
    not fully included in prior versions of PrimeKG. For more details, see 
    [this pull request](https://github.com/mims-harvard/PrimeKG/pull/12).
    
    To extend of PrimeKG using a new data source and include edges between existing nodes in the knowledge graph,
    we devised a standardized data format (see [PR#207](https://github.com/mims-harvard/TDC/pull/207) in mims-harvard/TD)
    that is used for all data sources in the same format as the published PrimeKG edge list.
    
    #### Summary
    * `datasets/processing_scripts/omim_tools.py` script contains functions to process OMIM data. 
    * `datasets/omim/` folder should store OMIM datasets.
    * `datasets/omim/omim-api.ipynb` notebook is the OMIM API wrapper, which is used to download OMIM entries (note that
      an API key is required).
    * `knowledge_graph/append_omim.ipynb` notebook is used to append OMIM entries to PrimeKG. 
    * `scripts/utils.py` includes scripts that are used across multiple data sources.
    
    #### OMIM Database
    Many of the OMIM phenotype entries have been already included in the PrimeKG through MONDO; however, there still exists
    OMIM information that was not included in the PrimeKG. Thus, we add scripts and notebooks to cover OMIM genes, 
    phenotypes, and phenotypic series (see [here](https://www.omim.org/help/faq#1_13)) entries, and enable regular updates.

    #### NCBI Gene
    * OMIM gene entries are linked to NCBI Gene entries via new edges in the KG.
    
    #### Human Phenotype Ontology
    * HPO-OMIM edges are added to PrimeKG.
    
    #### MONDO
    * MONDO-OMIM edges are added to PrimeKG.
    
    #### Statistics
    
    New nodes and edges added:
    ```text
    # of new edges: 612282
    # of new node: 32866
    ```
    
    Updated edge count by `display_relation`:
    ```text
    display_relation
    associated with    581387
    linked to           26784
    members              4111
    ```

    Updated edge_count by `relation`:
    ```text
    relation
    mim_disease                        9599
    mim_gene                          16636
    mim_phenotype                    574128
    mim_phenotypic_series              4111
    mim_phenotypic_series_disease       549
    phenotype_map                      7259
    ```

  </details>

- [July 2023] PrimeKG construction scripts are updated to include primary source data releases up to July 2023. Note that the files published on Harvard DataVerse remain unchanged; however, we provide new scripts and updated links should users wish to build their own current version of PrimeKG.
  
    <details><summary>Details:</summary>

    ### July 2023 update
    
    In July 2023, this repository was updated to rebuild PrimeKG and update the knowledge graph to include database releases up to July 2023. Note that the files published on Harvard DataVerse remain unchanged; however, we provide new scripts and updated links should users wish to build their own current version of PrimeKG. For more details, see [this pull request](https://github.com/mims-harvard/PrimeKG/pull/11).
    
    17 scripts `datasets/processing_scripts/` are re-run or updated to build a new version of PrimeKG, while `datasets/feature_construction/` scripts may remain out-of-date. Re-run or updated primary data sources include Bgee, Comparative Toxicogenomics Database, DisGeNET, DrugBank, DrugCentral, NCBI Gene, Gene Ontology, Human Phenotype Ontology, MONDO, Reactome, SIDER, UBERON, and UMLS. 
    
    For more information, see `datasets/primary_data_resources.sh`. Changes include the following:
    
    #### General
    Created script to automatically create directory structure, pull data, and run all necessary processing and feature extraction steps.
    * Fixed broken environment construction script.
    * Script automatically creates required directories.
    * Added commands to retrieve gene names, details, and NCBI ID to UniProt ID mapping from [www.genenames.org](http://www.genenames.org/), then output to `vocab/gene_names.csv` and `vocab/gene_map.csv`.

    #### Bgee
    * 58405/5257181 gold quality calls with expression rank < 25000 now specify cell type in a particular tissue (_e.g._, UBERON:0000473 ∩ CL:0000089, which denotes germ line stem cell in testis).
    * These rows are dropped in `bgee.py`.
    * URL updated to [here](https://www.bgee.org/ftp/current/download/calls/expr_calls/Homo_sapiens_expr_advanced.tsv.gz).
    
    #### Comparative Toxicogenomics Database
    * URL updated to [here](https://ctdbase.org/reports/CTD_exposure_events.csv.gz).
    
    #### DisGeNET
    * No changes needed.
    
    #### DrugBank
    * Fixed paths in `parsexml_drugbank.py`. Output to new `/parsed` subdirectory. Removed extraneous lines in `Parsed_feature.ipynb`.
    * :white_check_mark: Successfully ran `drugbank_drug_drug.py` and `drugbank_drug_protein.py`.
    * :warning: `parsexml_drugbank.py` and `Parsed_feature.ipynb` may need updates.
    
    #### DrugCentral
    * Modified `drugcentral_queries.txt` to work on O2, the Harvard Medical School high-performance computing cluster.
    * :warning:  `drugcentral_feature.Rmd` may need updates.
    
    #### NCBI Gene
    * No changes needed.
    
    #### Gene Ontology
    * Used `-L` flag to follow redirects. No other changes needed.
    
    #### Human Phenotype Ontology
    * Used `-L` flag to follow redirects. No other changes needed to `hpo.py`.
    * Updated `hpoa.py` to replace old column names with new column names.
    
    #### MONDO
    * Added check for NoneType values in external references (line 29).
    
    #### Reactome
    * No changes needed.
    
    #### SIDER
    * No changes needed.
    
    #### UBERON
    * Checked for NA values, dropped two obsolete terms (UBERON:0039300 and UBERON:0039302) not marked as obsolete in the source file.
    
    #### UMLS
    * UMLS data pulled and  paths updated for 2023 data.
    * :warning: `umls.ipynb` may need updates.
    </details>
  
- [Feb 2023] PrimeKG is [published](https://www.nature.com/articles/s41597-023-01960-3) in Nature Scientific Data. 
- [Jun 2022] PrimeKG crosses 5,000 downloads on Harvard Dataverse! 
- [Apr 2022] PrimeKG is live on [bioRxiv](https://www.biorxiv.org/content/10.1101/2022.05.01.489928v1) and [Harvard Dataverse](https://doi.org/10.7910/DVN/IXA7BM)!


## Table of Contents
- [Unique Features of PrimeKG](#unique-features-of-primekg)
- [Environment Setup](#environment-setup)
- [Using PrimeKG](#using-primekg)
- [Building an updated PrimeKG](#building-an-updated-primekg)
- [Data Server](#data-server)
- [Citing PrimeKG](#citing-primekg)
- [License](#license)


## Unique Features of PrimeKG
 
- *Diverse coverage of diseases*: PrimeKG contains over 17,000 diseases including rare dieases. Disease nodes in PrimeKG are densely connected to other nodes in the graph and have been optimized for clinical relevance in downstream precision medicine tasks. 
- *Heterogeneous knowledge graph*: PrimeKG contains over 100,000 nodes distributed over various biological scales as depicted below. PrimeKG also contains over 4 million relationships between these nodes distributed over 29 types of edges.
- *Multimodal integration of clinical knowledge*: Disease and drug nodes in PrimeKG are augmented with clinical descriptors that come from medical authorities such as Mayo Clinic, Orphanet, Drug Bank, and so forth. 
- *Ready-to-use datasets*: PrimeKG is minimally dependent on external packages. Our knowledge graph can be retrieved in a ready-to-use format from Harvard Dataverse.
- *Data functions*: PrimeKG provides extensive data functions, including processors for primary resources and scripts to build an updated knowledge graph.

<p align="center"><img src="https://github.com/mims-harvard/PrimeKG/blob/main/fig/schematic.png" alt="overview" width="600px" /></p>

<p align="center"><img src="https://github.com/mims-harvard/PrimeKG/blob/main/fig/PrimeKG-example.png" alt="PrimeKG-example"/></p>

## Environment setup

### Using `pip`

To install the dependencies required to run the PrimeKG code, use `pip`:

```bash
pip install -r updated_requirements.txt
```

### Or use `conda`

```bash
conda env create --name PrimeKG --file=environment.yml
```

## Using PrimeKG

For a quick start in Python, you can download the raw data files in `.csv` format directly from [Harvard Dataverse](https://doi.org/10.7910/DVN/IXA7BM) or load PrimeKG using the following community dataloaders.

### Getting started in Python

Download PrimeKG from Harvard Dataverse using the following bash command. You can replace `kg.csv` with any file path. 
```bash
wget -O kg.csv https://dataverse.harvard.edu/api/access/datafile/6180620
```
You can use the following code to load PrimeKG and visualize its data. 
```python
import pandas as pd
primekg = pd.read_csv('kg.csv', low_memory=False)
primekg.query('y_type=="disease"|x_type=="disease"')
```

### Dataloader: Therapeutics Data Commons 
[website](https://tdcommons.ai) | [docs](https://github.com/mims-harvard/TDC)
```bash
pip install PyTDC
```
```python
from tdc.resource import PrimeKG
data = PrimeKG(path = './data')
drug_feature = data.get_features(feature_type = 'drug')
data.to_nx()
data.get_node_list(type = 'disease')
```

### Dataloader: PyKEEN 
[website](https://github.com/pykeen/pykeen) | [docs](https://pykeen.readthedocs.io/en/latest/api/pykeen.datasets.PrimeKG.html)
```
pip install pykeen
```
```python
import pykeen.datasets
pykeen.datasets.has_dataset('primekg')
```

## Building an updated PrimeKG

### Downloading primary data resources

All persistent identifiers and weblinks to download the 20 primary data resources used to build PrimeKG are systematically provided in the Data Records section of our article. We have also mentioned the exact filenames that were downloaded from each resource for easy corroboration. 

### Curating primary data resources

We provide the scripts used to process all primary data resources and the names of the resulting output files generated by those scripts. We would be happy to share the intermediate processing datasets that were used to create PrimeKG on request. 

| Database                            | Processing scripts                            | Expected script output                                                                             |
|-------------------------------------|-----------------------------------------------|----------------------------------------------------------------------------------------------------|
| Bgee                                | bgee.py                                       | anatomy_gene.csv                                                                                   |
| Comparative Toxicogenomics Database | ctd.py                                        | exposure_data.csv                                                                                  |
| DisGeNET                            | -                                             | curated_gene_disease_associations.tsv                                                              |
| DrugBank                            | drugbank_drug_drug.py                         | drug_drug.csv                                                                                      |
| DrugBank                            | parsexml_drugbank.ipynb, Parsed_feature.ipynb | 12 drug feature files                                                                              |
| DrugBank                            | drugbank_drug_protein.py                      | drug_protein.csv                                                                                   |
| Drug Central                        | drugcentral_queries.txt                       | drug_disease.csv                                                                                   |
| Drug Central                        | drugcentral_feature.Rmd                       | dc_features.csv                                                                                    |
| Entrez Gene                         | ncbigene.py                                   | protein_go_associations.csv                                                                        |
| Gene Ontology                       | go.py                                         | go_terms_info.csv, go_terms_relations.csv                                                          |
| Human Phenotype Ontology            | hpo.py, hpo_obo_parser.py                     | hp_terms.csv, hp_parents.csv, hp_references.csv                                                    |
| Human Phenotype Ontology            | hpoa.py                                       | disease_phenotype_pos.csv, disease_phenotype_neg.csv                                               |
| MONDO                               | mondo.py,  mondo_obo_parser.py                | mondo_terms.csv, mondo_parents.csv, mondo_references.csv, mondo_subsets.csv, mondo_definitions.csv |
| OMIM                                | omim_tools.py, omim-api.ipynb                 | mim2gene.txt, mimTitles.txt, genemap2.txt, morbidmap.txt, <omim_full_path>.json                    |
| Reactome                            | reactome.py                                   | reactome_ncbi.csv, reactome_terms.csv, reactome_relations.csv                                      |
| SIDER                               | sider.py                                      | sider.csv                                                                                          |
| UBERON                              | uberon.py                                     | uberon_terms.csv, uberon_rels.csv, uberon_is_a.csv                                                 |
| UMLS                                | umls.py, map_umls_mondo.py                    | umls_mondo.csv                                                                                     |
| UMLS                                | umls.ipynb                                    | umls_def_disorder_2021.csv, umls_def_disease_2021.csv                                              |

### Harmonizing datasets into PrimeKG

The code to harmonize datasets and construct PrimeKG is available at `build_graph.ipynb`. Simply run this jupyter notebook in order to construct the knowledge graph from the outputs of the processing files mentioned above. This jupyter notebook produces all three versions of PrimeKG, `kg_raw.csv`, `kg_giant.csv`, and the complete version  `kg.csv`. 

[//]: # (### Building extended version of PrimeKG)

### Feature extraction

The code required to engineer features can be found at `engineer_features.ipynb` and `mapping_mayo.ipynb`. 

## Citing PrimeKG

If you find PrimeKG useful, cite our work:
```
@article{chandak2022building,
  title={Building a knowledge graph to enable precision medicine},
  author={Chandak, Payal and Huang, Kexin and Zitnik, Marinka},
  journal={Nature Scientific Data},
  doi={https://doi.org/10.1038/s41597-023-01960-3},
  URL={https://www.nature.com/articles/s41597-023-01960-3},
  year={2023}
}
```

## Data Server

PrimeKG is hosted on [Harvard Dataverse](https://doi.org/10.7910/DVN/IXA7BM) with the following persistent
identifier [https://doi.org/10.7910/DVN/IXA7BM](https://doi.org/10.7910/DVN/IXA7BM). When Dataverse is under
maintenance, PrimeKG datasets cannot be retrieved. That happens rarely; please check the status on
[the Dataverse website](https://dataverse.harvard.edu/).

## License
PrimeKG codebase and associated tools are released under the MIT license. Please note that this license specifically refers to the PrimeKG software, and is distinct from any licenses governing the PrimeKG dataset itself. For individual dataset usage, refer to the respective dataset licenses available on data website.
