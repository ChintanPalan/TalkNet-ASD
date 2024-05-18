"""
Pickle2JSON is a simple Python Command Line program for converting Pickle file to JSON file.

Arguments: Only one (1) argument is expected which is the pickle file.
Usage: python pickle2json.py myfile.pkl
Output: The output is a JSON file bearing the same filename containing the JSON document of the converted Pickle file.
"""

# import libraries
import pickle
import json
import sys
import os


def custom_converter(obj):
    """ Convert special float values to strings and recurse for iterable objects. """
    if isinstance(obj, float):
        if obj != obj:  # Checks for NaN
            return "NaN"
        elif obj == float('inf'):
            return "Infinity"
        elif obj == float('-inf'):
            return "-Infinity"
    elif isinstance(obj, dict):
        return {k: custom_converter(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [custom_converter(v) for v in obj]
    return obj  # Return the object itself if not a special float case

# open pickle file
with open(sys.argv[1], 'rb') as infile:
    obj = pickle.load(infile)

converted_obj = custom_converter(obj)

# convert pickle object to json object
json_obj = json.loads(json.dumps(converted_obj, default=str))
# write the json file
with open(
        os.path.splitext(sys.argv[1])[0] + '.json',
        'w',
        encoding='utf-8'
    ) as outfile:
    json.dump(json_obj, outfile, ensure_ascii=False, indent=4)
