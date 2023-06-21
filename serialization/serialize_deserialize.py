import pickle


def serialize_results(file_name, data):
    with open('../serialization/finishedData/' + file_name + '.pickle', 'wb') as pkl:
        pickle.dump(data, pkl)


def deserialize_results(file_name):
    with open('../serialization/finishedData/' + file_name + '.pickle', 'rb') as pkl:
        project_loaded = pickle.load(pkl)

    return project_loaded
