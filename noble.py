import pandas as pd

# Load the data
data = pd.read_csv("noble.csv")

# Question 1
top_gender = data['sex'].mode()[0]
top_country = data['birth_country'].mode()[0]

# Question 2
us_winners = data[data['birth_country'] == 'United States']
us_decades = us_winners['year'] // 10 * 10
max_decade_usa = us_decades.mode()[0]

# Question 3
female_winners = data[data['sex'] == 'Female']
female_proportions = female_winners.groupby(['year', 'category']).size() / data.groupby(['year', 'category']).size()
max_female_dict = female_proportions.idxmax()

# Question 4
first_woman = data[data['sex'] == 'Female'].iloc[0]
first_woman_name = first_woman['full_name']
first_woman_category = first_woman['category']

# Question 5
repeat_winners = data['full_name'].value_counts()[data['full_name'].value_counts() > 1].index.tolist()
repeat_list = [name for name in repeat_winners]

# Results
top_gender, top_country, max_decade_usa, max_female_dict, first_woman_name, first_woman_category, repeat_list