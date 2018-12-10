import os
import argparse
import tempfile
import json

parser = argparse.ArgumentParser()
parser.add_argument("-k", "--key", help = "key string")
parser.add_argument("-v", "--value", help = "value of key")
args = parser.parse_args()

storage_path = os.path.join(tempfile.gettempdir(), "storage.data")

if os.path.isfile(storage_path):
    with open(storage_path, 'r') as f:
        keys = json.load(f)
else: keys = {}

if args.value:
    if args.key in keys:
        keys[args.key].append(args.value)
    else:
        keys[args.key] = [args.value]
    with open(storage_path, 'w') as f:
        json.dump(keys, f)
else:
    if args.key in keys:
        print(", ".join(val for val in keys[args.key]))
    else: print(None)

