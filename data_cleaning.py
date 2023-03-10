# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 18:18:04 2023

@author: apoorva
"""

import pandas as pd
df = pd.read_csv("glassdoor_jobs.csv")

# salary parsing

df['hourly'] = df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)
df['employer provided'] = df['Salary Estimate'].apply(lambda x: 1 if 'employer provided salary' in x.lower() else 0)

df = df[df['Salary Estimate'] != "-1"]
salary = df['Salary Estimate'].apply(lambda x: x.split(" ")[0])
wo_sgn = salary.apply(lambda x: x.replace('K', "").replace('$', ""))

min_hr = wo_sgn.apply(lambda x: x.lower().replace('per hour', '').replace('employer provided salary', '').replace('(employer', '').replace('employer', '0-0'))

df['min_salary'] = min_hr.apply(lambda x: int(x.split('-')[0]) )
df['max_salary'] = min_hr.apply(lambda x: int(x.split('-')[1]) )
df['avg_salary'] = df['max_salary']/2+df['min_salary']/2

# company name text
df['company_txt'] = df.apply(lambda x: x['Company Name'] if x['Rating']<0 else x['Company Name'][:-3], axis =1)

# state field
df['job_state'] = df['Location'].apply(lambda x: x.split(',')[1])
df.job_state.value_counts()

# is job in same location as headquarters
df['same_state'] = df.apply(lambda x: 1 if x.Location == x.Headquarters else 0, axis = 1)

# company age
df['age'] = df.Founded.apply(lambda x: x if x<1 else 2023 - x)

# jd parsing
df['python_yn'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
df['R_yn'] = df['Job Description'].apply(lambda x: 1 if 'r studio' in x.lower() or 'r-studio' in x.lower() else 0)
df['saprk_yn'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)
df['aws_yn'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)
df['excel_yn'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)

df.drop('Unnamed : 0', axis = 1)
df.to_csv("salary_data_cleaned.csv", index=False)


