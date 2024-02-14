# analysis.py
import argparse
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import logging


# Parse command-line arguments
parser = argparse.ArgumentParser(description='Apartment analysis script')
parser.add_argument('input_csv', type=str, help='Path to the input CSV dataset')
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

if not os.path.exists(args.config):
    raise FileNotFoundError(f"Configuration file '{args.config}' not found.")

try:

    # Load the dataset
    apartment = pd.read_csv(args.input_csv) 
    print(apartment)


except Exception as e:
    # Catch any exceptions, add context using e.add_note(), then raise the exception
    e.add_note("An error occurred during the analysis.")
    raise e

# Renaming one or more columns 
def clean_names(string):
    return string.lower()

apartment = apartment.rename(columns=clean_names)

# Creating a new column 'storey_group', otherwise there would be too many columns
apartment['storeys_group'] = pd.cut(apartment['confirmed_storeys'], bins=[float('-inf'), 24, float('inf')], labels=['less than 25', '25 or more'], right=False)

# Grouped bar chart for 'score' by 'wardname' and 'storeys_group' using seaborn
plt.figure(figsize=(14, 8))
sns.barplot(data=apartment, x='wardname', y='score', hue='storeys_group')

# Adding labels, title, and legend
plt.xlabel('Ward Name')
plt.ylabel('Apartment Score')
plt.title('Apartment Score by Ward Name and Storeys Group')
plt.xticks(rotation=45, ha='right')
plt.legend(title='Storeys Group')

# Save figures
plt.savefig('Apartment.png')

logging.info('Script started.')
logging.debug(f'Loading input CSV: {args.input_csv}')
logging.warning('Watch out for potential issues!')