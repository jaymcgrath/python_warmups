import itertools


def mask_it(input_int):
    """
    Write a function that, given an input string, 'masks' all of the characters with a
    '#' except for the last four characters

    >>> mask_it (44455666)
    '####5666'

    >>> mask_it(1234)
    '1234'

    >>> mask_it(123456789)
    '#####6789'

    """

    input_str = str(input_int)
    mask_len = len(input_str) - 4

    return (mask_len * '#') + input_str[mask_len:]


def pop_growth(start_pop, fixed_growth, pct_growth, target_pop):
    """


    :param start_pop:
    :param fixed_growth:
    :param pct_growth:
    :param target_pop:
    :return:

    >>> pop_growth(1000, 50, 2, 1200)
    '3 years'

    """

    num_years = 0
    while start_pop < target_pop:
        num_years += 1
        start_pop += start_pop * (pct_growth/100) + fixed_growth

    return "{y} years".format(y=num_years)


def flatten(input_dicts):
    """
    takes a list of dictionaries with identical key 'name' and flattens the corresponding
    values into a list

    :param input_dicts:
    :return: flattened

    >>> springfielders = [{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}, {'name': 'Otto'}]
    >>> flatten(springfielders)
    'Bart, Lisa, Maggie & Otto'

>>> springfielders = [{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}, {'name': 'Otto'}, {'name': 'Homer'}]
    >>> flatten(springfielders)
    'Bart, Lisa, Maggie & 2 others'


    >>> springfielders = [{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]
    >>> flatten(springfielders)
    'Bart, Lisa & Maggie'

    >>> springfielders = [{'name': 'Bart'}, {'name': 'Lisa'}]
    >>> flatten(springfielders)
    'Bart & Lisa'

    >>> springfielders = [{'name': 'Bart'}]
    >>> flatten(springfielders)
    'Bart'
    """

    # Create empty accumulator list
    flatter = []

    # Add dict values to list
    for this_dict in input_dicts:
        flatter.append(this_dict['name'])

    # Check if length sufficient for summarizing list end
    if len(flatter) >= 5:
        last_one = str(len(flatter[3:])) + " others"
    else:
        # insufficient length for "& others", place a single name after '&'
        last_one = flatter.pop()

    # OK, now join the first elements of the remaining list.. no oxford comma to worry about
    first_ones = ", ".join(flatter[:3])

    # At least two elements, so join the two parts with an '&'
    # Single element input distills down to this, so just return it
    return " & ".join((first_ones, last_one)) if len(first_ones) > 0 else last_one


def roto_crypt(message, key, direction):
    """
    Encrypt a message by rotating each character's ordinal by the amount given in the key.
    SYnc with the first four characters of the message, and rotate each char with the corresponding char in the key,
    then move the four char 'window' encode the next four, until the message is fully encrypted.
    :param message: string to encrypt
    :param key: list of ordinal rotations
    :param direction: integer of either -1 for decryption of 1 for encryption

    :return: str encrypted text

    >>> message='test'
    >>> roto_crypt(message, [1, -5, 3, 2], 1)
    'u`vv'

    >>> message='u`vv'
    >>> roto_crypt(message, [1, -5, 3, 2], -1)
    'test'

    >>> message="The quick brown llama jumped over the lazy aardvark"
    >>> roto_crypt(message, [1, -5, 3, 2], 1)
    'Uch"rplel\x1betprq"mgdob\x1bmwnkhf!jygs\x1bwjf\x1boc{t#cbmgxbmn'

    """

    # Using itertools.cycle, pair each character from the message with its corresponding shift, repeating til end of msg

    operational_pairs = zip(message, itertools.cycle(key))

    # operation_pairs is a list of tuples. Operate on it in a generator function, then join the output.
    encrypted = "".join(chr(ord(letter) + (direction * shift)) for letter, shift in operational_pairs)

    return encrypted

