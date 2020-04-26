import requests
import gzip
import shutil
import shlex
import subprocess as sp
import os

def download_file_from_google_drive(id, destination):
    URL = "https://docs.google.com/uc?export=download"

    session = requests.Session()

    response = session.get(URL, params = { 'id' : id }, stream = True)
    token = get_confirm_token(response)

    if token:
        params = { 'id' : id, 'confirm' : token }
        response = session.get(URL, params = params, stream = True)

    save_response_content(response, destination)    

def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value

    return None

def save_response_content(response, destination):
    CHUNK_SIZE = 32768

    with open(destination, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)

def uncompress(filename, folder):
    cmd = shlex.split(("unzip {} -d {}").format(filename, folder))
    sp.call(cmd)
    
def get_data(file_list, data_dir):
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    for file_id, filename in file_list:
        destination = data_dir+filename
        download_file_from_google_drive(file_id, destination)
        uncompress(destination, data_dir)
        
def filter_recode(input_file, covar_file, data_dir, filename, hwe, maf, geno, mind, chr_, min_):
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    # check_sex
    cmd = shlex.split(("plink2 --file {}/{} --check-sex --gplink --out {}/check_sex --recode").format(data_dir, input_file, data_dir))
    sp.call(cmd)
    # filter: covar, 
    cmd = shlex.split(("plink2 --file {}/check_sex --covar {}/{} --hwe {} --maf {} --geno {} --mind {} --chr {} --min {} --genome --gplink --out {}/{} --recode").format(data_dir, data_dir, covar_file, hwe, maf, geno, mind, chr_ , min_, data_dir, filename))
    sp.call(cmd)
    
def pca(data_dir, input_file):
    cmd = shlex.split(("plink2 --file {}/{} --gplink --out {}/pca --pca var-wts --recode").format(data_dir, input_file, data_dir))
    sp.call(cmd)
