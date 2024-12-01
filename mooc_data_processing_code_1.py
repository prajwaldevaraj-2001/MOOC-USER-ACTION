import pandas as pd
import random

# Define possible values for actions and labels
actions = ["like", "share", "view", "purchase", "comment"]
labels = ["label_1", "label_2", "label_3", "label_4", "label_5"]

# Define a list of user IDs
user_ids = [f"user_{i}" for i in range(1, 6)]

# Generate synthetic dataset
data = []

for user in user_ids:
    # Randomly generate actions and labels for each user
    num_actions = random.randint(5, 10)  # Random number of actions per user
    for _ in range(num_actions):
        action = random.choice(actions)
        label = random.choice(labels)
        data.append([user, action, label])

# Convert the generated data to a DataFrame
synthetic_data = pd.DataFrame(data, columns=["userId", "action", "label"])

# Export the synthetic data to a CSV file
output_file = "synthetic_mooc_data.csv"
synthetic_data.to_csv(output_file, index=False)

# Print the first few rows to check
print("Synthetic Data:")
print(synthetic_data.head())
