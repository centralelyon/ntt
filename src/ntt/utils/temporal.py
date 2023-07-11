def calculate_temporal_accuracy(actual_value, predicted_value):
    """temporal accuracy = 1 - (error / actual_value)"""
    error = abs(actual_value - predicted_value)
    temporal_accuracy = 1.0 - (error / actual_value)
    return temporal_accuracy
