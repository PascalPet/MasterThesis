from cos_sim_and_ranking.DocumentBased import *
from cos_sim_and_ranking.K_SentenceBased import *
from thresholds.Thresholds import *
from serialization.serialize_deserialize import *
from cos_sim_and_ranking.K_WordBased import *
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


def compute_and_serialize_absolute_threshold(threshold, projects_with_ranking, languagemodel, k):
    doc_with_calculated_labels = get_labels_by_absolute_threshold(threshold, projects_with_ranking)
    serialize_results(languagemodel + '_' + str(k) + '_doc_absolute_threshold' + str(threshold),
                      doc_with_calculated_labels)
    print('doc_absolute_threshold_' + str(threshold) + ' saved... ')


def compute_and_serialize_relative_threshold(multiplier, projects_with_ranking, languagemodel, k):
    doc_with_calculated_labels = get_labels_by_relative_threshold(multiplier, projects_with_ranking)
    serialize_results(languagemodel + '_' + str(k) + '_word_relative_threshold' + str(multiplier),
                      doc_with_calculated_labels)
    print('doc_relative_threshold' + str(multiplier) + ' saved...')


def calculate_doc_based_with_array_of_absolute_threshold(thresholds, project_descriptions, languagemodel, k):
    for threshold in thresholds:
        compute_and_serialize_absolute_threshold(threshold, project_descriptions, languagemodel, k)


def calculate_doc_based_with_array_of_relative_thresholds(multiplier, project_descriptions, languagemodel, k):
    for multi in multiplier:
        compute_and_serialize_relative_threshold(multi, project_descriptions, languagemodel, k)


def print_one_project(doc_name, index):
    projects = deserialize_results(doc_name)
    print(projects[2])
    for res in projects[index]['result']:
        print(res)


def run_all():
    languagemodel = 'all-mpnet-base-v2'
    #for k in range(1, 7):
    projects_with_ranking = get_cossim_document_based('100_Document_embedding_' + languagemodel)  # auslagern
    #projects_with_ranking = get_cossim_sentence_based(str(k) + '_Sentence_Embeddings_all-mpnet-base-v2')
    #projects_with_ranking = get_cossim_word_based(str(k) + '_Word_Embeddings_all-mpnet-base-v2')

    thresholds = [0.25]  # 0.05, 0.1 ..
    calculate_doc_based_with_array_of_absolute_threshold(thresholds, projects_with_ranking, languagemodel, 100)
    #calculate_doc_based_with_array_of_relative_thresholds(thresholds, projects_with_ranking, languagemodel, k)


# run
#run_all()

print_one_project('all-mpnet-base-v2_100_doc_absolute_threshold0.25', 99)
