import shlex
import subprocess as sp
import os

def filter_recode(input_file, covar_file, data_dir, filename, hwe, maf, geno, mind, chr_, min_):
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    # check_sex
    cmd = shlex.split(("plink2 --file {}/{} --check-sex --gplink --out {}/check_sex --recode").format(data_dir, input_file, data_dir))
    sp.call(cmd)
    # filter: covar, hwe, maf, geno, mind, chr, min
    cmd = shlex.split(("plink2 --file {}/check_sex --covar {}/{} --hwe {} --maf {} --geno {} --mind {} --chr {} --min {} --genome --gplink --out {}/{} --recode").format(data_dir, data_dir, covar_file, hwe, maf, geno, mind, chr_ , min_, data_dir, filename))
    sp.call(cmd)
    
def pca(data_dir, input_file):
    cmd = shlex.split(("plink2 --file {}/{} --gplink --out {}/pca --pca var-wts --recode").format(data_dir, input_file, data_dir))
    sp.call(cmd)