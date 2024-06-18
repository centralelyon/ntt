"""TODO : temporal module provides ...
"""


def calculate_temporal_accuracy(actual_value, predicted_value):
    """temporal accuracy = 1 - (error / actual_value)

    Args:
        actual_value (_type_): _description_
        predicted_value (_type_): _description_

    Returns:
        _type_: _description_
    """
    error = abs(actual_value - predicted_value)
    temporal_accuracy = 1.0 - (error / actual_value)
    return temporal_accuracy
