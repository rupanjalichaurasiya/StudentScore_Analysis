import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import sqlalchemy as sal

# Correct method to read the CSV file
df = pd.read_csv("student_scores.csv")

# Display the first 5 rows of the DataFrame
print(df.head())

# Display summary statistics of numerical columns
print(df.describe())

# Display a concise summary of the DataFrame
print(df.info())

# Print column names to verify
print("Column names:", df.columns)

# Convert column names to lowercase
df.columns = df.columns.str.lower()

# Add a new column for percentage (assuming columns are 'mathscore', 'readingscore', 'writingscore')
df['percentage'] = df[['mathscore', 'readingscore', 'writingscore']].mean(axis=1)

# Display the updated DataFrame
print(df.head())

# Load the data into SQL Server using the replace option
# Create the SQLAlchemy engine for Windows Authentication
engine = sal.create_engine(
    "mssql+pyodbc://DESKTOP-KOHQCLC\SQLEXPRESS/master?driver=ODBC+Driver+17+for+SQL+Server&Trusted_Connection=yes"
)

# Connect to the database
conn = engine.connect()

# Load the DataFrame into SQL Server table named 'student_scores' (replace if exists)
df.to_sql('df_scores', conn, if_exists='replace', index=False)

# Close the connection
conn.close()
