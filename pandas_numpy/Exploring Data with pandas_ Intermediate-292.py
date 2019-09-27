## 2. Reading CSV files with pandas ##

f500 = pd.read_csv('f500.csv')
f500.loc[f500["previous_rank"] == 0, "previous_rank"] = np.nan

## 3. Using iloc to select by integer position ##

fifth_row = f500.iloc[4]
company_value = f500.loc[0,"company"]

## 4. Using iloc to select by integer position continued ##

import pandas as pd
import numpy as np

f500 = pd.read_csv("f500.csv", index_col=0)
f500.index.name = None
f500.loc[f500["previous_rank"] == 0, "previous_rank"] = np.nan

fifth_row = f500.iloc[4]
first_three_rows = f500.iloc[0:3]
first_seventh_row_slice = f500.iloc[[0,6],0:5]

## 5. Using pandas methods to create boolean masks ##

previously_ranked = f500[f500["previous_rank"].notnull()]
rank_change = previously_ranked["rank"] - previously_ranked["previous_rank"]

## 6. Working with Integer Labels ##

null_previous_rank = f500[f500["previous_rank"].isnull()]
top5_null_prev_rank = null_previous_rank.iloc[:5]

## 7. Pandas Index Alignment ##

previously_ranked = f500[f500["previous_rank"].notnull()]
rank_change = previously_ranked['previous_rank'] - previously_ranked['rank']
f500['rank_change'] = rank_change

## 8. Using Boolean Operators ##

big_rev_neg_profit = f500.loc[(f500["revenues"] > 100000) & (f500["profits"] < 0)]
tech_outside_usa = f500.loc[(f500["country"] != "USA") & (f500["sector"] == "Technology")].head()




## 9. Using Boolean Operators Continued ##

bv_bool = (f500["country"] == "Brazil") | (f500["country"] == "Venezuela")
brazil_venezuela = f500[bv_bool]

tu_bool = (f500["sector"] == "Technology") & (f500["country"] != "USA")
tech_outside_usa = f500[tu_bool].head(5)

## 10. Sorting Values ##

selected_rows = f500[f500["country"] == "Japan"]
sorted_rows = selected_rows.sort_values('employees', ascending=False)
first_row = sorted_rows.iloc[0]
top_japanese_employer = first_row.loc["company"]
                     

## 11. Using Loops with pandas ##

top_employer_by_country = {}

countries = f500["country"].unique()

for c in countries:
    selected_rows = f500[f500["country"] == c]
    selected_rows = selected_rows.sort_values(by="employees",ascending=False)
    selected_row = selected_rows.iloc[0,:]
    company = selected_row["company"]
    top_employer_by_country.update({c:company})

## 12. Challenge: Calculating Return on Assets by Country ##

f500["roa"] = f500["profits"] / f500["assets"]

top_roa_by_sector = {}

sectors = f500["sector"].unique()

for s in sectors:
    selected_rows = f500[f500["sector"] == s]
    selected_rows = selected_rows.sort_values(by="roa",ascending=False)
    selected_row = selected_rows.iloc[0,:]
    company = selected_row["company"]
    top_roa_by_sector.update({s:company})