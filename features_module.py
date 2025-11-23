import logging

def add_features(df):
    try:
        df['desc_length'] = df['description'].apply(len)
        df['ingredient_count'] = df['ingredients'].apply(len)
        logging.info("Features added.")
        return df
    except Exception as e:
        logging.error(f"Feature error: {e}")
        return df
