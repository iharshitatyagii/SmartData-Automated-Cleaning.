import pandas as pd
import numpy as np

def clean_data(file_path):
    # Loading dataset
    df = pd.read_csv(file_path)
    print("Initial Data Shape:", df.shape)

    # 1. Handling Missing Values using Pandas
    df.fillna(df.median(numeric_only=True), inplace=True)
    df.dropna(axis=1, how='all', inplace=True)

    # 2. Removing Duplicates
    df.drop_duplicates(inplace=True)

    # 3. Data Transformation
    # Converting column names to lowercase for consistency
    df.columns = [col.lower().replace(' ', '_') for col in df.columns]

    print("Cleaned Data Shape:", df.shape)
    return df

if __name__ == "__main__":
    # Placeholder for a sample CSV file
    # df_cleaned = clean_data('sample_data.csv')
    print("SmartData: Automated Cleaning Tool is Ready!")
