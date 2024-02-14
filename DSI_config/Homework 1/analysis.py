# analysis.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import pandas as pd
apartment=pd.read_csv('Ming_Kirsten-python_assignment2_orig.csv') 
print(apartment)

#Renaming one or more columns 
def clean_names(string):
    return string.lower()

apartment=apartment.rename(columns=clean_names)

# creating a new column 'storey_group', otherwise there would be too many columns
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

