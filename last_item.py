def last_item():
    """
    Given a dictionary, Return last item value.
    """
    data = {'a': 1, 'b': 2}
    last_item = list(data.values())[-1]
    return last_item
print(last_item())