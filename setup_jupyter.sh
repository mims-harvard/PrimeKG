#!/bin/bash
module load gcc/9.2.0 cuda/11.7 python/3.9.14 R/4.2.1 git/2.9.5
conda deactivate
source primeKG_env/bin/activate
jupyter notebook --port=54321 --browser='none'