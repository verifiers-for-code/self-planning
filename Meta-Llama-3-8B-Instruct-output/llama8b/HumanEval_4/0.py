from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    
    Parameters:
    numbers (List[float]): A list of float numbers.
    
    Returns:
    float: The Mean Absolute Deviation.
    """
    # 1. Calculate the mean of the input list.
    mean = sum(numbers) / len(numbers)
    
    # 2. Calculate the absolute difference between each number and the mean.
    deviations = [abs(num - mean) for num in numbers]
    
    # 3. Calculate the average of the absolute differences.
    mad = sum(deviations) / len(deviations)
    
    # 4. Return the result.
    return mad