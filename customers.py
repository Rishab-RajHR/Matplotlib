# Import the libraries

import pandas as pd
import matplotlib.pyplot as plt

# load the data
df = pd.read_csv('customers-1000.csv')

# clean data => duplicates removal
df = df.dropna(subset=['Index', 'Customer Id', 'First Name', 'Last Name', 'Company', 'City', 'Country', 'Phone 1', 'Phone 2', 'Email', 'Subscription Date', 'Website'])
# print(df.columns)

type_counts = df['Index'].value_counts()
plt.figure(figsize=(6,4))
plt.bar(type_counts.index, type_counts.values, color=['skyblue', 'orange'])
plt.title('Data of customers')
plt.xlabel('Customer')
plt.ylabel('Company')
plt.tight_layout()
plt.savefig('Customer_plot.png')
plt.show()