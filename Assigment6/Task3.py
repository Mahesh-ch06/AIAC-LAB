import statistics

def statistical_operations(tuple_num):
    if not tuple_num:
        return {}

    nums = list(tuple_num)

    min_val = min(nums)
    max_val = max(nums)
    mean_val = statistics.mean(nums)
    median_val = statistics.median(nums)

    try:
        mode_val = statistics.mode(nums)
    except statistics.StatisticsError:
        mode_val = None

    variance_val = statistics.variance(nums)
    stdev_val = statistics.stdev(nums)

    return {
        'minimum': min_val,
        'maximum': max_val,
        'mean': mean_val,
        'median': median_val,
        'mode': mode_val,
        'variance': variance_val,
        'standard_deviation': stdev_val
    }

# Example usage
if __name__ == "__main__":
    sample_tuple = (1, 2, 3, 4, 5, 5, 6)
    results = statistical_operations(sample_tuple)
    print("Statistical Operations Results:")
    for key, value in results.items():
        print(f"{key.capitalize()}: {value}")