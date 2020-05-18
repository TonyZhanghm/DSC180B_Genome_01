import shlex
import subprocess as sp
import os
from bioinfokit import analys, visuz
import pandas as pd

def logistic_regression(data_dir, how = 'pca1'):
    if how == 'pca1':
        cmd = shlex.split(("plink2 --adjust --allow-no-sex --ci .95 --covar {}/pca.eigenvec --covar-number 1 --file {}/pca --gplink --logistic --out {}/pca1 --recode").format(data_dir, data_dir, data_dir))
        sp.call(cmd)
        
def plot_manhattan(file, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    df = pd.read_table(file, delim_whitespace=True)
    visuz.marker.mhat(df=df, chr='CHR',pv='P',gwas_sign_line=True, dim=(15,10))
    os.rename("manhatten.png", output_dir+"manhattan.png")
    

def regional_manhattan(df, gene, chromo, start, end, gap=500000):
    
    def set_color(pos, start, end, gene):
        if pos<start:
            return 'AALeft'
        elif pos>end:
            return 'ZRight'
        return gene
    temp=df[(df['BP'].astype(int)>(int(start)-gap)) & (df['BP'].astype(int)<(int(end)+gap)) & (df['CHR']==chromo)]
    
    temp['color'] = temp['BP'].apply(lambda x: set_color(x, start, end, gene))
    visuz.marker.mhat(df=temp, chr='color',pv='P', gwas_sign_line=True, dim=(15,10), axxlabel='{} (Chromosome {})'.format(gene, str(chromo)), dotsize=10)
    
    
def plot_regional_manhattan(file, gene_csv, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    df = pd.read_table(file, delim_whitespace=True)
    genes = pd.read_csv(gene_csv)
    for i, row in genes.iterrows():
        regional_manhattan(df, row['gene'], row['chr'], row['start'], row['end'])
        os.rename("manhatten.png", output_dir+"{}.png".format(row['gene'].replace('/', '_')))