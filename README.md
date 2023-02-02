# PrimeKG
----

[![website](https://img.shields.io/badge/website-live-brightgreen)](https://zitniklab.hms.harvard.edu/projects/PrimeKG/)
[![GitHub Repo stars](https://img.shields.io/github/stars/mims-harvard/PrimeKG)](https://github.com/mims-harvard/PrimeKG/stargazers)
[![GitHub Repo forks](https://img.shields.io/github/forks/mims-harvard/PrimeKG)](https://github.com/mims-harvard/PrimeKG/network/members)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

[**Website**](https://zitniklab.hms.harvard.edu/projects/PrimeKG/) | [**Publication**](https://www.nature.com/articles/s41597-023-01960-3) | [**Harvard Dataverse**](https://doi.org/10.7910/DVN/IXA7BM)

**Precision Medicine Knowledge Graph (PrimeKG)** presents a holistic view of diseases. PrimeKG integrates 20 high-quality biomedical resources to describe 17,080 diseases with 4,050,249 relationships representing ten major biological scales. We accompany PrimeKG’s graph structure with text descriptions of clinical guidelines for drugs and diseases to enable multimodal analyses.
 
<!-- 
**Invited talk at the [Harvard Symposium on Drugs for Future Pandemics (#futuretx20)](https://www.drugsymposium.org/)** [**\[Slides\]**](https://drive.google.com/file/d/11eTrh_lsqPcwu3RZRYjJGNpJ3s18YlBS/view) [**\[Video\]**](https://youtu.be/ZuCOhEZtaOw)

**Presented at [NeurIPS 2021](https://openreview.net/forum?id=8nvgnORnoWr)** [**\[Poster\]**](https://drive.google.com/file/d/1LfF8mfPLUqAVEzH3KPBxDO_VF7nLFtiJ/view?usp=sharing) / **Oral at [ELLIS ML4Molecules](https://moleculediscovery.github.io/workshop2021/)** [**\[Slides\]**](https://drive.google.com/file/d/1iOSW_5eruca4vdygDxS1H64c49oQuH40/view?usp=sharing) / **Presented at [Baylearn](https://baylearn-org.github.io/www/)** [**\[Slides\]**](https://drive.google.com/file/d/1BNpk3dOdqE3ksgyVV-V3xySdBMq-8cXL/view?usp=sharing) [**\[Poster\]**](https://drive.google.com/file/d/1LfF8mfPLUqAVEzH3KPBxDO_VF7nLFtiJ/view?usp=sharing)

**[Recording of the first TDC User Group Meetup](https://harvard.zoom.us/rec/share/HO0TjRPs56YG-Fu3i033izaTwebB4KwUhPeNURkWSI-anrH9su03lCtUlHeZG-WP.67ZJmAIHsD7Q_2GQ) (Jan 25th, 2022). [Agenda](https://shoutout.wix.com/so/d1Nv1pC2d#/main)**
 -->
 
## Updates
<!-- 
- `0.3.6`: Add a new task on TCR-Epitope Binding! See [here](https://tdcommons.ai/multi_pred_tasks/tcrepitope/)!
- `0.3.5`: 1. Add hERG central dataset 2. Add ChEMBL V29 3. Fixed reaction type issue for USPTO-50 4. Fix bug on higher order multi-instance prediction cold-split! More information, see [here](https://tdcommons.ai/news/)!
- `0.3.4`: Bug fixes on docking oracles, KL divergence measure, see commit [0f7121a](https://github.com/mims-harvard/TDC/commit/0f7121a3bd7cb833fb55441054d7d87ff3c4ebd6) and commit [6e46fbd](https://github.com/mims-harvard/TDC/commit/6e46fbd1a946b3a6b9f7ba456d60dc09480c68b9)!
- `0.3.3`: Extended support on cold split - now you can split based on multiple entities, see [#127](https://github.com/mims-harvard/TDC/pull/127)!
- `0.3.2`: Bug fixes - Adding support for harmonizing same DTIs with different affinities (KIBA, DAVIS Updated accordingly, see [#98](https://github.com/mims-harvard/TDC/issues/98)). Support label name retrieval for TWOSIDES ([#121](https://github.com/mims-harvard/TDC/issues/121)), and add gene symbol info to GDSC ([#12t2](https://github.com/mims-harvard/TDC/issues/122)). 
- `0.3.1`: We have restructured the codebase to be contributor-friendly! Checkout the TDC documentation at [https://tdc.readthedocs.io](https://tdc.readthedocs.io/)!
- TDC paper is accepted to [NeurIPS 2021 Datasets and Benchmarks](https://openreview.net/pdf?id=8nvgnORnoWr)
- `0.2.0`: Release docking molecule generation benchmark! Checkout [here](https://tdcommons.ai/benchmark/docking_group/overview/)!
- `0.1.9`: Support molecule filters! Checkout [here](https://tdcommons.ai//functions/data_process/#molecule-filters)!
- `0.1.8`: Streamlined and simplified the leaderboard programming frameworks! Now, you can submit a result for a single dataset! Checkout [here](https://tdcommons.ai/benchmark/overview/)!
 -->
- [Feb 2023] PrimeKG is [published](https://www.nature.com/articles/s41597-023-01960-3) in Nature Scientific Data. 
- [Jun 2022] PrimeKG crosses 5,000 downloads on Harvard Dataverse! 
- [Apr 2022] PrimeKG is live on [bioRxiv](https://www.biorxiv.org/content/10.1101/2022.05.01.489928v1) and [Harvard Dataverse](https://doi.org/10.7910/DVN/IXA7BM)!


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
pip install -r requirements.txt
```

### Or use `conda`

```bash
conda env create --name PrimeKG --file=environments.yml
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
primekg.query('node_type=="disease"')
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

| Database  | Processing scripts       | Expected script output        |
|-----------|--------------------------|----------------------|
Bgee  | bgee.py  | anatomy_gene.csv 
Comparative Toxicogenomics Database   | ctd.py  | exposure_data.csv
DisGeNET   | -    | curated_gene_disease_associations.tsv
DrugBank   | drugbank_drug_drug.py   | drug_drug.csv
DrugBank   | parsexml_drugbank.ipynb, Parsed_feature.ipynb | 12 drug feature files 
DrugBank   | drugbank_drug_protein.py   | drug_protein.csv
Drug Central   | drugcentral_queries.txt   | drug_disease.csv
Drug Central   | drugcentral_feature.Rmd   | dc_features.csv
Entrez Gene | ncbigene.py | protein_go_associations.csv 
Gene Ontology | go.py | go_terms_info.csv, go_terms_relations.csv 
Human Phenotype Ontology | hpo.py, hpo_obo_parser.py | hp_terms.csv, hp_parents.csv, hp_references.csv
Human Phenotype Ontology | hpoa.py | disease_phenotype_pos.csv, disease_phenotype_neg.csv
MONDO | mondo.py,  mondo_obo_parser.py | mondo_terms.csv, mondo_parents.csv, mondo_references.csv, mondo_subsets.csv, mondo_definitions.csv
Reactome | reactome.py | reactome_ncbi.csv, reactome_terms.csv, reactome_relations.csv
SIDER | sider.py | sider.csv
UBERON | uberon.py | uberon_terms.csv, uberon_rels.csv, uberon_is_a.csv
UMLS | umls.py, map_umls_mondo.py | umls_mondo.csv
UMLS | umls.ipynb | umls_def_disorder_2021.csv, umls_def_disease_2021.csv

### Harmonizing datasets into PrimeKG

The code to harmonize datasets and construct PrimeKG is available at `build_graph.ipynb`. Simply run this jupyter notebook in order to construct the knowledge graph from the outputs of the processing files mentioned above. This jupyter notebook produces all three versions of PrimeKG, `kg_raw.csv`, `kg_giant.csv`, and the complete version  `kg.csv`. 

### Feature extraction

The code required to engineer features can be found at `engineer_features.ipynb` and `mapping_mayo.ipynb`. 

## Cite Us

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

PrimeKG is hosted on [Harvard Dataverse](https://doi.org/10.7910/DVN/IXA7BM) with the following persistent identifier [https://doi.org/10.7910/DVN/IXA7BM](https://doi.org/10.7910/DVN/IXA7BM). When Dataverse is under maintenance, PrimeKG datasets cannot be retrieved. That happens rarely; please check the status on [the Dataverse website](https://dataverse.harvard.edu/).

## License
PrimeKG codebase is under MIT license. For individual dataset usage, please refer to the dataset license found in the website.
