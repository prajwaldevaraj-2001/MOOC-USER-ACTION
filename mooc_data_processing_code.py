import pandas as pd
import os

# Define dataset paths assuming they are already downloaded and stored in the data folder
def get_dataset_path():
    # List the available datasets in the 'data' folder
    datasets = ["data/mooc_action_features.tsv", "data/mooc_action_labels.tsv", "data/mooc_actions.tsv"]
    
    # Check if the datasets exist in the folder
    for dataset in datasets:
        if os.path.exists(dataset):
            print(f"Found dataset: {dataset}")
            return dataset
    print("No dataset found in the data folder.")
    return None

# Load and process the dataset
def process_dataset(filepath):
    print("Loading dataset...")

    # Ensure the path points to a valid file, not a directory
    if os.path.isdir(filepath):
        print(f"Error: {filepath} is a directory, not a file!")
        return None

    try:
        # Attempt to read the dataset with different encodings
        data = pd.read_csv(filepath, sep="\t", header=None, encoding="ISO-8859-1")  # Use ISO-8859-1 to handle potential encoding issues
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None
    
    # Check the number of columns in the dataset
    print(f"Dataset has {data.shape[1]} columns.")

    # Print the first few rows to inspect the data
    print("\nSample Data:")
    print(data.head())
    
    # Rename columns only if the dataset has the expected number of columns
    if data.shape[1] == 4:
        data.columns = ["user_id", "target_id", "action", "timestamp"]
    else:
        print("Dataset has a different number of columns than expected. Skipping renaming.")

    # Convert timestamp to readable format if possible
    if 'timestamp' in data.columns:
        data['timestamp'] = pd.to_datetime(data['timestamp'], unit='s', origin='unix')

    print(f"Dataset loaded with {data.shape[0]} rows and {data.shape[1]} columns.")
    
    return data

# Export data for Tableau
def export_for_tableau(data):
    export_path = "data/processed_mooc_data.csv"
    print(f"Exporting data to {export_path} for Tableau analysis...")
    data.to_csv(export_path, index=False)
    print("Data exported successfully.")

def main():
    # Step 1: Get the path of an existing dataset
    dataset_path = get_dataset_path()
    
    if dataset_path is None:
        print("Exiting due to missing dataset.")
        return
    
    # Step 2: Process the dataset
    data = process_dataset(dataset_path)
    
    if data is None:
        print("Exiting due to dataset processing failure.")
        return
    
    # Step 3: Export the dataset for Tableau
    export_for_tableau(data)

if __name__ == "__main__":
    main()
