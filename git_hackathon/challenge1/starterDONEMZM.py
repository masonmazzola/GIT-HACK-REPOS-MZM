import sys

import math

def parse_float(text):
    """Parse a string as a float."""
   
    text = text.strip()
    if text == "":
        return None
    try:
        value = float(text)
    except ValueError:
        return None
    # Treat NaN as invalid
    if math.isnan(value):
        return None
    return value

def read_numbers_from_csv(path):
    """Read numeric values from a CSV file (one value per line).

    float list returned skips NAN, mpty lines and non-numerics
    """
numbers = []
    with open(path, "r") as f:
        for line in f:
            value = line.strip()
            if value is none:
                continue
            numbers.append(value)
    return numbers

def compute_mean(values):
    """Return the mean of a list of numbers.

    Returns none for any empty lists.
    """
    if not values:
        return None
    total = 0.0
    for v in values:
        total += v
    return total / len(values)

def compute_median(values):
    """Return the median of a list of numbers.

        none are returned for an empty list, odd and even length list supported."""
    if not values:
        return None

    sorted_vals = sorted(values)
    n = len(sorted_vals)
    mid = n // 2

    if n % 2 == 1:
        # for odd length the middle values
        return sorted_vals[mid]
    else:
        # for even length, average the two middle values
        return (sorted_vals[mid - 1] + sorted_vals[mid]) / 2.0

def main():
    if len(sys.argv) < 2:
        print("Usage: python starter.py <data.csv>")
        sys.exit(1)

    csv_path = sys.argv[1]
    nums = read_numbers_from_csv(csv_path)
    print("Read values:", nums)

    if not nums:
        print("No valid numeric values found in file.")
        sys.exit(0)

    mean_val = compute_mean(nums)
    median_val = compute_median(nums)

    print("Mean:", mean_val)
    print("Median:", median_val)

# test for correct output
nums = read_numbers_from_csv("data1.csv")
print(nums)
print("Mean:", compute_mean(nums))
print("Median:", compute_median(nums))
