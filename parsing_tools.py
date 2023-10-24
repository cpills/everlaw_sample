import re


"""
Simple function for removing any matches of a regex from a given text
"""
def remove_tags(passage, regex):
    passage = re.sub(regex, '', passage)
    return passage
