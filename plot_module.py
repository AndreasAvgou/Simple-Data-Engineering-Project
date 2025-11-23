import logging
import matplotlib.pyplot as plt

def generate_plots(df):
    try:
        plt.figure()
        df['desc_length'].hist()
        plt.savefig('plot_desc_length.png')

        plt.figure()
        df['ingredient_count'].hist()
        plt.savefig('plot_ing_count.png')

        if 'id' in df.columns:
            plt.figure()
            plt.scatter(df['id'], df['desc_length'])
            plt.savefig('plot_id_desc.png')

        plt.figure()
        plt.scatter(df['ingredient_count'], df['desc_length'])
        plt.savefig('plot_ing_desc.png')

        logging.info("Plots created.")
    except Exception as e:
        logging.error(f"Plot error: {e}")
