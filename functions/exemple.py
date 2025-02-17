import pandas as pd


def create_exemple():

    """
    Returns a data frame exemple.
    """

    data = pd.DataFrame({
        'product': ['cafe', 'guarana', 'pastel'],
        'price': [6, 5 , 7],
        'quantity': [20, 10, 15]
    })

    return data 