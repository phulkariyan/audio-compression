







import numpy as np
from decibel_limiter import decibel_limiter

def check_output_range(input_level, output_level):
    """
    Check if the output level is within the expected range based on the input level.
    
    Args:
    input_level (float): Input audio level in decibels.
    output_level (float): Output audio level in decibels after limiting.
    
    Returns:
    bool: True if the output is within the expected range, False otherwise.
    """
    if input_level > 20:
        return output_level <= 20
    elif 6 < input_level <= 20:
        return 0 <= output_level <= 17  # Max reduction is 6dB, so 20-6=14, allowing some margin
    elif -10 <= input_level < 3:
        return -4 <= output_level <= 9  # Max boost is 6dB, so 3+6=9, allowing some margin
    else:
        return output_level == input_level

def test_limiter(test_levels):
    """
    Test the decibel limiter with a range of input levels and check if outputs are within expected ranges.
    
    Args:
    test_levels (list): List of input levels to test.
    
    Returns:
    tuple: (bool, list) - Overall test result and list of failed tests.
    """
    all_passed = True
    failed_tests = []

    for input_level in test_levels:
        output_level = decibel_limiter(input_level)
        if not check_output_range(input_level, output_level):
            all_passed = False
            failed_tests.append((input_level, output_level))

    return all_passed, failed_tests

def print_test_results(test_levels):
    """
    Run tests and print detailed results.
    
    Args:
    test_levels (list): List of input levels to test.
    """
    print("Detailed Test Results:")
    print("Input (dB) | Output (dB) | Within Range")
    print("----------|-------------|-------------")
    
    for level in test_levels:
        output = decibel_limiter(level)
        within_range = check_output_range(level, output)
        print(f"{level:10.2f} | {output:11.2f} | {'Yes' if within_range else 'No':13}")

    all_passed, failed_tests = test_limiter(test_levels)
    
    print("\nOverall Test Result:", "PASSED" if all_passed else "FAILED")
    
    if not all_passed:
        print("\nFailed Tests (Input, Output):")
        for input_level, output_level in failed_tests:
            print(f"  {input_level:.2f} dB -> {output_level:.2f} dB")

if __name__ == "__main__":
    # Test with a wide range of input levels
    test_levels = np.arange(-20, 30, 0.5).tolist()
    print_test_results(test_levels)
