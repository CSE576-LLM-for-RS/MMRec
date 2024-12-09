# coding: utf-8
# @email: enoche.chow@gmail.com

"""
Main entry
# UPDATED: 2022-Feb-15
##########################
"""

import os
import argparse
from utils.quick_inference import quick_inference
os.environ['NUMEXPR_MAX_THREADS'] = '48'


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--model', '-m', type=str, default='SELFCFED_LGN', help='name of models')
    parser.add_argument('--dataset', '-d', type=str, default='baby', help='name of datasets')
    parser.add_argument('--mg', type=str, default=None, help='some description for mg')  # Add this line
    config_dict = {
        'gpu_id': 0,
    }

    args, _ = parser.parse_known_args()

    quick_inference(model=args.model, dataset=args.dataset, config_dict=config_dict, save_model=True, mg=args.mg)


