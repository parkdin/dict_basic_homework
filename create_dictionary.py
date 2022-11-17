def create_dictionary(key, value):
    """
    Convert two lists into a dictionary
    Args:
        key(list): list of keys
        value(list): list of values
    Returns:
        dict: dictionary with keys and values
    """
    dic = dict(zip(key, value))
    return dic
key = [1, 2, 3, 4, 5]
value = ["one", "two", "three", "four", "five"]
print(create_dictionary(key, value))