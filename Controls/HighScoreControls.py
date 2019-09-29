import sys
import random
import json as json
import encodings.base64_codec as base64
import os


__SNAYKTON_SCORES_FILENAME = os.getcwd() + '\\snaykton_scores.score'


def __generate_high_score_list():
    names = ['Reggie', 'Mick', 'Geoff', 'Stan', 'John', 'Dennis', 'Tony', 'Pat', 'Patrick', 'Arnold', 'Joe']
    sorted_random_points = sorted([random.randint(2, 5) for _ in range(10)])
    sorted_random_points.reverse()

    # -- Create list of name-point pairs
    names_points = [[random.choice(names), points] for points in sorted_random_points]
    return names_points


def __encode_high_scores(high_score_list):
    # -- Jsonify the pairs
    high_score_list_encoded = json.dumps(high_score_list)
    # -- Pass the utf-8 encoded points to the b64 encoder - They have to first be utf-8 encoded
    high_score_list_encoded_b64 = base64.base64_encode(high_score_list_encoded.encode('utf-8'))
    return high_score_list_encoded_b64[0].decode('utf-8')


def __decode_high_scores(high_score_list_b64_encoded):
    # -- Decode with b64 framework
    high_score_list_b64_decoded = base64.base64_decode(high_score_list_b64_encoded.encode('utf-8'))
    # -- Use json.loads to create an object out of a string
    high_score_list = json.loads(high_score_list_b64_decoded[0])
    return high_score_list


def save_high_scores_to_file(high_score_list):
    try:
        with open(__SNAYKTON_SCORES_FILENAME, 'w') as snaykton_scores_file:
            snaykton_scores_file.write(__encode_high_scores(high_score_list))
            return True
    except IOError:
        return False


def load_high_scores_from_file():
    try:
        with open(__SNAYKTON_SCORES_FILENAME, 'r') as snaykton_scores_file:
            everything = snaykton_scores_file.read()
            high_scores = __decode_high_scores(everything)
            return high_scores
    except FileNotFoundError:
        print(f'File {__SNAYKTON_SCORES_FILENAME} not found. Will be created and encoded as an empty list. '
              f'Generated list will be returned.')
        new_scores = __generate_high_score_list()
        save_high_scores_to_file(new_scores)
        return new_scores


# save_high_scores_to_file(__generate_high_score_list())
# load_high_scores_from_file()
