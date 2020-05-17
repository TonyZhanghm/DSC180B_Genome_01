import shlex
import subprocess as sp
import os

def logistic_regression(data_dir, how = 'pca1'):
    if how == 'pca1':
        cmd = shlex.split(("plink2 --adjust --allow-no-sex --ci .95 --covar {}/pca.eigenvec --covar-number 1 --file {}/pca --gplink --logistic --out {}/pca1 --recode").format(data_dir, data_dir, data_dir))
        sp.call(cmd)