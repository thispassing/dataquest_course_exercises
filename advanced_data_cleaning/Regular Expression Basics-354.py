## 1. Introduction ##

import pandas as pd
hn = pd.read_csv('hacker_news.csv')
hn.describe()

## 2. The Regular Expression Module ##

import re

titles = hn["title"].tolist()
python_mentions = 0
pattern = "[Pp]ython"

for title in titles:
    if re.search(pattern, title):
        python_mentions +=1
 

## 3. Counting Matches with pandas Methods ##

pattern = '[Pp]ython'
titles = hn['title']
python_mentions = titles.str.contains(pattern).sum()

## 4. Using Regular Expressions to Select Data ##

titles = hn['title']
pattern = "[Rr]uby"
ruby_titles = titles[titles.str.contains(pattern)]

## 5. Quantifiers ##

# The `titles` variable is available from
# the previous screens
pattern = "e-?mail"
email_bool = titles.str.contains(pattern)
email_count = email_bool.sum()
email_titles = titles[email_bool]


## 6. Character Classes ##

pattern = "\[\w+\]"
tag_titles = titles[titles.str.contains(pattern)]
tag_count = tag_titles.shape[0]

## 7. Accessing the Matching Text with Capture Groups ##

pattern = r"\[(\w+)\]"
tag_freq = titles.str.extract(pattern).value_counts()


## 8. Negative Character Classes ##

def first_10_matches(pattern):
    """
    Return the first 10 story titles that match
    the provided regular expression
    """
    all_matches = titles[titles.str.contains(pattern)]
    first_10 = all_matches.head(10)
    return first_10

pattern = r"[Jj]ava[^Ss]"
java_titles = titles[titles.str.contains(pattern)]
