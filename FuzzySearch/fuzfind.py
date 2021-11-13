"""
Fuzzy Search Algorithm, finds a similar string from a list.
fuzfind()
Created by Fergus Haak - 2021
 """

import Levenshtein as lev


def fuzfind(str_input: str, str_list: list[str], min_ratio: float) -> str:
    """
    Fuzzy Search Algorithm, compares a string against a list of strings.
    If the string is close enough to an item in the data. the item is returned
    ---
    str_input: A single string which will be compared.
    data: A list of string data which str_input will be compared to.
    min_ratio: (0-1) float which is minimum closeness between str_input to data.
    """
    index = 0
    most_common = 0
    for i in range(len(data)):
        commonality = lev.ratio(str_input.lower(), data[i].lower())
        if commonality > most_common:
            most_common = commonality
            index = i
    if most_common >= min_ratio:
        return data[index]
    else:
        return str_input


# test data
if __name__ == '__main__':
    data = ['Martin-Rodriguez', 'Harris, Lee and Murillo', 'Whitaker-Smith', 'Stewart-Glass', 'Henson-Avila',
            'Montoya, Thompson and Boyd', 'Caldwell-Chang', 'Oliver-Conley', 'Baker, Yu and Stokes', 'Martinez Group']
    print(fuzfind('Stwer Glasz', data, 0.2))
    print(fuzfind('Stwer Glasz', data, 0.9))
