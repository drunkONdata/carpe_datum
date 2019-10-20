#!/usr/bin/env python

from pathlib import Path
import argparse
import datetime
import pprint
import pandas as pd
from google.cloud import storage
from impute_suite import *

def download_blob(bucket_name, source_blob_name, destination_file_name):
    """Downloads a blob from the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(source_blob_name)

    blob.download_to_filename(destination_file_name)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Impute missing values from .csv')
    parser.add_argument('infile', type=Path, help='.csv file from which to impute missing values')

    args = parser.parse_args()

    outfilenames = main("input.csv")

    with open("results", "w") as results:
        for outfilename in outfilenames:
            results.write(outfilename + "\n")
