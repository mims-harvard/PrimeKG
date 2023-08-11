import pandas as pd 


def get_omim_info(data,info=None,output_type='list'):
    if info:
        entries = []
        for i in range(len(data['omim'])):
            mim = data['omim'][i]['entry']['mimNumber']
            if info in data['omim'][i]['entry'].keys():
                entries.append((str(mim),data['omim'][i]['entry'][info]))

        if output_type == 'df':
            out = pd.DataFrame(entries,columns=['mimNumber',info]).set_index(['mimNumber']) # ,'Content'
        elif output_type == 'dict':
            out = dict(entries)
        elif output_type == 'list':
            out = entries

        return out
    else:
        all_keys = {k for i in range(len(data['omim'])) for k in data['omim'][i]['entry'].keys()}
        
        print('select one of these:')
        print('')
        for k in sorted(all_keys):
            print(f'\t{k}')


def get_omim_phenotype_info(data,info=None):
    entries = get_omim_info(
        data,
        'phenotypeMapList',
        output_type='dict'
    )
    
    if info:
        out = [
            (mim,phe['phenotypeMap'][info]) 
            for mim,phe_list in entries.items() for phe in phe_list if info in phe['phenotypeMap'].keys()
        ]

        out = pd.DataFrame(out,columns=['mimNumber',info]).drop_duplicates().sort_values(info).reset_index(drop=True)
        
        return out
    else:
        all_keys = {k for mim,phe_list in entries.items() 
                    for phe in phe_list for k in phe['phenotypeMap'].keys()
                   }
        print('select one of these:')
        print('')
        for k in sorted(all_keys):
            print(f'\t{k}')
