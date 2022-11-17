def create_dictionary(key, value):
    """
    Convert two lists into a dictionary
    Args:
        key(list): list of keys
        value(list): list of values
    Returns:
        dict: dictionary with keys and values
    """
    for k in key:
        key_item = k
        dic = dic.get(key_item)
        for v in value:
            value_item = v
            dic = {key_item : value_item}
        return dic
key = [1, 2, 4, 4, 5]
value = ["one", "two", "three", "four", "five"]
print(create_dictionary(key, value))