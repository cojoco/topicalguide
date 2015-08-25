from __future__ import division, print_function, unicode_literals
from visualize.models import DatasetMetricValue
from collections import OrderedDict

from sys import path
path.insert(0,'import_tool/metric/dataset')
import document_count

database_table = DatasetMetricValue
metrics = OrderedDict([
    ('document_count', document_count),
])

def metric_exists(database_id, dataset_db, analysis_db, metric_db):
    return DatasetMetricValue.objects.using(database_id).filter(dataset=dataset_db, metric=metric_db).exists()
