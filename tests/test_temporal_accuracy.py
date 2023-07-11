from ntt.utils.temporal import calculate_temporal_accuracy


def test_temporal_accuracy():
    actual = 10
    predicted = 10
    expected_accuracy = 1.0
    accuracy = calculate_temporal_accuracy(actual, predicted)
    assert (
        accuracy == expected_accuracy
    ), f"expected accuracy: {expected_accuracy} ({accuracy})"

    actual = 10
    predicted = 5
    expected_accuracy = 0.5
    accuracy = calculate_temporal_accuracy(actual, predicted)
    assert (
        accuracy == expected_accuracy
    ), f"expected accuracy: {expected_accuracy} ({accuracy})"

    actual = 10
    predicted = 15
    expected_accuracy = 0.5
    accuracy = calculate_temporal_accuracy(actual, predicted)
    assert (
        accuracy == expected_accuracy
    ), f"expected accuracy: {expected_accuracy} ({accuracy})"


if __name__ == "__main__":
    test_temporal_accuracy()
