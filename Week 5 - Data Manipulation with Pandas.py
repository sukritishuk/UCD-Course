## Working with Pandas DataFrame -
# import libraries:
import pandas as pd
# define data file and read the same as a Pandas DataFrame:
file = 'Files/winequality-white.csv'
data = pd.read_csv(file, sep=';')
# exploring the dataframe:
print(data.head())
print(data.info())
print(data.describe())
print(data.values)
print(data.columns)
print(data.index)

## Sorting and subsetting
# sorting a column - ascending:
data.sort_values('alcohol')
# sorting a column - descending:
data.sort_values('alcohol',ascending=False)
# sorting by multiple columns/variables:
data.sort_values(['alcohol','quality'])
data.sort_values(['alcohol','quality'],ascending=[True,False])
# subsetting a column:
data["volatile acidity"]
# subsetting multiple columns:
data[["citric acid","quality"]]
# subsetting rows (as a boolean):
data["quality"]==7
# subsetting rows (as all the relevant rows):
data[data["quality"] == 7]
# subsetting on multiple conditions: & operator so both conditions must be True
wine_quality = data["quality"] == 7
wine_alcohol = data["alcohol"] > 14
print(data[wine_quality & wine_alcohol])
print(data[(data["quality"]==7) & (data["alcohol"] > 14)])
# subsetting using .isin() method:
# prints rows where quality is 6 or 7 -
print(data[data["quality"].isin([7,6]))

## Summary Statistics -
# computing Mean for alcohol column -
print(data['alcohol'].mean())
# computing Min for quality column -
data['quality'].min()
# .agg() function - return 30th percentile for fixed acidity column
def pct30(column):
    return column.quantile(0.3)
print(data['fixed acidity'].agg(pct30))
# return 30th percentile for multiple columns
print(data[['citric acid','sulphates']].agg(pct30))
# return 30th & 40th percentile on a column
def pct40(column):
    return column.quantile(0.4)
print(data["volatile acidity"].agg([pct30,pct40]))
# cumulative sum
print(data["quality"].cumsum())

## Counting -
# dropping duplicates from quality column:
print(data.drop_duplicates(subset='quality'))
# dropping duplicates from alcohol and quality columns:
print(data.drop_duplicates(subset=['alcohol','quality']))
# count the number of fixed acidity type wines:
print(data['fixed acidity'].value_counts(sort=False, normalize=True))

## Grouped Summary Statistics -
# summaries by group:
print(data.groupby('fixed acidity')['quality'].mean())
# multiple grouped summaries:
print(data.groupby(['fixed acidity','alcohol'])['quality'].mean())
# many groups, many summaries:
print(data.groupby(['fixed acidity','alcohol'])[['quality','citric acid']].mean())

## Pivot Tables -
print(data.pivot_table(values='alcohol',index='quality'))
# different statistics: mean alcohol for each quality of wine
import numpy as np
print(data.pivot_table(values='alcohol',index='quality',aggfunc=np.median))
# multiple statistics: mean & median alcohol for each quality of wine
print(data.pivot_table(values='alcohol',index='quality',aggfunc=[np.mean,np.median]))
# pivot on two variables and filling missing values with zeroes:
print(data.pivot_table(values='alcohol',index='quality',columns='sulphates'))
print(data.pivot_table(values='alcohol',index='quality',columns='sulphates',fill_value=0))
# summing with pivot tables:
print(data.pivot_table(values='alcohol',index='quality',columns='sulphates',fill_value=0,margins=True))


## Explicit indexes -
# setting a column as index:
print(data.set_index('fixed acidity'))
# removing an index:
print(data.reset_index())
# dropping an index:
data.reset_index(drop=True)
# subsetting with indices:
data_ind = data.set_index('fixed acidity')
print(data_ind)
# subsetting where fixed acidity equals 7.2:
data_ind.loc[7.2]
# subsetting with multi-level indexes or Hierarchical indexes:
# step 1 - set multi-level indices (fixed acidity & alcohol)
data_ind2 = data.set_index(['fixed acidity','quality'])
print(data_ind2)
# step 2 - subsetting outer level from multi-level indexes
data_ind2.loc[[7.2,8.1]]
# step 3 - subsetting inner level from multi-level indexes
data_ind2.loc[[(7.2,6),(8.1,5)]]
# sorting by index values:
data_ind2.sort_index()
# controlling sort_index:
data_ind2.sort_index(level=['fixed acidity','quality'],ascending=[True,False])


## Slicing and subsetting with .loc and .iloc -
# Slicing outer level index: here quality 7 is included
data_ind3 = data.set_index('quality').sort_index()
print(data_ind3)
data_ind3.loc[3:7]
# Slicing inner level index:
data_ind4 = data.set_index(['quality','alcohol']).sort_index()
print(data_ind4)
data_ind4.loc[(4,9.1):(5,11.0)]
# slicing columns:
data_ind4.loc[:,'volatile acidity':'pH']
# Slicing by rows/column number: using .iloc() method
data_ind4.iloc[2:5,3:6]


## Working with Pivot Tables -
# calculate the statistic across rows:
data_ind4.mean(axis = 'index')
# calculating summary stats across columns:
data_ind4.mean(axis = 'columns')