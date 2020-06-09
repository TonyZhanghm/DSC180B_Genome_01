# DSC180B_Genome_Project -- GWAS on Alzheimer’s Disease

### Tony Zhang, Zhuoyuan Ren, Haoshu Qin

Visualization Website: https://tonyzhanghm.github.io/adgwas_website/

## Introduction

## Usage

### Environment (Docker)
Docker images: https://hub.docker.com/repository/docker/tonyzhanghm/genetics

### Commands
Clone the repo: `git clone https://github.com/TonyZhanghm/DSC180B_Genome_01.git`

To run the whole experiment: `python run.py test-project`

To run the project step by step: `python run.py` with following flags:
`get_data`: download the raw data/ tools needed and store them in `data/`.   
`filter`: filter the dataset with [PLINK 1.9](https://www.cog-genomics.org/plink/). The specific parameter choices could be found in the paper.    
`pca`: run principal component analysis with [PLINK 1.9](https://www.cog-genomics.org/plink/).  
`plot_pca`: plot first 5 principal components and store the result in `data/output/`.  
`plot_eigenval`: plot the scree plot.   
`logistic`: run the association test with logistic regression.   
`manhattan`: plot the manhattan plot with [bioinfokit](https://reneshbedre.github.io//blog/howtoinstall.html).  
`regional`: plot regional plots for the nine genes.   
`qqplot`: plot a qqplot on the test result.  
`meta`: run metal analysis with [METAL](https://genome.sph.umich.edu/wiki/METAL_Documentation).  

## Checkpoint-1
- Request data from source: UK Biobank and NIAGADS
- Understand the analysis methods: meta analysis, Manhattan plot, regional association plot. 
- Write a survey of the data you are using, the relationship and appropriateness of the data to the problem under examination, and the context in which the data was created.
- Summarize relevant details of the data generating process, describing the population that the data represents, whether that population is relevant to the question at hand, while addressing possible questions of data reliability.
- Understand how to use population stratification on our data so that it can apply to other races besides European descent.
- no new code added

## Checkpoint-2
- Describe the source of the backup dataset, the population that the data represents, whether that population is relevant to the question at hand, while addressing possible questions of data reliability. (Scott)
- Perform preprocessing quality controls using Plink commands (Jared, Tony)
- Statistically assess the quality of the data (Tony)
- EDA (Barplot, PCA, Scatter matrix plot, Scree Plot) (All)
- Perform multi-covariate association analysis with logistic regression (Tony)

