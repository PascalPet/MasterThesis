import pickle
import json
import csv


# print(labelEmbeddings[3])

def precision(y_true, y_pred):
    """
    Calculate precision for multi-label classification.

    Parameters:
    - y_true: list, true labels (shape: [n_samples])
    - y_pred: list, predicted labels (shape: [n_samples])

    Returns:
    - precision: float, precision score
    """
    true_positives = sum(label in y_pred for label in y_true)
    predicted_positives = len(y_pred)
    precision = true_positives / predicted_positives if predicted_positives > 0 else 0
    return precision


def recall(y_true, y_pred):
    """
    Calculate recall for multi-label classification.

    Parameters:
    - y_true: list, true labels (shape: [n_samples])
    - y_pred: list, predicted labels (shape: [n_samples])

    Returns:
    - recall: float, recall score
    """
    true_positives = sum(label in y_pred for label in y_true)
    actual_positives = len(y_true)
    recall = true_positives / actual_positives if actual_positives > 0 else 0
    return recall


def accuracy(y_true, y_pred):
    """
    Calculate accuracy for multi-label classification.

    Parameters:
    - y_true: list, true labels (shape: [n_samples])
    - y_pred: list, predicted labels (shape: [n_samples])

    Returns:
    - accuracy: float, accuracy score
    """
    correct_predictions = sum(label in y_pred for label in y_true)
    union_pred_true = len(list(set(y_true + y_pred)))
    accuracy = correct_predictions / union_pred_true if union_pred_true > 0 else 0
    return accuracy


def calculate_metrics(project_descriptions):
    sum_precision = sum_recall = sum_accuracy = 0
    for i in range(len(project_descriptions)):
        project = project_descriptions[i]
        true_labels = project['resarch_areas']
        predicted_labels = project['result']
        filtered_predicted_labels = [x['Label'] for x in predicted_labels]
        sum_precision += precision(true_labels, filtered_predicted_labels)
        sum_recall += recall(true_labels, filtered_predicted_labels)
        sum_accuracy += accuracy(true_labels, filtered_predicted_labels)
    avg_precision = sum_precision / (i + 1)
    avg_recall = sum_recall / (i + 1)
    avc_accuracy = sum_accuracy / (i + 1)
    return avg_precision, avg_recall, avc_accuracy


thresholds = [round(x, 2) for x in [i * 0.05 for i in range(1, 21)]]
results = []
for threshold in thresholds:
    with open('../serialization/finishedData/doc_relative/all-mpnet-base-v2_doc_relative_threshold'
              + str(threshold) + '.pickle', 'rb') as pkl:
        labelEmbeddings = pickle.load(pkl)

    result = calculate_metrics(labelEmbeddings)
    results.append({
        'threshold': threshold,
        'precision': result[0],
        'recall': result[1],
        'accuracy': result[2]
    })

with open('metric_values/all-mpnet-base-v2_doc_relative_threshold.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=4)

#
# print("Precision:", precision_score)
# print("Recall:", recall_score)
# print("Accuracy:", accuracy_score)
