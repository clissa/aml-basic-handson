# Pandas Tutorial for Data Science
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# Set display options for better readability
pd.set_option('display.max_columns', 10)
pd.set_option('display.max_rows', 20)

# 1. Pandas Series
# Creating a Series from a list
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print("Basic Series:")
print(s)
print("\nSeries data type:", type(s))
print("\nSeries index:", s.index)
print("\nSeries values:", s.values)
print("\nSeries data type of values:", type(s.values))

# Series vs NumPy Arrays
# Create a NumPy array
np_array = np.array([1, 3, 5, np.nan, 6, 8])
print("NumPy array:")
print(np_array)
print("\nNumPy array type:", type(np_array))

# Key differences
print("\nKey differences:")
print("1. Series has index labels, NumPy arrays don't")
print("2. Series can have a name")
print("3. Series have additional built-in methods for data analysis")

# Create a Series with custom index
s_with_index = pd.Series([1, 3, 5, 7, 9], index=['a', 'b', 'c', 'd', 'e'])
print("\nSeries with custom index:")
print(s_with_index)

# Series with name
s_with_index.name = 'my_series'
print("\nSeries with name:")
print(s_with_index)

# Series access by index
print("\nAccessing Series elements:")
print("Value at index 'c':", s_with_index['c'])
print("Values at indexes 'a', 'c', 'e':", s_with_index[['a', 'c', 'e']])

# Series operations
print("\nSeries operations:")
print("Series + 5:")
print(s_with_index + 5)
print("\nSeries * 2:")
print(s_with_index * 2)

# Creating Series from Dictionaries
# Creating a Series from a dictionary
cities_population = {'Rome': 2873000, 'Paris': 2161000, 'London': 8982000, 'Berlin': 3645000, 'Madrid': 3223000}
population_series = pd.Series(cities_population)
print("Series from dictionary:")
print(population_series)
print("\nIndex:", population_series.index)
print("\nValues:", population_series.values)

# Filtering Series
print("\nCities with population > 3M:")
print(population_series[population_series > 3000000])

# 2.1 Creating DataFrames from Scratch
# Creating a DataFrame from a dictionary of Series
data = {
    'City': ['Rome', 'Paris', 'London', 'Berlin', 'Madrid'],
    'Population': [2873000, 2161000, 8982000, 3645000, 3223000],
    'Area': [1285, 105, 1572, 891, 604],
    'Country': ['Italy', 'France', 'UK', 'Germany', 'Spain']
}

df_cities = pd.DataFrame(data)
print("DataFrame from dictionary:")
print(df_cities)

# Creating a DataFrame with custom index
df_indexed = pd.DataFrame(data, index=data['City'])
print("\nDataFrame with custom index:")
print(df_indexed)

# Creating a DataFrame from a list of dictionaries
list_of_dicts = [
    {'Name': 'Alice', 'Age': 25, 'City': 'Rome'},
    {'Name': 'Bob', 'Age': 30, 'City': 'Paris'},
    {'Name': 'Charlie', 'Age': 35, 'City': 'London'},
    {'Name': 'Diana', 'Age': 40, 'City': 'Berlin'}
]
df_from_list = pd.DataFrame(list_of_dicts)
print("\nDataFrame from list of dictionaries:")
print(df_from_list)

# Creating a DataFrame from a 2D NumPy array
np_array_2d = np.random.randn(5, 4)  # 5 rows, 4 columns of random numbers
df_from_array = pd.DataFrame(np_array_2d, 
                           columns=['A', 'B', 'C', 'D'],
                           index=['Row1', 'Row2', 'Row3', 'Row4', 'Row5'])
print("\nDataFrame from 2D NumPy array:")
print(df_from_array)

# 2.2 Iterating Over DataFrames
# Setup a small DataFrame for iteration examples
iteration_df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['Rome', 'Paris', 'London']
})
print("DataFrame for iteration examples:")
print(iteration_df)

# Using iterrows()
print("\nUsing iterrows():")
for index, row in iteration_df.iterrows():
    print(f"Index: {index}, Name: {row['Name']}, Age: {row['Age']}")

# Using itertuples()
print("\nUsing itertuples():")
for row in iteration_df.itertuples():
    print(f"Index: {row.Index}, Name: {row.Name}, Age: {row.Age}")

# Using iteritems() - iterates over columns
print("\nUsing iteritems():")
for column_name, column_values in iteration_df.iteritems():
    print(f"Column: {column_name}, Values: {column_values.values}")

# Performance comparison (not executed for brevity, but described)
print("\nBest practices for iteration:")
print("1. itertuples() is generally the fastest for row iteration")
print("2. Vectorized operations are preferred over explicit iteration")
print("3. Use apply() for more complex operations")
print("4. Use NumPy or list comprehensions for extremely performance-critical code")

# Example of vectorized operation vs iteration
print("\nVectorized operation example:")
# Slow way (iteration):
# for i, row in df.iterrows():
#     df.loc[i, 'Age_plus_10'] = row['Age'] + 10

# Fast way (vectorized):
iteration_df['Age_plus_10'] = iteration_df['Age'] + 10
print(iteration_df)

# 2.3 Reading Data from Files
# Let's assume we have Boston Housing Dataset in CSV format
try:
    boston_df = pd.read_csv('boston.csv')
    print("Boston Housing Dataset (first 5 rows):")
    print(boston_df.head())
except FileNotFoundError:
    # If file not found, create mock data
    print("Boston Housing Dataset not found, creating mock data...")
    np.random.seed(42)
    n_samples = 100
    
    boston_df = pd.DataFrame({
        'CRIM': np.random.exponential(scale=0.5, size=n_samples),
        'ZN': np.random.choice([0, 20, 40, 60, 80, 100], size=n_samples),
        'INDUS': np.random.uniform(low=0, high=30, size=n_samples),
        'CHAS': np.random.choice([0, 1], size=n_samples),
        'NOX': np.random.uniform(low=0.3, high=0.9, size=n_samples),
        'RM': np.random.normal(loc=6.0, scale=0.7, size=n_samples),
        'AGE': np.random.uniform(low=10, high=100, size=n_samples),
        'DIS': np.random.exponential(scale=3, size=n_samples),
        'RAD': np.random.choice([1, 2, 3, 4, 5, 6, 7, 8, 24], size=n_samples),
        'TAX': np.random.uniform(low=180, high=700, size=n_samples),
        'PTRATIO': np.random.uniform(low=12, high=22, size=n_samples),
        'B': np.random.uniform(low=0, high=400, size=n_samples),
        'LSTAT': np.random.exponential(scale=7, size=n_samples),
        'MEDV': np.random.normal(loc=22, scale=9, size=n_samples)
    })
    print(boston_df.head())

# Basic dataset information
print("\nDataset information:")
print(boston_df.info())

# Basic statistics
print("\nBasic statistics:")
print(boston_df.describe())

# Check for missing values
print("\nMissing values count:")
print(boston_df.isnull().sum())

# 2.4 Data Filtering and Indexing
# Basic column selection
print("Selecting single column:")
print(boston_df['MEDV'].head())  # Housing price (target variable)

# Selecting multiple columns
print("\nSelecting multiple columns:")
print(boston_df[['CRIM', 'RM', 'MEDV']].head())

# Row filtering with conditions
print("\nExpensive houses (MEDV > 30):")
expensive_houses = boston_df[boston_df['MEDV'] > 30]
print(expensive_houses.head())

# Multiple conditions
print("\nLarge houses (RM > 7) that are expensive (MEDV > 30):")
large_expensive = boston_df[(boston_df['RM'] > 7) & (boston_df['MEDV'] > 30)]
print(large_expensive.head())

# Using .loc for label-based indexing
print("\nUsing .loc for label-based indexing:")
print(boston_df.loc[0:4, ['CRIM', 'RM', 'MEDV']])  # rows 0-4, columns CRIM, RM, MEDV

# Using .iloc for integer-based indexing
print("\nUsing .iloc for integer-based indexing:")
print(boston_df.iloc[0:5, [0, 5, -1]])  # first 5 rows, columns 0, 5, and last

# Setting index
boston_indexed = boston_df.set_index('MEDV')
print("\nDataFrame with MEDV as index:")
print(boston_indexed.head())

# Reset index
boston_reset = boston_indexed.reset_index()
print("\nDataFrame with reset index:")
print(boston_reset.head())

# Sorting
print("\nSorting by MEDV (descending):")
print(boston_df.sort_values('MEDV', ascending=False).head())

# Sorting by multiple columns
print("\nSorting by RM (ascending) and MEDV (descending):")
print(boston_df.sort_values(['RM', 'MEDV'], ascending=[True, False]).head())

# 2.5 Working with Date Indexes
# Create a DataFrame with date index
print("Creating a time series DataFrame:")
date_range = pd.date_range(start='2023-01-01', periods=10, freq='D')
print("Date range:")
print(date_range)

time_series_df = pd.DataFrame({
    'Value': np.random.randn(10),
    'Volume': np.random.randint(100, 1000, size=10)
}, index=date_range)
print("\nTime series DataFrame:")
print(time_series_df)

# Select specific date
print("\nData for specific date (2023-01-05):")
print(time_series_df.loc['2023-01-05'])

# Select date range
print("\nData for date range (2023-01-03 to 2023-01-07):")
print(time_series_df.loc['2023-01-03':'2023-01-07'])

# Resampling - Aggregating to monthly frequency
print("\nResampling to monthly frequency (mean):")
print(time_series_df.resample('M').mean())

# Shifting data (lag)
print("\nShifting data by 2 periods:")
print(time_series_df.shift(periods=2))

# Creating a rolling window
print("\nRolling 3-day window (mean):")
print(time_series_df.rolling(window=3).mean())

# 2.6 SQL-like Operations
print("SQL-like operations in pandas:")

# SELECT - column selection
print("\nSELECT equivalent (column selection):")
select_result = boston_df[['CRIM', 'RM', 'MEDV']]
print(select_result.head())

# WHERE - filtering
print("\nWHERE equivalent (filtering):")
where_result = boston_df[boston_df['MEDV'] > 30]
print(where_result.head())

# GROUP BY - aggregation
print("\nGROUP BY equivalent (aggregation):")
# Group by CHAS (Charles River dummy variable), compute mean for each group
groupby_result = boston_df.groupby('CHAS').mean()
print(groupby_result)

# ORDER BY - sorting
print("\nORDER BY equivalent (sorting):")
orderby_result = boston_df.sort_values('MEDV', ascending=False)
print(orderby_result.head())

# JOIN - will be covered in the merging section

# HAVING - filtering on aggregated results
print("\nHAVING equivalent (filtering on aggregated results):")
having_result = boston_df.groupby('RAD').filter(lambda x: x['MEDV'].mean() > 25)
print(having_result.head())

# COUNT, SUM, AVG - aggregation functions
print("\nCOUNT, SUM, AVG equivalents:")
print("COUNT:", boston_df['CHAS'].value_counts())
print("SUM:", boston_df['MEDV'].sum())
print("AVG:", boston_df['MEDV'].mean())

# 2.7 Data Cleaning
# Create a DataFrame with some issues to clean
print("Creating a dataset with issues to clean:")
np.random.seed(42)
cleaning_df = pd.DataFrame({
    'A': np.random.randn(10),
    'B': [1, 2, np.nan, 4, 5, 6, 7, np.nan, 9, 10],
    'C': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', np.nan],
    'D': np.random.choice(['X', 'Y', 'Z'], size=10),
    'E': pd.date_range(start='2023-01-01', periods=10)
})
print(cleaning_df)

# Check for missing values
print("\nMissing values count:")
print(cleaning_df.isnull().sum())

# Handling missing values - dropping
print("\nDropping rows with any missing values:")
print(cleaning_df.dropna())

# Handling missing values - filling with fixed value
print("\nFilling numerical missing values with 0:")
print(cleaning_df['B'].fillna(0))

# Filling missing values with method
print("\nFilling missing values with forward fill method:")
print(cleaning_df.fillna(method='ffill'))

# Filling different columns with different strategies
print("\nFilling different columns with different strategies:")
filled_df = cleaning_df.copy()
filled_df['B'] = filled_df['B'].fillna(filled_df['B'].mean())  # Fill B with mean
filled_df['C'] = filled_df['C'].fillna('unknown')  # Fill C with 'unknown'
print(filled_df)

# Removing duplicates
duplicated_df = pd.concat([cleaning_df, cleaning_df.iloc[0:3]])
print("\nDataFrame with duplicates:")
print(duplicated_df)

print("\nRemoving duplicates:")
print(duplicated_df.drop_duplicates())

# Detecting and handling outliers
print("\nDetecting outliers (Z-score method):")
from scipy import stats
z_scores = stats.zscore(boston_df['MEDV'].dropna())
print("Z-scores:", z_scores)
outliers = np.abs(z_scores) > 3
print("Outliers (Z-score > 3):", boston_df['MEDV'].iloc[outliers])

# Data type conversion
print("\nConverting data types:")
print("Original dtype of column D:", cleaning_df['D'].dtype)
cleaning_df['D'] = cleaning_df['D'].astype('category')
print("New dtype of column D:", cleaning_df['D'].dtype)

# String operations
print("\nString operations:")
print("Uppercase conversion:", cleaning_df['C'].str.upper())

# 2.8 Aggregation and Distribution Analysis
# Basic aggregation functions
print("Basic aggregation functions:")
print("\nSum:", boston_df.sum())
print("\nMean:", boston_df.mean())
print("\nMedian:", boston_df.median())
print("\nMin:", boston_df.min())
print("\nMax:", boston_df.max())
print("\nStandard deviation:", boston_df.std())

# Aggregate multiple statistics at once
print("\nMultiple statistics at once:")
print(boston_df.agg(['min', 'max', 'mean', 'median', 'std']))

# Aggregate different functions for different columns
print("\nDifferent aggregations per column:")
print(boston_df.agg({
    'CRIM': ['min', 'max', 'mean'],
    'RM': ['mean', 'std'],
    'MEDV': ['median', 'std', 'count']
}))

# Distribution analysis
print("\nDistribution analysis:")
print("Quantiles:")
print(boston_df.quantile([0.1, 0.25, 0.5, 0.75, 0.9]))

# Histogram
print("\nHistogram bins for MEDV:")
print(pd.cut(boston_df['MEDV'], bins=5).value_counts())

# Value counts for categorical data
print("\nValue counts for RAD (categorical):")
print(boston_df['RAD'].value_counts())

# Correlation matrix
print("\nCorrelation matrix:")
print(boston_df.corr())

# Visualize a histogram (uncomment to run)
# plt.figure(figsize=(10, 6))
# boston_df['MEDV'].hist(bins=20)
# plt.title('Housing Price Distribution')
# plt.xlabel('MEDV (Housing Price)')
# plt.ylabel('Frequency')
# plt.show()

# 2.9 Data Merging and Joining
# Create Bologna housing data
print("Creating Bologna housing dataset for merging examples:")
np.random.seed(42)
bologna_housing = pd.DataFrame({
    'property_id': range(1, 11),
    'area_sqm': np.random.uniform(50, 200, size=10).round(0),
    'rooms': np.random.randint(1, 6, size=10),
    'price': np.random.uniform(100000, 500000, size=10).round(-3),
    'neighborhood': np.random.choice(['Centro', 'San Donato', 'Navile', 'Santo Stefano', 'San Vitale'], size=10)
})
print(bologna_housing)

# Create property features dataset
bologna_features = pd.DataFrame({
    'property_id': range(1, 15),  # Note: includes IDs not in housing data
    'has_balcony': np.random.choice([True, False], size=14),
    'floor': np.random.randint(0, 10, size=14),
    'year_built': np.random.randint(1900, 2020, size=14)
})
print("\nBologna property features:")
print(bologna_features)

# Inner join (only matching property_id)
print("\nInner join:")
inner_join = pd.merge(bologna_housing, bologna_features, on='property_id', how='inner')
print(inner_join)

# Left join (all properties from housing data)
print("\nLeft join:")
left_join = pd.merge(bologna_housing, bologna_features, on='property_id', how='left')
print(left_join)

# Right join (all properties from features data)
print("\nRight join:")
right_join = pd.merge(bologna_housing, bologna_features, on='property_id', how='right')
print(right_join)

# Outer join (all properties from both datasets)
print("\nOuter join:")
outer_join = pd.merge(bologna_housing, bologna_features, on='property_id', how='outer')
print(outer_join)

# Joining with different key names
# Create neighborhood data
neighborhood_data = pd.DataFrame({
    'name': ['Centro', 'San Donato', 'Navile', 'Santo Stefano', 'San Vitale'],
    'safety_score': np.random.uniform(7, 10, size=5).round(1),
    'transport_score': np.random.uniform(6, 10, size=5).round(1)
})
print("\nNeighborhood data:")
print(neighborhood_data)

# Join housing with neighborhood data (different key names)
print("\nJoin with different key names:")
neighborhood_join = pd.merge(
    bologna_housing, 
    neighborhood_data,
    left_on='neighborhood',  # key in bologna_housing
    right_on='name',         # key in neighborhood_data
    how='left'
)
print(neighborhood_join)

# Concatenation (stacking DataFrames)
print("\nConcatenation (vertical stacking):")
bologna_housing_more = pd.DataFrame({
    'property_id': range(11, 16),
    'area_sqm': np.random.uniform(50, 200, size=5).round(0),
    'rooms': np.random.randint(1, 6, size=5),
    'price': np.random.uniform(100000, 500000, size=5).round(-3),
    'neighborhood': np.random.choice(['Centro', 'San Donato', 'Navile', 'Santo Stefano', 'San Vitale'], size=5)
})

concat_result = pd.concat([bologna_housing, bologna_housing_more], axis=0)
print(concat_result)

# Horizontal concatenation
print("\nHorizontal concatenation:")
extra_features = pd.DataFrame({
    'property_id': range(1, 11),
    'has_garage': np.random.choice([True, False], size=10),
    'has_garden': np.random.choice([True, False], size=10)
})

h_concat = pd.concat([bologna_housing, extra_features.set_index('property_id')], axis=1)
print(h_concat)

# 3. Hands-on Exercise: Pima Indians Diabetes Dataset
# Load the Pima Indians Diabetes dataset (or create mock data if not available)
try:
    pima_df = pd.read_csv('pima-indians-diabetes.csv')
    print("Pima Indians Diabetes dataset loaded successfully!")
except FileNotFoundError:
    print("Pima Indians Diabetes dataset not found, creating mock data...")
    np.random.seed(42)
    n_samples = 100
    
    pima_df = pd.DataFrame({
        'Pregnancies': np.random.randint(0, 15, size=n_samples),
        'Glucose': np.random.randint(50, 200, size=n_samples),
        'BloodPressure': np.random.randint(40, 120, size=n_samples),
        'SkinThickness': np.random.randint(10, 50, size=n_samples),
        'Insulin': np.random.randint(0, 300, size=n_samples),
        'BMI': np.random.uniform(15, 50, size=n_samples).round(1),
        'DiabetesPedigreeFunction': np.random.uniform(0.1, 1.5, size=n_samples).round(3),
        'Age': np.random.randint(20, 80, size=n_samples),
        'Outcome': np.random.choice([0, 1], size=n_samples, p=[0.65, 0.35])  # 0: No diabetes, 1: Diabetes
    })

print("Pima Indians Diabetes dataset preview:")
print(pima_df.head())

print("\nDataset information:")
print(pima_df.info())

print("\nBasic statistics:")
print(pima_df.describe())

# Exercise: Complete the following tasks (10 minutes)
# 1. Check for missing values in the dataset. If any, replace them with the mean of the respective column.
# 2. Create a new column 'BMI_Category' that categorizes BMI into 'Underweight' (<18.5), 'Normal' (18.5-24.9), 'Overweight' (25-29.9), and 'Obese' (>=30).
# 3. Calculate the mean and standard deviation of glucose levels for each BMI category, grouped by Outcome.
# 4. Find the correlation between all numeric columns and sort them in descending order relative to 'Outcome'.
# 5. Create a new DataFrame that only includes women who are over 40 and have had at least 1 pregnancy.
# 6. Bonus: Create a pivot table that shows the average BMI for each combination of Age group (20-39, 40-59, 60+) and Outcome.

# Example solution (to be revealed after exercise time):
"""
# 1. Check and handle missing values
print("\n1. Checking for missing values:")
print(pima_df.isnull().sum())

# In Pima dataset, 0 values in certain columns are likely missing values
zero_mask = (pima_df['Glucose'] == 0) | (pima_df['BloodPressure'] == 0) | \
            (pima_df['SkinThickness'] == 0) | (pima_df['Insulin'] == 0) | \
            (pima_df['BMI'] == 0)

# Replace 0s with NaN
cols_to_fix = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
pima_df[cols_to_fix] = pima_df[cols_to_fix].replace(0, np.nan)

# Check missing values again
print("Missing values after replacing zeros:")
print(pima_df.isnull().sum())

# Fill missing values with mean
for col in cols_to_fix:
    mean_value = pima_df[col].mean()
    pima_df[col].fillna(mean_value, inplace=True)

print("Missing values after filling with mean:")
print(pima_df.isnull().sum())

# 2. Create BMI category
def bmi_category(bmi):
    if bmi < 18.5:
        return 'Underweight'
    elif bmi < 25:
        return 'Normal'
    elif bmi < 30:
        return 'Overweight'
    else:
        return 'Obese'

pima_df['BMI_Category'] = pima_df['BMI'].apply(bmi_category)
print("\n2. BMI categories:")
print(pima_df['BMI_Category'].value_counts())

# 3. Glucose statistics by BMI category and Outcome
print("\n3. Glucose statistics by BMI category and Outcome:")
glucose_stats = pima_df.groupby(['BMI_Category', 'Outcome'])['Glucose'].agg(['mean', 'std'])
print(glucose_stats)

# 4. Correlations with Outcome
print("\n4. Correlations with Outcome (sorted):")
correlations = pima_df.corr()['Outcome'].sort_values(ascending=False)
print(correlations)

# 5. Women over 40 with at least 1 pregnancy
print("\n5. Women over 40 with at least 1 pregnancy:")
filtered_df = pima_df[(pima_df['Age'] > 40) & (pima_df['Pregnancies'] >= 1)]
print(filtered_df.head())
print(f"Number of women in this group: {len(filtered_df)}")

# 6. Pivot table for BMI by Age group and Outcome
print("\n6. Pivot table for BMI by Age group and Outcome:")
# Create age groups
def age_group(age):
    if age < 40:
        return '20-39'
    elif age < 60:
        return '40-59'
    else:
        return '60+'

pima_df['Age_Group'] = pima_df['Age'].apply(age_group)

# Create pivot table
pivot = pd.pivot_table(
    pima_df, 
    values='BMI',
    index='Age_Group',
    columns='Outcome',
    aggfunc='mean'
)
print(pivot)
"""
