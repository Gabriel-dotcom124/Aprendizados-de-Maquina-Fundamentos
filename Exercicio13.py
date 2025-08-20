import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder


data = sns.load_dataset('penguins')


data.head()



print("Missing values before handling:")
print(data.isnull().sum())


data.dropna(inplace=True)

print("\nMissing values after handling:")
print(data.isnull().sum())

display(data.head())



numerical_cols = data.select_dtypes(include=np.number).columns


response_vars = ['species', 'sex'] 
numerical_cols = [col for col in numerical_cols if col not in response_vars]


scaler = StandardScaler()
for col in numerical_cols:
    data[col + '_std'] = scaler.fit_transform(data[[col]])


display(data.head())


categorical_cols = data.select_dtypes(include='object').columns
response_vars = ['species', 'sex']
nominal_cols = [col for col in categorical_cols if col not in response_vars]
ordinal_cols = [] 
print("Nominal columns:", nominal_cols)
print("Ordinal columns:", ordinal_cols)


ohe = OneHotEncoder(sparse_output=False)

encoded_data = ohe.fit_transform(data[nominal_cols])

encoded_df = pd.DataFrame(encoded_data, columns=ohe.get_feature_names_out(nominal_cols), index=data.index)

data = pd.concat([data, encoded_df], axis=1)

data.drop(columns=nominal_cols, inplace=True)

display(data.head())

from sklearn.preprocessing import OrdinalEncoder

oe = OrdinalEncoder()

data = pd.concat([data, encoded_df], axis=1)

display(data.head())

display(data.head())


cols_to_keep = response_vars + [col for col in data.columns if col.endswith('_std') or col.endswith('_nom') or col.endswith('_ord')]

cols_to_drop = [col for col in data.columns if col not in cols_to_keep]

data.drop(columns=cols_to_drop, inplace=True)

display(data.head())

