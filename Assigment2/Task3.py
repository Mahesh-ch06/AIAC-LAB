# Write a Python code that read a CSV file and calculates the mean, min, and max of a specific numerical column.

import csv
def calculate_statistics(file_name: str, column_name: str) -> None:
    values = []
    
    # Reading the CSV file
    with open(file_name, mode='r') as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            try:
                value = float(row[column_name])
                values.append(value)
            except ValueError:
                continue  # Skip rows where conversion fails
    
    if not values:
        print(f"No valid data found in column '{column_name}'.")
        return
    
    mean_value = sum(values) / len(values)
    min_value = min(values)
    max_value = max(values)
    
    print(f"Statistics for column '{column_name}':")
    print(f"Mean: {mean_value}")
    print(f"Min: {min_value}")
    print(f"Max: {max_value}")
if __name__ == "__main__":
    # Example usage - Using 'Age' column from data.csv
    calculate_statistics('data.csv', 'Age')
