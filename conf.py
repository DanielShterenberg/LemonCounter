import os
import pickle

CHUNK_SIZE = 4 * 1024 * 1024
DATA_FILE = "data.pkl"


def get_allowed_mime_types():
    allowed_mime_types = ['text/plain']
    return allowed_mime_types


def get_number_of_cores_to_use():
    cores = os.cpu_count()
    return cores


def save_counters(word_counter):
    with open(DATA_FILE, 'wb') as f:
        pickle.dump(word_counter, f, pickle.HIGHEST_PROTOCOL)


def load_counters():
    with open(DATA_FILE, 'rb') as f:
        return pickle.load(f)
