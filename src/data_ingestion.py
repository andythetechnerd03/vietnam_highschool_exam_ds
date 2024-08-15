import pandas as pd
from src.config import Config

def read_data(file_name: str) -> pd.DataFrame:
    """Read data from file_name and return a pandas DataFrame

    Args:
        file_name (str): Path to the file

    Returns:
        pd.DataFrame: DataFrame containing data from file_name
    """
    df = pd.read_csv(file_name)
    print("Read data successfully")
    # Rename columns from Vietnamese to English
    df = df.rename(Config.column_rename_dict, axis=1)
    print("Renamed columns")
    print("Data shape: ", df.shape)
    print("Dataframe info: ", df.info())
    return df

def feature_engineering(df: pd.DataFrame) -> pd.DataFrame:
    """Feature engineering for the data, including:
    - Adding province column
    - Adding language name column
    - Adding social and natural columns

    Args:
        df (pd.DataFrame): DataFrame containing data

    Returns:
        pd.DataFrame: DataFrame containing data after feature engineering
    """
    # Use first 2 digits of student_id to get province code and map to province name
    df["province"] = (df["student_id"] // 1000000).map(Config.province_codes)
    print("Added province column")

    # Map language id to language name
    df["lang_name"] = df["lang_id"].map(Config.language_codes)
    print("Added language name column")

    # Find out if the students chose Natural Science or Social Science
    natural_df = df[["physics","chemistry","biology"]]
    social_df = df[["history","geography","civic_education"]]
    df["social"] = social_df.notna().sum(axis=1) > 0
    df["natural"] = natural_df.notna().sum(axis=1) > 0
    print("Added social and natural columns")
    return df

def process_nan(df: pd.DataFrame) -> pd.DataFrame:
    """Process NaN values in the DataFrame

    Args:
        df (pd.DataFrame): DataFrame containing data

    Returns:
        pd.DataFrame: DataFrame containing data after processing NaN values
    """
    # Fill NaN values in subject columns with 0
    # Replace NaN values in mandatory subject columns with 0
    df[["math","literature","language"]].fillna(0, inplace=True)
    # Replace NaN values in Natural/Social Science for students opting for it
    df[df["social"]==True][["history","geography","civic_education"]].fillna(0, inplace=True)
    df[df["natural"]==True][["physics","chemistry","biology"]].fillna(0, inplace=True)
    return df

