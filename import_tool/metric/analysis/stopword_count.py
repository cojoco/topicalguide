


metric_name = 'Stopword Count'

def compute_metric(database_id, dataset_db, analysis_db):
    count = analysis_db.stopwords.count()
    return [{'analysis': analysis_db, 'value': count }]
