from ebooklib import epub
from bs4 import BeautifulSoup
from parsing_tools import remove_tags
from argparse_utils import input_str, output_str
import itertools
import argparse

def main(args):
    input_path = args.input_path
    output_path = args.output_path
    output_name = args.output_name

    # handling case where path does not end in "/"
    if output_path[-1] != "/":
        output_name = "/" + args.output_name

    book = epub.read_epub(input_path)

    output_file = open(f"{output_path}{output_name}.txt", "w")

    # first 6 sections are title, table of contents, copy, etc.
    for it in itertools.islice(book.get_items(), 6, 12):

        soup = BeautifulSoup(it.get_body_content(), "html.parser")
        print(it)
        print("*" * 20)

        string_soup = str(soup)

        # removing <p> and </p> tags
        string_soup = remove_tags(string_soup, r"<p class=\"\w*\">")
        string_soup = remove_tags(string_soup, r"<\/p>")

        # removing <span> and </span> tags
        string_soup = remove_tags(string_soup, r"<span>|<span class=\"\w*\">")
        string_soup = remove_tags(string_soup, r"<\/span>")

        # removing <a> and </a> tags (used for page numbers)
        string_soup = remove_tags(string_soup, r"<a id=\"page_[0-9]+\">")
        string_soup = remove_tags(string_soup, r"<\/a>")

        # removing <i> and </i> tags (used for italics)
        string_soup = remove_tags(string_soup, r"<i>")
        string_soup = remove_tags(string_soup, r"<\/i>")

        # removing <b/> (breaks)
        string_soup = remove_tags(string_soup, r"<br/>")

        string_soup = remove_tags(string_soup, r"<img alt=\"image\" src=\"images\/ufig_[0-9]+.jpg\"/>")

        string_soup = remove_tags(string_soup, r"<small>")
        string_soup = remove_tags(string_soup, r"<\/small>")

        output_file.write(string_soup)

    output_file.close()



if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='clean_book_1',
                                     usage='%(prog)s [options] path',
                                     description='Script for cleaning epub of any tags. Writes to cleaned text to a file')


    parser.add_argument('-i', '--input_path',
                           metavar='<input path>',
                           type=input_str,
                           required=True,
                           help='The path to the book 1 epub file')

    parser.add_argument('-o', '--output_path',
                           metavar='<output path>',
                           type=output_str,
                           required=True,
                           help='The path to the output location for the cleaned text')

    parser.add_argument('-n', '--output_name',
                           metavar='<filename>',
                           type=str,
                           required=True,
                           help='''The name of the file to output (don\'t include extension).
                                   Output will be in the format /output_path/<output_name>.txt''')

    args = parser.parse_args()
    main(args)
