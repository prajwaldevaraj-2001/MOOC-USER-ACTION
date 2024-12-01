import pandas as pd
import os
import random

# Define possible values for actions and labels
actions = ["like", "share", "view", "purchase", "comment"]
labels = ["label_1", "label_2", "label_3", "label_4", "label_5"]

# Function to load all datasets from the 'data' directory
def load_datasets(data_dir):
    datasets = []
    for filename in os.listdir(data_dir):
        if filename.endswith(".csv") or filename.endswith(".tsv"):  # Check for .csv or .tsv files
            file_path = os.path.join(data_dir, filename)
            try:
                # Assuming the data is in a tab-separated or comma-separated format
                if filename.endswith(".csv"):
                    data = pd.read_csv(file_path)
                elif filename.endswith(".tsv"):
                    data = pd.read_csv(file_path, sep="\t")
                datasets.append(data)
            except Exception as e:
                print(f"Error loading {filename}: {e}")
    return datasets

# Generate synthetic dataset (for demonstration, random actions and labels for users)
def generate_synthetic_data(users):
    data = []
    for user in users:
        num_actions = random.randint(5, 10)  # Random number of actions per user
        for _ in range(num_actions):
            action = random.choice(actions)
            label = random.choice(labels)
            data.append([user, action, label])
    return pd.DataFrame(data, columns=["userId", "action", "label"])

# Forecast the next action and label for each user (based on their last action)
def forecast_next_action(data):
    forecasted_data = []
    for user in data["userId"].unique():
        user_data = data[data["userId"] == user]
        
        # Forecast based on the last action and label
        last_action = user_data["action"].iloc[-1]
        last_label = user_data["label"].iloc[-1]
        
        # Randomly predict the next action and label
        next_action = random.choice(actions)
        next_label = random.choice(labels)
        
        forecasted_data.append([user, next_action, next_label])
    
    forecast_df = pd.DataFrame(forecasted_data, columns=["userId", "predicted_action", "predicted_label"])
    return forecast_df

# Function to combine synthetic data with forecasted data
def combine_data(synthetic_data, forecast_data):
    combined_data = pd.concat([synthetic_data, forecast_data], axis=0, ignore_index=True)
    return combined_data

# Export the combined data to a CSV file
def export_data_to_csv(data, output_file):
    data.to_csv(output_file, index=False)
    print(f"Data exported successfully to {output_file}")

def main():
    # Step 1: Load datasets from the 'data' folder
    data_dir = "data/"
    datasets = load_datasets(data_dir)
    
    if not datasets:
        print("No datasets found in the data folder.")
        return
    
    # Step 2: Generate synthetic data for all users
    all_users = [f"user_{i}" for i in range(1, 6)]  # Example users user_1 to user_5
    synthetic_data = generate_synthetic_data(all_users)
    
    # Step 3: Forecast the next action/label for each user
    forecasted_data = forecast_next_action(synthetic_data)
    
    # Step 4: Combine the original synthetic data with the forecasted data
    combined_data = combine_data(synthetic_data, forecasted_data)
    
    # Step 5: Export the combined data to a CSV file
    output_file = "synthetic_mooc_data_with_forecasting.csv"
    export_data_to_csv(combined_data, output_file)

    # Print sample output for verification
    print("Combined Data with Forecasting:")
    print(combined_data.head())

if __name__ == "__main__":
    main()
