from fetch_module import fetch_data
from prepare_module import prepare_dataframe
from features_module import add_features
from save_module import save_to_file
from plot_module import generate_plots
from db_module import init_db, insert_data
import logging

logging.basicConfig(filename='app.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    url = "https://api.sampleapis.com/coffee/hot"

    init_db()

    data = fetch_data(url)
    df = prepare_dataframe(data)

    if df.empty:
        logging.error("Empty dataframe. Exiting.")
        return

    df = add_features(df)
    save_to_file(df)
    insert_data(df)
    generate_plots(df)

    print("Execution completed.")

if __name__ == "__main__":
    main()
