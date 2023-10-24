"""
export_to_json.py

Script for exporting pickle to a json file. Json will be of the following format:

{
    'label_1': {
        'named_entity_1': [sentence_1, sentence_2, ...],
        'named_entity_2': [sentence_1, sentence_2, ...],
        ...
    },
    ...
}

"""
from argparse_utils import input_str, output_str
import itertools
import argparse
import json
import spacy
import pickle


def main(args):
    input_path = args.input_path
    output_path = args.output_path
    output_name = args.output_name

    # handling case where path does not end in "/"
    if output_path[-1] != "/":
        output_name = "/" + args.output_name

    doc = pickle.load(open(f"{input_path}", "rb"))
    skip_labels = set(["CARDINAL", "DATE", "TIME", "ORDINAL", "LANGUAGE", "QUANTITY", "MONEY", "GPE", "NORP", "EVENT", "FAC", "LOC", "PERCENT", "LAW"])

    data = {}

    for ent in doc.ents:
        if (ent.label_ not in skip_labels):
            if ent.label_ not in data:
                data[str(ent.label_)] = {}

            label_data = data[str(ent.label_)]
            if ent.text not in label_data:
                label_data[ent.text] = []

            label_data[ent.text].append(ent.sent.text)


    with open(f"{output_path}{output_name}.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4, separators=(',', ': '))




if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='export_to_json',
                                     usage='%(prog)s [options] path',
                                     description='Script for exporting named entity data to a json file')


    parser.add_argument('-i', '--input_path',
                           metavar='<input path>',
                           type=input_str,
                           required=True,
                           help='The path to the book pickle file')

    parser.add_argument('-o', '--output_path',
                           metavar='<output path>',
                           type=output_str,
                           required=True,
                           help='The path to the output the json')

    parser.add_argument('-n', '--output_name',
                           metavar='<filename>',
                           type=str,
                           required=True,
                           help='''The name of the file to output (don\'t include extension).
                                   Output will be in the format /output_path/<output_name>.json''')

    args = parser.parse_args()
    main(args)
