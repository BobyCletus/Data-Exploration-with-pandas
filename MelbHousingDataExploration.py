# install pandas
# import pandas
import pandas as pd
housing_data = pd.read_csv('melb_data.csv')
print(housing_data)
# to get wider picture of variables while printing df to console
import numpy as np

new_width=300

pd.set_option('display.width', new_width)

np.set_printoptions(linewidth=new_width)

pd.set_option('display.max_columns',12)
print(housing_data)
print(housing_data.head(8))
# debug+variable + view as df will give full view of the data set
# summary of the data set
print(housing_data.describe())
avg_house_price = int(round(housing_data['Price'].mean()))
print(avg_house_price)
avg_land_area = int(round(housing_data['LotArea'].mean()))
print(avg_land_area)