"""
To create a dummy dataset that simulates client data for multiple bank branches, we can generate a set of structured data for three hypothetical branches. Each branch dataset will include features like account balance, transaction history, loan history, and demographic information. Below, I outline the structure of the datasets and provide a sample generation using Python.

Dataset Structure
For each branch, the dataset will contain:

Client ID: Unique identifier for each client.
Branch: Identifying the branch to which the client belongs.
Age: Age of the client.
Gender: Gender of the client.
Account Balance: The current balance in the client's main account.
Total Loan Amount: Total amount of loans taken by the client.
Number of Transactions Last Month: A count of transactions in the last month.
Loan Defaulted: Whether the client has defaulted on a loan (Yes/No).
Sample Dataset Generation
To generate the data, we will use Python with libraries like pandas and numpy to handle data frames and generate random values.
"""

import pandas as pd
import numpy as np

# Define the number of clients per branch
num_clients_per_branch = 100

# Define branches
branches = ['North', 'South', 'East']

# Initialize an empty DataFrame
clients = pd.DataFrame()

# Seed for reproducibility
np.random.seed(42)

# Generate data for each branch
for branch in branches:
    # Generate data
    branch_data = pd.DataFrame({
        'Client ID': np.arange(1, num_clients_per_branch + 1),
        'Branch': branch,
        'Age': np.random.randint(18, 70, size=num_clients_per_branch),
        'Gender': np.random.choice(['Male', 'Female', 'Other'], size=num_clients_per_branch),
        'Account Balance': np.random.uniform(100, 10000, size=num_clients_per_branch).round(2),
        'Total Loan Amount': np.random.uniform(0, 50000, size=num_clients_per_branch).round(2),
        'Number of Transactions Last Month': np.random.poisson(5, size=num_clients_per_branch),
        'Loan Defaulted': np.random.choice(['Yes', 'No'], size=num_clients_per_branch, p=[0.1, 0.9])
    })
    
    # Append to the main DataFrame
    clients = pd.concat([clients, branch_data], ignore_index=True)

# Display a sample of the data
print(clients.head())
