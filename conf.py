import os

CHUNK_SIZE = 4 * 1024 * 1024


def get_allowed_mime_types():
    allowed_mime_types = ['text/plain']
    return allowed_mime_types


def get_number_of_cores_to_use():
    cores = os.cpu_count()
    return cores
