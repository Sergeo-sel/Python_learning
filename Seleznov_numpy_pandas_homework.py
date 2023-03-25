import numpy as np
import math
import pandas as pd
import ssl

# Create an an array with shape (4, 3) of: a. all zeros b. ones c. numbers from 0 to 11

a = np.zeros((4, 3))
b = np.ones((4, 3))
c = np.arange(0, 12).reshape((4, 3))

print(a)
print(b)
print(c)

# 2. Tabulate the following function: F(x) = 2x^2 + 5, x in [1,100]

x = np.arange(1, 101)
f_x = 2 * x**2 + 5

print(f_x)


# 3. Tabulate the following function: F(x) = e^(-x), x in [-10,10]

x = np.arange(-10, 10)
f_x = math.e ** (-x)

print(f_x)


# 4. Import the dataset from this address and assign it to df variable
# new_table = requests.get('https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/02_Filtering_%26_Sorting/Euro12/Euro_2012_stats_TEAM.csv')
# print(new_table.content)

ssl._create_default_https_context = ssl._create_unverified_context

df=pd.read_csv("https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/02_Filtering_%26_Sorting/Euro12/Euro_2012_stats_TEAM.csv")
print(df)


# 5. Select only the Team, Yellow Cards and Red Cards columns.

my_columns= ["Team", "Yellow Cards", "Red Cards"]
print(df[my_columns])


# 6. How many teams participated in the Euro2012?

participations = len(df.index)
print(f'Number of the team participations on the Euro2012 is {participations}')


# 7. Filter teams that scored more than 6 goals

print(df[df.Goals > 6])
