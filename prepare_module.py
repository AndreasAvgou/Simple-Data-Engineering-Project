import pandas as pd
import logging

def prepare_dataframe(data):
    try:
        df = pd.DataFrame(data)
        df = df.dropna()
        logging.info("Data cleaned.")
        return df
    except Exception as e:
        logging.error(f"Prep error: {e}")
        return pd.DataFrame()
