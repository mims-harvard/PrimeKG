import gzip
import json
from time import time


def read_data(jsonfilename):
    t0 = time()
    if '.gz' in jsonfilename:
        with gzip.open(jsonfilename, 'r') as fin:        # 4. gzip
            json_bytes = fin.read()                      # 3. bytes (i.e. UTF-8)
        json_str = json_bytes.decode('utf-8')            # 2. string (i.e. JSON)
        data = json.loads(json_str)                      # 1. data
    else:
        f = open(jsonfilename, 'r')
        data = json.load(f)
    print("done in %0.3fs" % (time() - t0))
    return data


def read_gmt(gmt):
    with open(gmt) as genesets:
        genesets_dict = {
            line.strip().split("\t")[0]: line.strip().split("\t")[2:]
            for line in genesets.readlines()
        }
    return genesets_dict


def write_data(data, filename, verbose=False):
    t0 = time()
    if verbose:
        print (len(data))
        
    dicobj = json.dumps(data).encode('utf-8') # outputs in bytes format
    
    # alternatively, to save the file
    with open(filename, 'wb+') as file:
        file.write(dicobj)
        file.close()
    
    print("done in %0.3fs" % (time() - t0))
