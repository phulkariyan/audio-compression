import numpy as np

def calculate_proportion(value, min_range, max_range):
    """
    Calculate the proportion of a value within a given range.
    
    Args:
    value (float): The value to calculate the proportion for.
    min_range (float): The minimum value of the range.
    max_range (float): The maximum value of the range.
    
    Returns:
    float: The calculated proportion.
    """
    return (value - min_range) / (max_range - min_range)

def apply_upper_limiting(input_level, min_threshold, max_threshold, min_reduction, max_reduction):
    """
    Apply upper threshold limiting to the input level.
    
    Args:
    input_level (float): Input audio level in decibels.
    min_threshold (float): Minimum threshold for limiting.
    max_threshold (float): Maximum threshold for limiting.
    min_reduction (float): Minimum reduction to apply.
    max_reduction (float): Maximum reduction to apply.
    
    Returns:
    float: Adjusted audio level in decibels.
    """
    proportion = calculate_proportion(input_level, min_threshold, max_threshold)
    reduction = min_reduction + (proportion * (max_reduction - min_reduction))
    return input_level - reduction

def apply_lower_boosting(input_level, min_threshold, max_threshold, min_boost, max_boost):
    """
    Apply lower threshold boosting to the input level.
    
    Args:
    input_level (float): Input audio level in decibels.
    min_threshold (float): Minimum threshold for boosting.
    max_threshold (float): Maximum threshold for boosting.
    min_boost (float): Minimum boost to apply.
    max_boost (float): Maximum boost to apply.
    
    Returns:
    float: Adjusted audio level in decibels.
    """
    proportion = calculate_proportion(input_level, min_threshold, max_threshold)
    boost = max_boost - (proportion * (max_boost - min_boost))
    return input_level + boost

def decibel_limiter(input_level):
    """
    Applies decibel limiting to the input level.
    
    Args:
    input_level (float): Input audio level in decibels.
    
    Returns:
    float: Adjusted audio level in decibels.
    """
    if 6 < input_level <= 20:
        return apply_upper_limiting(input_level, 6, 20, 3, 6)
    elif -10 <= input_level < 3:
        return apply_lower_boosting(input_level, -10, 3, 3, 6)
    else:
        return input_level

def print_test_results(test_levels):
    """
    Print test results for a list of input levels.
    
    Args:
    test_levels (list): List of input levels to test.
    """
    print("Input (dB) | Output (dB)")
    print("----------|-----------")
    for level in test_levels:
        output = decibel_limiter(level)
        print(f"{level:10.2f} | {output:10.2f}")

# Test the function
if __name__ == "__main__":
    test_levels = [-15, -10, -5, 0, 3, 6, 10, 15, 20, 25]
    print_test_results(test_levels)
