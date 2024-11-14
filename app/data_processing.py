import pandas as pd

def clean_data(data):
    df = pd.DataFrame(data)
    df.dropna(inplace=True)
    # Additional cleaning steps here
    return df

def analyze_data(data):
    df = pd.DataFrame(data)
    analysis = {
        "mean_price": df["price"].mean(),
        "max_price": df["price"].max(),
        # Other analytics
    }
    return analysis
