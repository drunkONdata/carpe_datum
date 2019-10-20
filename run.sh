#!/bin/bash
echo args: "$@"

gsutil -q cp $1 input.csv

python3 run.py input.csv

cat results