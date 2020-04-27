import sys
import json
import argparse
sys.path.insert(0, 'src')
from etl import get_data, filter_recode, pca, logistic_regression

DATA_PARAMS = 'config/data-params.json'
TEST_PARAMS = 'config/test-params.json'

def load_params(fp):
    with open(fp) as fh:
        param = json.load(fh)
    return param

cfg = load_params(TEST_PARAMS)

parser = argparse.ArgumentParser(description='PCA and visualization with Plink2')
parser.add_argument('process', type=str, nargs=1, help='the process to deal with')
args = parser.parse_args()

if args.process[0]=="get_data":
    cfg = load_params(DATA_PARAMS)
    get_data(cfg['files'], 'data/')
elif args.process[0]=="filter":
    filter_recode(cfg['filename'], cfg['covar_file'], cfg['data_dir'], cfg['filter_output'], cfg['hwe'], cfg['maf'], cfg['geno'], cfg['mind'], cfg['chr'], cfg['min'])
elif args.process[0]=='pca':
    pca(cfg['data_dir'], cfg['filter_output'])
elif args.process[0]=='logistic':
    logistic_regression(cfg['data_dir'])