
# coding: utf-8

# # Exercise 1
# 
# Parse the following dates and sort them by first 'date' then 'index' (== original position) and return a Series in the following form:
# ```
# 23   1971-07-08
# 19   2008-06-01
# 7    2009-01-01
# 21   2009-01-01
# 16   2009-02-01
# 4    2009-03-20
# 5    2009-03-20
# 6    2009-03-20
# 9    2009-03-20
# 10   2009-03-20
# 11   2009-03-20
# 12   2009-03-20
# 13   2009-03-20
# 14   2009-03-21
# 15   2009-03-22
# 0    2009-04-20
# 1    2009-04-20
# 17   2009-09-01
# 20   2009-12-01
# 22   2010-01-01
# 18   2010-10-01
# 3    2011-04-03
# 2    2014-04-20
# 8    2017-03-20
# Name: dt, dtype: datetime64[ns]
# ```
# Hints:
# - first column is the original position (index)
# - think about using `pd.to_datetime()`

# In[22]:


import pandas as pd

time_values = '''I come at 04/20/2009 ...; 04/20/09 in Bremen; 4/20/14 maybe; or 4/3/2011 also possible; 
never at Mar-20-2009, but maybe later; how about Mar 20, 2009 or not; Moskow: March 20, 2009, 12:00; 
in Koeln, Mar. 20, 2009 however; Why not Mar 20 2017 ?; Clear picture for 20 Mar 2009; In the iden of 20 March 2009;
20 Mar. 2009 in Dresden; 20 March, 2009 BR; Mar 20th, 2009 Hamburg; Current date: Mar 21st, 2009; 
Mar 22nd is spring, 2009 Kiel; Feb 2009 is winter; Sep 2009; long ago in Oct 2010; 6/2008 vacation in Schwerin; 12/2009 blackout; 2009 timeout; Year 2010 the rest is history;
Soccer game at 7/8/71 in NY'''

time_s = pd.Series(time_values.split(';')).str.strip()
time_s


# In[23]:


def date_sorter(df):
    pattern1 = '(\d{1,2}-\d{1,2}-[12]?\d{2,3})'
    pattern2 = '((\d{1,2}/)*(\d{1,2})*/[12]?\d{2,3})'
    pattern3 = '(\d{1,2}\s)*((january|february|march|april|june|july|august|september|october|november|december)[-,.\s]?(\d{1,2}\w*)?[-,.\s]*([12]\d{3}))'
    pattern4 = '(\d{1,2}\s)*((jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[-,.\s]?(\d{1,2}\w*)?[-,.\s]*([12]\d{3}))'
    pattern5 = '[12]\d{3}'

    pattern = '(%s|%s|%s|%s|%s)' % (pattern1,pattern2,pattern3,pattern4,pattern5)

    date_df = df.str.lower().str.extract(pattern, expand=False) 
    date_df['dt'] = pd.to_datetime(date_df[0], errors='coerce')
    
    return date_df.reset_index().sort_values(by=['dt','index'])['dt']

date_sorter(time_s)

