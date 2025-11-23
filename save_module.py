import logging

def save_to_file(df, filename="processed_data.csv"):
    try:
        df.to_csv(filename, index=False)
        logging.info("File saved.")
    except Exception as e:
        logging.error(f"Save error: {e}")
