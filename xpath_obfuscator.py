"""
Simple XPath obfuscator based around tokenizing
"""

def obfuscate_tokens(tokens):
    id = 10000
    token_to_obfuscated_dict = dict()

    def next_token(token, id):
        if (len(token) < 3):
            return (token, id)
        next_token = f"token_{id}"
        id = id + 1
        return (next_token, id)

    for token in tokens:
        (obfuscated, next_id) = next_token(token, id)
        id = next_id
        token_to_obfuscated_dict[token] = obfuscated

    return token_to_obfuscated_dict

def create_translation_table():
    special_chars = "()[]/\\@.$='"
    translate_to_split = dict()
    split_char = ' '
    for special_char in special_chars:
        translate_to_split[ord(special_char)] = ord(split_char)
    return translate_to_split

def obfuscate(xpath):
    translate_to_split = create_translation_table()
    # we don't obfuscate keywords
    keywords = ['and', 'or', 'not', 'contains', 'sibling']

    # using a set, so that values are distinct
    xpath_no_special_chars = xpath.translate(translate_to_split).split()
    tokens = list(set(xpath_no_special_chars))
    tokens = [t for t in tokens if not(t in keywords)]

    # sort for consistent, testable behaviour:
    tokens.sort()
    token_to_obfuscated_dict = obfuscate_tokens(tokens)

    # replace, starting with longest tokens first (since they can contain shorter tokens):
    keys_by_len_desc = list(token_to_obfuscated_dict.keys())
    keys_by_len_desc.sort(key=len, reverse=True)

    obfuscated = xpath
    for token in keys_by_len_desc:
        obfuscated = obfuscated.replace(token, token_to_obfuscated_dict[token])

    return obfuscated
