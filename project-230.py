import pandas as pd
dataset = pd.read_csv(r'country_vaccinations')

print('Shape of given datset: ', dataset.shape)
print('Count of column: ', len(dataset.columns))
print('Name of parameter: ', dataset.columns)
print(f'Display empty row data: {dataset.loc[:, dataset.isna().any()]}')
