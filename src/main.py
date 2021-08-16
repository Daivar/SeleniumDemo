import logging

logging.basicConfig(
  filename='../main.log',
  level=logging.INFO,
  format='%(asctime)s : %(levelname)s : %(name)s : %(message)s'
)
import logging
import sys

import yaml
import argparse

parser = argparse.ArgumentParser(description='Simple calculator')
parser.add_argument('--method', required=False, type=str, nargs='?', help='method to call in the program')
args = parser.parse_args()

# print(args.method)

formatter = logging.Formatter('%(asctime)s : %(name)s : %(message)s')

file_logger = logging.FileHandler('..\\logs\\main.log')
file_logger.setFormatter(formatter)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(file_logger)

with open('../config/main_config.yml') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)