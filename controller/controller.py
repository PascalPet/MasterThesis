from cos_sim_and_ranking.DocumentBased import *
from thresholds.Thresholds import *
from serialization.serialize_deserialize import *
import pickle


def get_labels_by_absolute_threshold(threshold, project_description):
    for i in range(len(project_description)):  # len(project_description)
        result = absolute_threshold(threshold, project_description[i]['ranking'])
        project_description[i]['result'] = result
    return project_description


def get_labels_by_relative_threshold(multiplier, project_description):
    for i in range(len(project_description)):  # len(project_description)
        result = relative_threshold(multiplier, project_description[i]['ranking'])
        project_description[i]['result'] = result
    return project_description


def compute_and_serialize_absolute_threshold(threshold, projects_with_ranking = None):
    languagemodel = 'all-mpnet-base-v2'
    projects_with_ranking = get_cossim_document_based('Document_embedding_' + languagemodel)  # #auslagern
    doc_with_calculated_labels = get_labels_by_absolute_threshold(threshold, projects_with_ranking)
    serialize_results(languagemodel + '_doc_absolute_threshold' + str(threshold), doc_with_calculated_labels)
    print('doc_absolute_threshold_' + str(threshold) + ' saved... ')


def compute_and_serialize_relative_threshold(multiplier, projects_with_ranking = None):
    languagemodel = 'all-mpnet-base-v2'
    projects_with_ranking = get_cossim_document_based('Document_embedding_' + languagemodel)  # auslagern
    #print(projects_with_ranking[10])
    doc_with_calculated_labels = get_labels_by_relative_threshold(multiplier, projects_with_ranking)
    serialize_results(languagemodel + '_doc_relative_threshold' + str(multiplier), doc_with_calculated_labels)
    print('doc_relative_threshold' + str(multiplier) + ' saved...')


def calculate_doc_based_with_array_of_absolute_threshold(thresholds):
    for threshold in thresholds:
        compute_and_serialize_absolute_threshold(threshold)


def calculate_doc_based_with_array_of_relative_thresholds(multiplier):
    for multi in multiplier:
        compute_and_serialize_relative_threshold(multi)


def print_one_project(doc_name, index):
    projects = deserialize_results(doc_name)
    for res in projects[index]['result']:
        print(res)


def run_all():
    thresholds = [round(x, 2) for x in [i * 0.05 for i in range(1, 21)]] #0.05, 0.1 ..
    calculate_doc_based_with_array_of_absolute_threshold(thresholds)
    #calculate_doc_based_with_array_of_relative_thresholds(multiplier)


# run
run_all()

# print_one_project('doc_absolute_threshold_0.1', 1)
