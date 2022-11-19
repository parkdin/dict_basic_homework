def first_item():
    """
    Given a dictionary, Return first item value.
    """
    data = {
        'a': 10, 'b': 2,}
    first_item = list(data.values())[0]
    return first_item
print(first_item())