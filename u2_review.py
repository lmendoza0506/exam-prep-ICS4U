# 1) Jupyter Notebooks and its Advantages

# JUPYTER NOTEBOOK - computing environments that allow sharing of live code
## execute code interactively and seeing the result below each line
## combination of code cells and markdown cells
## integrates with data visualization libraries

# 2) DataFrame vs DataSeries - data structure for handling tabular data

# DATAFRAME - 2D labeled structure with columns; like a spreadsheet
# axes: 0 - rows, 1 - column
# two indices: row and column indices
# complemented by data series


# DATASERIES - 1D array that holds data of any type
## often represents a single column OR row of data from a DF
## consists of Identifiers and Values
# one index: row labels

# 3) DF Organization - extends beyond Rows and Columns

# RC Indexing: accessed using numerical indices (row and column numbers)
# DF Indexing: accessed using associated labels with columns

# 4) loc vs iloc

df = {'Name':['Alice', 'Bob'],
      'Age':[25, 30]
      }

# ILOC - integer location; integer-based indexing
# df.iloc[0] - first ROW
# df.loc[:, 0] - first COLUMN

# NOTE: colon is to specify ALL ROWS

# LOC - location; label-based indexing (using index n)
# df.loc['Alice'] - row with label 'Alice'
# df.loc[:, 'Age']

# 5) .count() vs .valuecounts()

# COUNT - method that returns number of non-null values in a DF column (one series)
## result is the count of different things for the Series

# VALUECOUNTS - method that returns count of unique values in a DF column
## counts the occurrences of each UNIQUE value in the Series

# COUNT - counts how many things are in a DS
# VALUESCOUNT - counts frequency of each thing in a DS

# 6) Advantage of Pandas module

# PANDAS - provides DF and DS; manipulate tabular data
## aligns data based on rows and columns; easy operations on data with different indices
## functions and method used for data sorting, grouping, and aggregating