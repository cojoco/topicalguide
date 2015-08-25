from __future__ import division, print_function, unicode_literals
import sys
sys.path.insert(0, 'import_tool/dataset/interfaces')
from generic_dataset import GenericDataset
from json_dataset import JsonDataset
from random_dataset import RandomDataset

datasets = {
    'Generic': GenericDataset,
    'JSON': JsonDataset,
    'Random': RandomDataset,
}
