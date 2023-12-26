from sklearn.metrics import precision_score, recall_score, f1_score

def compute_f1(expected_ids, predicted_ids):
    precision = precision_score(expected_ids, predicted_ids, average='micro')
    recall = recall_score(expected_ids, predicted_ids, average='micro')
    
    # Compute F1 score
    f1 = f1_score(expected_ids, predicted_ids, average='micro')
    
    return f1