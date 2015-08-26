
from collections import OrderedDict
from visualize.models import TopicMetricValue
#~ import alpha
#~ import attribute_entropy
#~ import coherence
#~ import sentiment
#~ import subset_document_entropy
#~ import subset_token_count
from . import token_count
from . import type_count

from sys import path
path.insert(0,'import_tool/metric/topic')
from . import document_entropy
from . import word_entropy
from . import temperature


database_table = TopicMetricValue
metrics = OrderedDict([
    #~ ('alpha', alpha), 
    #~ ('attribute_entropy', attribute_entropy), 
    #~ ('coherence', coherence), 
    #~ ('sentiment', sentiment), 
    #~ ('subset_document_entropy', subset_document_entropy), 
    #~ ('subset_token_count', subset_token_count), 
    ('token_count', token_count), 
    ('type_count', type_count), 
    ('document_entropy', document_entropy), 
    ('word_entropy', word_entropy), 
    ('temperature', temperature), 
])

def metric_exists(database_id, dataset_db, analysis_db, metric_db):
    return TopicMetricValue.objects.using(database_id).filter(topic__analysis=analysis_db, metric=metric_db).exists()
