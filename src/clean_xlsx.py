"""
                                    +---------------+
                                    | clean_xlsx.py |
                                    +---------------+

This is a python script you can use to clean up the .xlsx file
that the professor gave us. It creates two new files:
- data.csv: data in csv format
- data.pkl: data in pickle format

Run the script from the root of the repository with:

```bash
uv run python src/clean_xlsx.py
```
"""

import pandas as pd

def clean_xlsx(file_path: str = "data/baseline_sample.xlsx") -> pd.DataFrame:
    # Read the xlsx file
    df = pd.read_excel(file_path)

    # Missing value check
    n_row_missing = df.isnull().sum(axis=1)
    if n_row_missing.sum() > 0:
        raise ValueError(f"Found {n_row_missing.sum()} rows with missing values in the dataset. Please check the xlsx file.")

    # New columns names
    col_map = {
        'Media_Attention (IV1)': 'media_attention',
        'Exposure_Level (IV2)': 'exposure_level',
        'Industry (IV3)': 'industry',
        'Buying_Intention (DV1)': 'buying_intention'
    }

    # Rename columns
    df.rename(columns=col_map, inplace=True)

    # Categorical columns
    categorical_columns = ['media_attention', 'exposure_level', 'industry']
    for col in categorical_columns:
        df[col] = df[col].astype('category')

    # Int for buying intention
    df['buying_intention'] = df['buying_intention'].astype(int)

    # Print the head of the cleaned dataframe
    print(df.head())

    # Save to csv
    df.to_csv('data/data.csv', index=False)

    # Save to pickle
    df.to_pickle('data/data.pkl')

    return df

if __name__ == "__main__":
    print("Cleaning the xlsx file...")
    clean_xlsx()
    print("Done. The cleaned data is saved as data.csv and data.pkl.")