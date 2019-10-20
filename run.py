#!/usr/bin/env python

from pathlib import Path
import sys
import argparse
import datetime
import pprint
import pandas as pd
from google.cloud import storage
from impute_suite import *
from flask import Flask, request, jsonify


app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
    push = request.get_json()
    if not push:
        msg = 'no Pub/Sub message received'
        return f'Bad Request: {msg}', 400

    if not isinstance(push, dict) or 'message' not in push:
        msg = 'invalid Pub/Sub message format'
        return f'Bad Request: {msg}', 400

    pubsub_message = push['message']
    bucket_name = pubsub_message["bucket"],
    file_name = pubsub_message["name"]
    
    outfilenames = main(bucket_name, file_name)

    if len(outfilenames) > 0:
        response = {
            "output": outfilenames
        }
        return jsonify(response)
    else:
        return ('Could not process {filename}'.format(
            filename= file_name), 400)

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
