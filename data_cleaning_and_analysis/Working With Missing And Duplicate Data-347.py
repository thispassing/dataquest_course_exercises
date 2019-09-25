## 1. Introduction ##

shape_2015 = happiness2015.shape
shape_2016 = happiness2016.shape
shape_2017 = happiness2017.shape

## 2. Identifying Missing Values ##

missing_2016 = happiness2016.isnull().sum()
missing_2017 = happiness2017.isnull().sum()

## 3. Correcting Data Cleaning Errors that Result in Missing Values ##

happiness2017.columns = happiness2017.columns.str.replace('.', ' ').str.replace('\s+', ' ').str.strip().str.upper()
happiness2015.columns = happiness2015.columns.str.replace('[\(\)]', ' ').str.replace('\s+', ' ').str.strip().str.upper()
happiness2016.columns = happiness2016.columns.str.replace('[\(\)]', ' ').str.replace('\s+', ' ').str.strip().str.upper()

combined = pd.concat([happiness2015, happiness2016, happiness2017], ignore_index=True)
missing = combined.isnull().sum()

## 4. Visualizing Missing Data ##

regions_2017 = combined[combined['YEAR'] == 2017]['REGION']
missing = regions_2017.isnull().sum()
regions_2017.shape

## 5. Using Data From Additional Sources to Fill in Missing Values ##

combined = pd.merge(left=combined, right=regions, on='COUNTRY', how='left')
combined = combined.drop('REGION_x', axis=1)
missing = combined.isnull().sum()

## 6. Identifying Duplicates Values ##

combined['COUNTRY'] = combined['COUNTRY'].str.upper()
dups = combined.duplicated(['COUNTRY', 'YEAR'])
print(combined[dups])

## 7. Correcting Duplicates Values ##

combined['COUNTRY'] = combined['COUNTRY'].str.upper()

combined = combined.drop_duplicates(subset=(['COUNTRY', 'YEAR']))