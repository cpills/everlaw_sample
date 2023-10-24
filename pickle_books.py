"""
pickle_books.py


Script for generating a spaCy model for a specific text and then pickling them.
Takes a path to the text to read from, a path to write the pickle to, a name
for the output file, and a type of spaCy model to use.

Run `python3 pickle_books.py -h` for more information
"""
import spacy
import pickle
import argparse
from argparse_utils import input_str, output_str, model_str

def main(args):
    input_path = args.input_path
    output_path = args.output_path
    output_name = args.output_name
    model = args.model

    nlp = spacy.load(f'en_core_web_{model}')
    nlp.max_length = 2500000 # testing this value, default is 1000000

    file_text = open(input_path).read()
    doc = nlp(file_text)
    pickle.dump(doc, open(f'{output_path}{output_name}.pickle', "wb"))
    print(f"Finished generating {output_name}.pickle")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='pickle_books',
                                     usage='%(prog)s [options] path',
                                     description='Script for generating a pickle binary of a text')


    parser.add_argument('-i', '--input_path',
                           metavar='<input path>',
                           type=input_str,
                           required=True,
                           help='The path to the input text')

    parser.add_argument('-o', '--output_path',
                           metavar='<output path>',
                           type=output_str,
                           required=True,
                           help='The path to the output location for the pickle')

    parser.add_argument('-n', '--output_name',
                           metavar='<filename>',
                           type=str,
                           required=True,
                           help='''The name of the pickle file to output (don\'t include extension).
                                   Output will be in the format /output_path/<output_name>.pickle''')

    parser.add_argument('-m', '--model',
                           metavar='<model>',
                           type=model_str,
                           required=True,
                           help='''The spaCy model to use (english). Available options are \'sm\', \'md\',
                                   \'lg\', and \'trf\'. For more information on the models,
                                   visit https://spacy.io/models/en''')

    args = parser.parse_args()
    main(args)
