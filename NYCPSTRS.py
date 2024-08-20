# Every year, American high school students take SATs, which are standardized tests intended to measure literacy, numeracy, and writing skills. There are three sections - reading, math, and writing, each with a maximum score of 800 points. These tests are extremely important for students and colleges, as they play a pivotal role in the admissions process.

# Analyzing the performance of schools is important for a variety of stakeholders, including policy and education professionals, researchers, government, and even parents considering which school their children should attend.

# You have been provided with a dataset called schools.csv, which is previewed below.

# You have been tasked with answering three key questions about New York City (NYC) public school SAT performance.

# Re-run this cell 
import pandas as pd
import numpy as np

# Read in the data
schools = pd.read_csv('MatplotlibProject/schools1.csv')

# Preview the data
print(schools.info())

# Best schools in math have at least 80% of the maximum score for that test. Save as best_math_results, include school_name, average_math and sort by average_math
best_math_schools = schools[schools['average_math']>=640][['school_name', 'average_math']].sort_values('average_math', ascending=False)
print(best_math_schools.info())

# What are the top 10 performing schools?
top_10_schools = pd.DataFrame()
top_10_schools['school_name'] = schools['school_name']
total_SAT = schools['average_math'] + schools['average_reading'] + schools['average_writing']
top_10_schools['total_SAT'] = total_SAT
top_10_schools = top_10_schools.sort_values(by='total_SAT', ascending=False)
top_10_schools = top_10_schools[0:10]
print(top_10_schools)

# Whick single borough has the largest standard deviation in the combined SAT score?
largest_std_dev = pd.DataFrame()
largest_std_dev['borough'] = schools['borough']
largest_std_dev['total_SAT'] = total_SAT
largest_std_dev = largest_std_dev.groupby('borough')['total_SAT'].agg(['count', 'mean', 'std']).round(2)
largest_std_dev = largest_std_dev[largest_std_dev['std'] == largest_std_dev['std'].max()].rename(columns={'count': 'num_schools', 'mean': 'average_SAT', 'std': 'std_SAT'})
print(largest_std_dev)