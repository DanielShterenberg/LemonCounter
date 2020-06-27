import io
import logging
import mimetypes
import multiprocessing as mp
import os
import re
import time

import urllib3

from conf import get_allowed_mime_types, get_number_of_cores_to_use, CHUNK_SIZE


# Example: "data": "Hi! My name is (what?), my name is (who?), my name is sliky Slim Shady"
def count_words_from_string(word_counter, raw_data):
    update_counters(word_counter, raw_data)


# example: "https://www.w3.org/TR/PNG/iso_8859-1.txt"
def count_words_from_url(word_counter, url):
    http = urllib3.PoolManager()
    r = http.request('GET', url, preload_content=False)
    r.__class__ = ExplicitlyClosedHttpResponse
    for line in io.TextIOWrapper(r):
        update_counters(word_counter, line)


# Example: "../mynameis.txt"
def count_words_from_path(word_counter, path):
    logging.info("data is a path type")
    start_time = time.time()

    allowed_mime_types = get_allowed_mime_types()
    mime_type = mimetypes.guess_type(path)[0]

    if mime_type not in allowed_mime_types:
        return "Unexpected MimeType - we only support text files", 400

    parellalize_count(word_counter, path)

    end_time = time.time()
    logging.info(f"Total processing time: {end_time - start_time} ms")


def parellalize_count(word_counter, path):
    cores = get_number_of_cores_to_use()
    logging.info(f"using {cores} cores to process the file")

    pool = mp.Pool(cores)
    jobs = []

    # create jobs
    for chunk_start, chunk_size in generate_chunks(path):
        jobs.append(pool.apply_async(process_wrapper, (word_counter, path, chunk_start, chunk_size)))

    # wait for all the jobs to finish
    for job in jobs:
        job.get()

    pool.close()


def generate_chunks(path, size=CHUNK_SIZE):
    file_end = os.path.getsize(path)
    with open(path, "r+b") as f:
        chunk_end = f.tell()
        while True:
            chunk_start = chunk_end
            f.seek(size, 1)
            f.readline()

            chunk_end = f.tell()
            yield chunk_start, (chunk_end - chunk_start)
            if chunk_end > file_end:
                break


def process_wrapper(word_counter, path, chunk_start, chunk_size):
    with open(path, "r+") as f:
        f.seek(chunk_start)
        lines = f.read(chunk_size).splitlines()
        for line in lines:
            update_counters(word_counter, line)
    print(word_counter)


def update_counters(word_counter, line):
    line = filter_line(line)

    for word in re.findall(r'\w+', line):
        if word in word_counter:
            word_counter[word] += 1
        else:
            word_counter[word] = 1


def filter_line(line):
    line = re.sub(r'[^A-Za-z\s]+', ' ', line)
    return line.lower()


class ExplicitlyClosedHttpResponse(urllib3.HTTPResponse):
    @property
    def closed(self):
        return self._fp.closed
