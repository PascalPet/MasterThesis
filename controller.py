from cos_sim_and_ranking.DocumentBased import *
from thresholds.Thresholds import *
from serialization.serialize_deserialize import *
import pickle


def get_labels_by_absolute_threshold(threshold, project_description):
    for i in range(len(project_description)):
        result = absolute_threshold(threshold, project_description[i]['ranking'])
        project_description[i]['result'] = result
    return project_description


def get_labels_by_relative_threshold(multiplier, project_description):
    for i in range(len(project_description)):
        result = relative_threshold(multiplier, project_description[i]['ranking'])
        project_description[i]['result'] = result
    return project_description


def get_document_based_absolute_threshold(threshold):
    project_descriptions_with_ranking = get_cossim()
    doc_with_calculated_labels = get_labels_by_absolute_threshold(threshold, project_descriptions_with_ranking)
    serialize_results('doc_absolute_threshold_' + str(threshold), doc_with_calculated_labels)

    print('doc_absolute_threshold_' + str(threshold) + ' saved... ')


def get_document_based_relative_threshold(multiplier):
    projects_with_ranking = get_cossim()
    doc_with_calculated_labels = get_labels_by_relative_threshold(multiplier, projects_with_ranking)
    serialize_results('doc_relative_threshold' + str(multiplier), doc_with_calculated_labels)

    print('doc_relative_threshold' + str(multiplier) + ' saved...')


def calculate_doc_based_with_array_of_absolute_threshold(thresholds):
    for threshold in thresholds:
        get_document_based_absolute_threshold(threshold)


def calculate_doc_based_with_array_of_relative_thresholds(multiplier):
    for multi in multiplier:
        get_document_based_relative_threshold(multi)


def run_all():
    thresholds = [0.2, 0.15, 0.1]
    multiplier = [0.95, 0.9, 0.85]
    #calculate_doc_based_with_array_of_absolute_threshold(thresholds)
    calculate_doc_based_with_array_of_relative_thresholds(multiplier)


run_all()

# a = deserialize_results('doc_absolute_threshold_15.0')
# print(a[0])
# loop different approaches
# loop different encodings includes cossim and ranking
# loop different thresholds
# METRIC
