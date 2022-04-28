# PrimeKG
----

[![website](https://img.shields.io/badge/website-live-brightgreen)](TODO_add_url_here)
[![GitHub Repo stars](https://img.shields.io/github/stars/mims-harvard/PrimeKG)](https://github.com/mims-harvard/PrimeKG/stargazers)
[![GitHub Repo stars](https://img.shields.io/github/forks/mims-harvard/PrimeKG)](https://github.com/mims-harvard/PrimeKG/network/members)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

[**Website**](TODO_add_url_here) | [**Arxiv Paper**](TODO_add_url_here) | [**Harvard Dataverse**](https://doi.org/10.7910/DVN/IXA7BM)

**Precision Medicine Knowledge Graph (PrimeKG)** TODO is the first unifying framework to systematically access, evaluate, and benchmark machine learning methods across the entire range of therapeutics. TDC supports the development of novel ML methods and theory, with a strong bent towards developing the foundations of which ML algorithms are most suitable for drug discovery applications and why.

The collection of curated AI/ML-ready datasets, AI/ML tasks, and benchmarks in TDC serves as a meeting point for domain and machine learning scientists. We envision that TDC can considerably accelerate ML model development, validation and transition into biomedical and clinical implementation.

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
- PrimeKG is live on [arXiv](https://arxiv.org/abs/2102.09548) and [Harvard Dataverse](https://doi.org/10.7910/DVN/IXA7BM)!

## Unique Features of PrimeKG
 
- TODO *Diverse areas of therapeutics development*: TDC covers a wide range of learning tasks, including target discovery, activity screening, efficacy, safety, and manufacturing across biomedical products, including small molecules, antibodies, and vaccines.
- TODO
- *Ready-to-use datasets*: PrimeKG is minimally dependent on external packages. Our knowledge graph can be retrieved in a ready-to-use format from Harvard Dataverse.
- *Data functions*: PrimeKG provides extensive data functions, including processors for primary resources and scripts to build an updated knowledge graph.
- *Open-source initiative*: PrimeKG is an open-source initiative. If you want to get involved, let us know. 

<p align="center"><img src="https://raw.githubusercontent.com/mims-harvard/TDC/master/fig/tdc_overview.png" alt="overview" width="600px" /></p>

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

## Tutorials

We provide a tutorial to help you get started with PrimeKG! It will help you load the knowledge graph into ... TODO

## Building an updated PrimeKG

#### Downloading primary data resources

#### Curating primary data resources

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

#### Harmonizing datasets into PrimeKG

The code to harmonize datasets and construct the knowledge graph is available at  \emph{build\_graph.ipynb}. Simply run this jupyter notebook in order to construct the knowledge graph form the outputs of the processing files mentioned above. This script produces all three versions of PrimeKG, `kg_raw.csv`, `kg_giant.csv`, and the complete version  `kg.csv`.

#### Feature extraction

The code required to engineer features can be found at \emph{engineer\_features.ipynb} and \emph{mapping\_mayo.ipynb}.

<!-- 
## Design of TDC

TDC has a unique three-tiered hierarchical structure, which to our knowledge, is the first attempt at systematically organizing machine learning for therapeutics. We organize TDC into three distinct *problems*. For each problem, we give a collection *learning tasks*. Finally, for each task, we provide a series of *datasets*.

In the first tier, after observing a large set of therapeutics tasks, we categorize and abstract out three major areas (i.e., problems) where machine learning can facilitate scientific advances, namely, single-instance prediction, multi-instance prediction, and generation:

* Single-instance prediction `single_pred`: Prediction of property given individual biomedical entity.
* Multi-instance prediction `multi_pred`: Prediction of property given multiple biomedical entities. 
* Generation `generation`: Generation of new desirable biomedical entities.

<p align="center"><img src="https://raw.githubusercontent.com/mims-harvard/TDC/master/fig/tdc_problems.png" alt="problems" width="500px" /></p>

The second tier in the TDC structure is organized into learning tasks. Improvement on these tasks can result in numerous applications, including identifying personalized combinatorial therapies, designing novel class of antibodies, improving disease diagnosis, and finding new cures for emerging diseases.

Finally, in the third tier of TDC, each task is instantiated via multiple datasets. For each dataset, we provide several splits of the dataset into training, validation, and test sets to simulate the type of understanding and generalization (e.g., the model's ability to generalize to entirely unseen compounds or to granularly resolve patient response to a polytherapy) needed for transition into production and clinical implementation.

#### Dataset Splits

To retrieve the training/validation/test dataset split, you could simply type
```python 
data = X(name = Y)
data.get_split(seed = 42)
# {'train': df_train, 'val': df_val, 'test': df_test}
```
You can specify the splitting method, random seed, and split fractions in the function by e.g. `data.get_split(method = 'scaffold', seed = 1, frac = [0.7, 0.1, 0.2])`. Check out the [data split page](https://zitniklab.hms.harvard.edu/TDC/functions/data_split/) on the website for details.
-->
## Cite Us

If you find PrimeKG useful, cite our arxiv paper: TODO

```
@article{Huang2021tdc,
  title={Therapeutics Data Commons: Machine Learning Datasets and Tasks for Drug Discovery and Development},
  author={Huang, Kexin and Fu, Tianfan and Gao, Wenhao and Zhao, Yue and Roohani, Yusuf and Leskovec, Jure and Coley, 
          Connor W and Xiao, Cao and Sun, Jimeng and Zitnik, Marinka},
  journal={Proceedings of Neural Information Processing Systems, NeurIPS Datasets and Benchmarks},
  year={2021}
}
```

## Data Server

PrimeKG is hosted on [Harvard Dataverse](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/21LKWG) with the following persistent identifier [https://doi.org/10.7910/DVN/IXA7BM](https://doi.org/10.7910/DVN/IXA7BM). When Dataverse is under maintenance, PrimeKG datasets cannot be retrieved. That happens rarely; please check the status on [the Dataverse website](https://dataverse.harvard.edu/).

## License
PrimeKG codebase is under MIT license. For individual dataset usage, please refer to the dataset license found in the website.
