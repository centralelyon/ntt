def calculate_temporal_accuracy(actual_value, predicted_value):
    """temporal accuracy = 1 - (error / actual_value)"""
    if actual_value == 0:
        return 0
    error = abs(actual_value - predicted_value)
    temporal_accuracy = 1.0 - (error / actual_value)
    return temporal_accuracy

if __name__ == "__main__":
    print(calculate_temporal_accuracy(10, 5))
    print(calculate_temporal_accuracy(10, 10))
    print(calculate_temporal_accuracy(10, 15))