import argparse
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import logging
import yaml
import os

def load_configuration(config_path):
    """Load configuration from YAML file."""
    try:
        with open(config_path, 'r') as file:
            return yaml.safe_load(file)
    except Exception as e:
        e.add_note("An error occurred while loading the configuration.")
        raise e

# creating the bins for the graph
def preprocess_data(df):
    """Preprocess the dataset."""
    df.columns = map(str.lower, df.columns)
    df['storeys_group'] = pd.cut(df['confirmed_storeys'], bins=[float('-inf'), 24, float('inf')],
                                labels=['less than 25', '25 or more'], right=False)
    return df

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Apartment analysis script')
    parser.add_argument('--config', type=str, help='Path to the configuration file', default='user_config.yml')
    parser.add_argument('--verbose', '-v', action='store_true', help='Print verbose logs')
    args = parser.parse_args()

    # Determine logging level based on arguments
    logging_level = logging.DEBUG if args.verbose else logging.INFO

    # Initialize logging module
    logging.basicConfig(
        level=logging_level,
        handlers=[logging.StreamHandler(), logging.FileHandler('my_python_analysis.log')],
    )

    # Get the absolute path to the configuration file
    config_path = os.path.abspath(args.config)

    # Load configuration
    config_data = load_configuration(config_path)

    # Assuming dataset path is included in the configuration file
    dataset_path = os.path.abspath(config_data['dataset_path'])
    
    # Load dataset
    apartment = pd.read_csv(dataset_path)

    # Preprocess data
    apartment = preprocess_data(apartment)

    # Grouped bar chart
    plt.figure(figsize=(14, 8))
    sns.barplot(data=apartment, x=config_data['group_col'], y=config_data['aggregation_col'], hue=config_data['color_col'])

    # Adding labels, title, and legend
    plt.xlabel(config_data['x_label'])
    plt.ylabel(config_data['y_label'])
    plt.title(config_data['plot_title'])
    plt.xticks(rotation=config_data['x_ticks_rotation'], ha='right')
    plt.legend(title=config_data['legend_title'])

    # Save figure
    plt.savefig(config_data['output_file'])

    logging.info('Script completed successfully.')

if __name__ == "__main__":
    main()
