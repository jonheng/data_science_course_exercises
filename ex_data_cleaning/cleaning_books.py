'''
books.csv is a CSV file containing information about
books from the British Library
'''

import pandas as pd
import numpy as np

# Loads csv file into pandas dataframe
df = pd.read_csv('books.csv')

# Displays top 5 rows of dataframe
df.head()

# Displays shape of dataframe (number of rows, number of columns)
df.shape

# Displays columns
df.columns

# Let's drop the unnecessary columns
to_drop = ['Edition Statement',
           'Corporate Author',
           'Corporate Contributors',
           'Former owner',
           'Engraver',
           'Contributors',
           'Issuance type',
           'Shelfmarks',
           'Flickr URL']
df.drop(to_drop, inplace=True, axis='columns')

# Inspect again to see that the columns specified are removed
df.head()

# Replace existing index with the 'Identifier' column
df = df.set_index('Identifier') # Note the difference with the df.drop above. By specifying
                                # the inplace, we do not have to reassign the df
df.head()

# You can then access each record through its index with loc[]
df.loc[206]

# To access it by position, we can use df.iloc[]
df.iloc[0]

# Check the datatypes of each column
df.dtypes
df.get_dtype_counts()
# All of them should be of object type. This is similar to strings.
# In other words, all the data is currently in a string format.

# Let's convert the 'Date of Publication' to a numeric value
# First let us take a look at the values inside the column
df['Date of Publication']

# There are multiple formats:
# - Square brackets, e.g. [1845]
# - Date ranges, e.g. 1898-1912
# - Various punctuations, e.g. 1831, 32 / [1845.] / [1897?]
# - NaN (not a number) values, which are equivalent to missing values
# One way to clean this column and make it consistent is to take only the first 4 digits.
# This can be done through regular expressions, which are a way to
# do pattern matching in strings.
# You can go to https://regexr.com/ or any other sites by googling to
# learn more about regular expressions.

# The below regular expression has 4 parts
# 1. '^' represents starting the search from the start of the string
# 2. '\d' represents searching for any digits i.e. from 0 to 9
# 3. '{4}' represents repeating the previous rule 4 times i.e. search for 4 digits
# 4. The parentheses '()' groups together a set of rules
regex = '^(\d{4})'

# Apply regex to the column
df['Date of Publication'] = df['Date of Publication'].str.extract(regex)

# Drop rows with NaN in 'Date of Publication' column
df = df.dropna(subset=['Date of Publication'])

# Convert row dtype to int64
df['Date of Publication'] = df['Date of Publication'].astype('int64')

# Check how the dataframe has changed!
df.shape
df.dtypes

# Let's look at the 'Place of Publication' column now
df['Place of Publication']

# Issues:
# 1.
# [216]: London; Virtue & Yorston
# We want to change everything that contains 'London' to be 'London' only
# 2.
# [4157862]: Newcastle-upon-Tyne
# [4159587]: Newcastle upon Tyne

# Replaces hyphens in column with spaces

df['Place of Publication'] = df['Place of Publication'].str.replace('-', ' ')

# Use np.where to use a condition followed by the if value and else value
# i.e. np.where(condition, if return value, else return value)
# Apply this to the entire column of values
df['Place of Publication'] = np.where(df['Place of Publication'].str.contains('London'),
                                      'London',
                                      df['Place of Publication'])

# This can be done for the other values in this column!
# There are many more operations that can be done, such as removing multiple white spaces

# Save it into a new csv file!
df.to_csv('books_processed.csv')
