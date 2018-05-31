import numpy as np
import json

def save_hyper(feat_type, add_bias, lr, reg_const):
    '''
    Saves the parameters tuned for different sub-problems of the assignment into a file.
    This file is later used for evaluation purposes.
    '''
    
    prob_dict = dict()
    prob_dict['add_bias'] = add_bias
    prob_dict['lr'] = lr
    prob_dict['reg_const'] = reg_const

    filename = 'hyper_param.json'
    
    try:
        with open(filename, 'r') as fp:
            dict_hyper = json.load(fp)
    except:
        dict_hyper = dict()

    dict_hyper[feat_type] = prob_dict
    with open(filename, 'w') as fp:
        json.dump(dict_hyper, fp)
